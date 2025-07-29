import os
import json
import time
from datetime import datetime
from typing import List, Optional, Tuple

import openai
from dotenv import load_dotenv
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
import torch
import torch.nn.functional as F
import numpy as np
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

from app.models.diary import DiaryAnalysisResponse, DiaryChunk, EmotionSituationExtraction

# 환경설정
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class DiaryAnalyzer:
    """일기 분석 및 코멘트 생성 서비스"""
    
    def __init__(self):
        # ChromaDB 설정
        self.diary_embedding_function = SentenceTransformerEmbeddingFunction(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )
        self.general_embedding_function = SentenceTransformerEmbeddingFunction(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        self.client = chromadb.PersistentClient(path="./chroma_rag")
        self.pre_diary_col = self.client.get_or_create_collection(
            name="diary_past_diaries", 
            embedding_function=self.diary_embedding_function
        )
        self.advice_col = self.client.get_or_create_collection(
            name="diary_advice", 
            embedding_function=self.general_embedding_function
        )
        self.quote_col = self.client.get_or_create_collection(
            name="diary_quotes", 
            embedding_function=self.general_embedding_function
        )
    
    def preprocess_diary(self, raw_diary: str, max_retries: int = 3) -> str:
        """일기 전처리 - 문법 및 문맥 정리"""
        prompt = f"""
다음은 사용자가 쓴 일기입니다.  
이 일기를 문법적으로 자연스럽게 다듬고, 문맥 흐름도 매끄럽게 정리해주세요.  
내용을 바꾸지 말고, 표현을 다듬기만 하세요.

📜 원본 일기:
{raw_diary}

📦 출력 형식:
```text
(수정된 일기 전체 문장)
```
"""
        for attempt in range(max_retries):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "너는 문장 교정에 특화된 한국어 편집기야. 일기를 자연스럽게 고쳐줘."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
                content = response.choices[0].message.content.strip()
                if "```" in content:
                    content = content.split("```")[1].strip()
                return content
            except Exception as e:
                print(f"⚠️ 일기 전처리 실패 {attempt+1}회: {e}")
                time.sleep(1)
        return raw_diary
    
    def chunk_diary_by_meaning(self, diary_text: str, max_retries: int = 3) -> List[str]:
        """의미 단위로 일기 청크 분할"""
        prompt = f"""
다음은 한 사용자가 쓴 일기입니다.  
이 일기를 **의미 단위**로 나눠서 문장 단위로 청크(덩어리)로 만들어 주세요.  

조건:
- 각 청크는 명확한 의미 흐름을 가져야 합니다.
- 문장은 자르지 말고, 자연스럽게 연결된 문장끼리 묶어 주세요.
- 출력은 리스트(JSON 배열) 형태로 주세요.

📜 일기:
{diary_text}

📦 출력 형식:
```json
[
  "청크1",
  "청크2"
]
```
"""
        for attempt in range(max_retries):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "너는 텍스트를 의미 단위로 나누는 전문 청크 분석기야."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
                content = response.choices[0].message.content.strip()
                if "```json" in content:
                    content = content.split("```json")[1].split("```")[0].strip()
                return json.loads(content)
            except Exception as e:
                print(f"⚠️ 청크 분할 실패 {attempt+1}회: {e}")
                time.sleep(1)
        return []
    
    def extract_emotion_situation(self, text: str, max_retries: int = 3) -> Tuple[Optional[str], Optional[str]]:
        """감정과 상황 추출"""
        system_prompt = """당신은 심리 분석에 능숙한 AI입니다.

다음은 사용자 일기에서 분리된 한 개의 청크(문장 묶음)입니다.  
이 청크의 내용 전체를 이해하고, 다음 조건에 따라 **주된 감정 1개와 상황 1개를 추출**하세요.

✅ 조건:
1. 감정과 상황은 각각 **정확히 1개**만 추출합니다.
2. 감정은 사용자의 심리 상태, 정서, 반응 (예: 외로움, 뿌듯함, 분노 등)
3. 상황은 사용자의 행동, 환경, 맥락 (예: 발표, 친구와 대화 등)
4. 추상적 단어나 복합 감정은 피하세요.
5. 반드시 JSON 형식으로만 출력하세요. 그 외 설명은 절대 하지 마세요.

📦 출력 형식 (형식을 반드시 지킬 것):

```json
{
  "감정": "여기에 감정 1개",
  "상황": "여기에 상황 1개"
}
```"""
        
        for attempt in range(max_retries):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": text}
                    ],
                    temperature=0.3
                )
                content = response.choices[0].message.content.strip()
                
                if "```json" in content:
                    content = content.split("```json")[1].split("```")[0].strip()
                
                result = json.loads(content)
                return result.get("감정"), result.get("상황")
            except Exception as e:
                print(f"⚠️ 감정/상황 추출 실패 {attempt+1}회: {e}")
                time.sleep(1)
        
        return None, None
    
    def map_to_categories(self, emotion: str, situation: str, max_retries: int = 3) -> Tuple[Optional[str], Optional[str]]:
        """감정과 상황을 카테고리로 매핑"""
        prompt = f"""
다음은 LLM이 추출한 감정과 상황입니다:
- 감정: "{emotion}"
- 상황: "{situation}"

이 감정과 상황을 아래 사전 정의된 카테고리 중 가장 유사한 항목으로 각각 매핑해주세요.  
정확히 일치하지 않아도 의미상 가장 가까운 항목 하나를 선택하세요.  
카테고리 외의 값을 출력하지 마세요.

📌 감정 카테고리 목록:
["긍정적 감정", "부정적 감정", "두려움과 공포", "불안과 긴장", "수치와 자책", "소외와 상실", "그리움과 아쉬움", "동기와 욕구", "사회적 관계 감정", "이완과 침체", "혼란과 의심", "경이와 압도"]

📌 상황 카테고리 목록:
["일상 및 여가", "인간관계", "업무 및 학습", "건강 및 의료", "디지털 및 온라인 활동", "내면 활동 및 감정", "경제 및 소비생활", "특별한 날과 사건", "창작과 성장"]

📦 출력 형식:
```json
{{
  "감정카테고리": "여기에 감정 카테고리",
  "상황카테고리": "여기에 상황 카테고리"
}}
```"""
        
        for attempt in range(max_retries):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "너는 감정과 상황을 정확히 사전 카테고리에 매핑하는 AI야. 반드시 JSON 형식으로 출력해. 감정카테고리와 상황카테고리라는 정확한 key를 사용해."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.0
                )
                content = response.choices[0].message.content.strip()
                
                if "```json" in content:
                    content = content.split("```json")[1].split("```")[0].strip()
                
                result = json.loads(content)
                return result.get("감정카테고리"), result.get("상황카테고리")
            except Exception as e:
                print(f"⚠️ 카테고리 매핑 실패 {attempt+1}회: {e}")
                time.sleep(1)
        
        return None, None
    
    def calculate_cosine_similarity_torch(self, embedding1, embedding2) -> float:
        """torch를 사용한 코사인 유사도 계산"""
        if isinstance(embedding1, list):
            embedding1 = np.array(embedding1)
        if isinstance(embedding2, list):
            embedding2 = np.array(embedding2)
        
        vec1 = torch.tensor(embedding1, dtype=torch.float32)
        vec2 = torch.tensor(embedding2, dtype=torch.float32)
        
        cosine_sim = F.cosine_similarity(vec1.unsqueeze(0), vec2.unsqueeze(0), dim=1)
        return cosine_sim.item()
    
    def find_similar_past_diaries(self, current_embedding: List[float], user_id: str) -> List[str]:
        """유사한 과거 일기 검색"""
        today = datetime.now().strftime('%Y.%m.%d')
        similar_diaries = []
        
        try:
            similar_results = self.pre_diary_col.query(
                query_embeddings=[current_embedding],
                where={
                    "$and": [
                        {"user_id": user_id},
                        {"date": {"$ne": today}}
                    ]
                },
                n_results=3,
                include=['documents', 'embeddings']
            )
            
            if similar_results['documents'] and similar_results['documents'][0]:
                for doc, doc_embedding in zip(similar_results['documents'][0], similar_results['embeddings'][0]):
                    similarity = self.calculate_cosine_similarity_torch(current_embedding, doc_embedding)
                    if similarity >= 0.7:
                        similar_diaries.append(doc)
        except Exception as e:
            print(f"⚠️ 과거 일기 검색 중 오류 발생: {e}")
        
        return similar_diaries
    
    def find_relevant_advice(self, current_embedding: List[float], emotion_category: str, situation_category: str) -> List[str]:
        """관련 조언 검색"""
        advice_list = []
        
        try:
            advice_results = self.advice_col.query(
                query_embeddings=[current_embedding],
                where={
                    "$and": [
                        {"emotion": emotion_category},
                        {"situation": situation_category}
                    ]
                },
                n_results=2,
                include=["documents", "embeddings"]
            )
            
            if advice_results.get("documents") and advice_results["documents"][0]:
                for doc, doc_embedding in zip(advice_results["documents"][0], advice_results["embeddings"][0]):
                    similarity = self.calculate_cosine_similarity_torch(current_embedding, doc_embedding)
                    if similarity >= 0.7 and doc:
                        advice_list.append(doc)
        except Exception as e:
            print(f"⚠️ 조언 검색 중 오류 발생: {e}")
        
        return advice_list
    
    def generate_final_advice(self, advice_list: List[str]) -> Optional[str]:
        """조언 통합 및 최종 조언 생성"""
        if not advice_list:
            return None
        
        advice_prompt = f"""
다음은 사용자가 작성한 일기의 각 청크에서 추출된 조언들입니다.

이 조언들은 상황에 따라 중복되거나 유사한 내용을 담고 있을 수 있습니다.
이 조언들을 종합해서, 전체 흐름을 고려한 **핵심적인 하나의 조언 문장**으로 정리해주세요.

조건:
- 너무 길게 쓰지 말고, 한 문장 또는 두 문장 이내로 간결하게 작성해주세요.
- 말투는 따뜻하고 부드럽게 해주세요.
- 반복되거나 불필요한 내용은 정리해서 하나로 통합해 주세요.

---

조언 리스트:
{chr(10).join(f"- {a}" for a in advice_list)}

---

# 출력 형식:
```text
하나의 통합 조언 문장
```
"""
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "너는 심리 상담 전문가야. 여러 조언을 하나로 따뜻하게 통합해줘."},
                    {"role": "user", "content": advice_prompt}
                ],
                temperature=0.4
            )
            advice = response.choices[0].message.content.strip().strip("```text").strip("```").strip()
            return advice
        except Exception as e:
            print(f"❌ 통합 조언 생성 실패: {e}")
            return None
    
    def find_relevant_quote(self, advice: str) -> Optional[str]:
        """관련 인용문 검색"""
        if not advice:
            return None
        
        try:
            advice_emb = self.general_embedding_function([advice])[0]
            quote_results = self.quote_col.query(
                query_embeddings=[advice_emb], 
                n_results=3, 
                include=["documents", "distances", "metadatas"]
            )
            
            best_quote = None
            best_similarity = -1
            
            for doc, dist, meta in zip(
                quote_results.get("documents", [[]])[0],
                quote_results.get("distances", [[]])[0],
                quote_results.get("metadatas", [[]])[0]
            ):
                cosine_similarity = 1 - dist
                msg = meta.get("message", doc)
                author = meta.get("author", "")
                
                if cosine_similarity > best_similarity and cosine_similarity >= 0.65:
                    if author:
                        quote_str = f'"{msg}" - {author}'
                    else:
                        quote_str = f'"{msg}"'
                    best_quote = quote_str
            
            return best_quote
        except Exception as e:
            print(f"⚠️ 인용문 검색 중 오류 발생: {e}")
            return None
    
    def generate_comment(self, current_diary: str, advice: str, similar_past_diaries: List[str], quote: Optional[str]) -> str:
        """AI 코멘트 생성"""
        generator = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, n=3)
        
        system_prompt = "당신은 사용자의 감정을 진심으로 이해하고 위로해주는 따뜻한 선생님입니다."
        
        if quote:
            human_prompt = f"""아래 내용을 바탕으로 진심 어린 공감과 격려의 코멘트를 작성해주세요.

일기:
{current_diary}

조언:
{advice}

{f'\n과거 유사 일기 기록:\n{similar_past_diaries}' if similar_past_diaries else ''}
{f'\n관련 인용문:\n{quote}'}

요구사항:
- 코멘트는 3~4문장으로 하나의 문단을 이루어야 합니다.
- 반드시 조언 내용을 참고하되, 코멘트에 '조언에 따라', '조언을 참고하여' 등 조언을 직접적으로 언급하지 마세요.
- 과거 일기 기록이 있는 경우 해당 내용을 구체적으로 언급해주세요.
- 관련 인용문을 따옴표("")로 감싸고 저자와 함께 표시해주세요.
- 따뜻하고 공감 어린 말투를 유지해주세요."""
        else:
            human_prompt = f"""아래 내용을 바탕으로 진심 어린 공감과 격려의 코멘트를 작성해주세요.

일기:
{current_diary}

조언:
{advice}

{f'\n과거 유사 일기 기록:\n{similar_past_diaries}' if similar_past_diaries else ''}

요구사항:
- 코멘트는 3~4문장으로 하나의 문단을 이루어야 합니다.
- 반드시 조언 내용을 참고하되, 코멘트에 '조언에 따라', '조언을 참고하여' 등 조언을 직접적으로 언급하지 마세요.
- 과거 일기 기록이 있는 경우 해당 내용을 구체적으로 언급해주세요.
- 따뜻하고 공감 어린 말투를 유지해주세요."""
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt)
        ]
        
        response = generator.generate([messages])
        comments = [gen.text.strip() for gen in response.generations[0]]
        
        # 최종 코멘트 선택
        selector = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, n=1)
        
        select_system = SystemMessage(content="당신은 공정하고 객관적인 평가자입니다.")
        select_human = HumanMessage(content=f"""위에 생성된 세 개의 코멘트 중에서
"일기의 감정과 상황, 제시된 조언, 과거 유사 일기, 그리고 인용문"을
가장 잘 반영한 한 가지 코멘트를 골라서, 번호와 함께 해당 코멘트만 출력해주세요.

1) {comments[0]}

2) {comments[1]}

3) {comments[2]}""")
        
        selection = selector.invoke([select_system, select_human])
        final_comment = selection.content.strip()
        
        # 번호 제거
        if final_comment and any(final_comment.startswith(f"{i})") for i in range(1, 4)):
            for i in range(1, 4):
                if final_comment.startswith(f"{i})"):
                    final_comment = final_comment[len(f"{i})"):].strip()
                    break
        
        return final_comment
    
    def extract_emotion_keywords(self, chunks: List[str]) -> List[str]:
        """감정 키워드 추출"""
        if not chunks:
            return []
        
        prompt = f"""
다음은 사용자가 작성한 일기의 청크들입니다. 
이 내용에서 나타나는 주요 감정 키워드들을 추출해주세요.

일기 청크들:
{chr(10).join(f"- {chunk}" for chunk in chunks)}

감정 키워드들을 쉼표로 구분하여 출력해주세요. (예: 기쁨, 평온, 대견함, 일상)
"""
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "너는 감정 분석 전문가야. 일기에서 감정 키워드를 추출해줘."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            keywords = response.choices[0].message.content.strip()
            return [kw.strip() for kw in keywords.split(',')]
        except Exception as e:
            print(f"⚠️ 감정 키워드 추출 실패: {e}")
            return []
    
    async def analyze_diary(self, user_id: str, raw_diary: str) -> DiaryAnalysisResponse:
        """일기 분석 및 코멘트 생성 메인 함수"""
        # 1. 일기 전처리
        processed_diary = self.preprocess_diary(raw_diary)
        
        # 2. 의미 단위 청크 분할
        chunks = self.chunk_diary_by_meaning(processed_diary)
        
        # 3. 각 청크별 감정/상황 분석 및 조언 수집
        advice_list = []
        similar_past_diaries = []
        
        for i, chunk in enumerate(chunks):
            # 감정/상황 추출
            emotion, situation = self.extract_emotion_situation(chunk)
            
            if emotion and situation:
                # 카테고리 매핑
                emotion_category, situation_category = self.map_to_categories(emotion, situation)
                
                if emotion_category and situation_category:
                    # 현재 청크 임베딩 생성
                    current_embedding_diary = self.diary_embedding_function([chunk])[0]
                    current_embedding = self.general_embedding_function([chunk])[0]
                    
                    # 유사한 과거 일기 검색
                    similar_diaries = self.find_similar_past_diaries(current_embedding_diary, user_id)
                    similar_past_diaries.extend(similar_diaries)
                    
                    # 일기 저장
                    chunk_id = f"{user_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}"
                    today = datetime.now().strftime('%Y.%m.%d')
                    self.pre_diary_col.add(
                        documents=[chunk],
                        metadatas=[{
                            "user_id": user_id,
                            "date": today,
                            "emotion": emotion_category,
                            "situation": situation_category
                        }],
                        ids=[chunk_id]
                    )
                    
                    # 관련 조언 검색
                    chunk_advice_list = self.find_relevant_advice(current_embedding, emotion_category, situation_category)
                    advice_list.extend(chunk_advice_list)
        
        # 4. 최종 조언 생성
        final_advice = self.generate_final_advice(advice_list)
        
        # 5. 관련 인용문 검색
        quote = self.find_relevant_quote(final_advice) if final_advice else None
        
        # 6. AI 코멘트 생성
        comment = self.generate_comment(processed_diary, final_advice or "", similar_past_diaries, quote)
        
        # 7. 감정 키워드 추출
        emotion_keywords = self.extract_emotion_keywords(chunks)
        
        return DiaryAnalysisResponse(
            processed_diary=processed_diary,
            chunks=chunks,
            advice=final_advice,
            comment=comment,
            quote=quote,
            emotion_keywords=emotion_keywords,
            similar_past_diaries=similar_past_diaries
        ) 