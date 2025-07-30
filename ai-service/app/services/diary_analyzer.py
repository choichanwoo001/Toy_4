import os
import json
import time
from datetime import datetime
from typing import List, Optional, Tuple

import openai
from dotenv import load_dotenv
import chromadb
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
import numpy as np
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

from app.models.diary import DiaryAnalysisResponse, DiaryChunk, EmotionSituationExtraction
from app.prompts.loader import load_prompt

# 환경설정
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class DiaryAnalyzer:
    """일기 분석 및 코멘트 생성 서비스"""
    
    def __init__(self):
        # HuggingFace 모델 로딩 (vector_db.py와 동일한 방식)
        self.tokenizer_diary = AutoTokenizer.from_pretrained("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        self.embedding_model_diary = AutoModel.from_pretrained("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        
        self.tokenizer_general = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        self.embedding_model_general = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        
        # ChromaDB 설정 (임베딩 함수 없이)
        self.client = chromadb.PersistentClient(path="./data/chroma_db")
        self.pre_diary_col = self.client.get_or_create_collection(name="diary_past_diaries")
        self.advice_col = self.client.get_or_create_collection(name="diary_advice")
        self.quote_col = self.client.get_or_create_collection(name="diary_quotes")
    
    def embed_text_diary(self, text: str) -> List[float]:
        """일기 텍스트를 벡터로 변환하는 함수 (Mean Pooling 방식)"""
        try:
            # 1. 텍스트를 토큰으로 변환
            encoded_input = self.tokenizer_diary(text, padding=True, truncation=True, max_length=512, return_tensors='pt')
            
            # 2. AI 모델에 토큰 입력해서 벡터 생성
            with torch.no_grad():
                model_output = self.embedding_model_diary(**encoded_input)
            
            # 3. Mean Pooling 사용 (모든 토큰의 평균)
            attention_mask = encoded_input['attention_mask']
            token_embeddings = model_output.last_hidden_state
            
            # 패딩 토큰 제외하고 평균 계산
            input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
            sentence_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
            
            # 4. 벡터 정규화 (크기를 1로 만듦)
            sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
            
            # 5. PyTorch 텐서를 파이썬 리스트로 변환해서 반환
            return sentence_embeddings.squeeze().cpu().numpy().tolist()
            
        except Exception as e:
            print(f"일기 임베딩 생성 실패: {e}")
            raise
    
    def embed_text_general(self, text: str) -> List[float]:
        """일반 텍스트를 벡터로 변환하는 함수 (Mean Pooling 방식)"""
        try:
            # 1. 텍스트를 토큰으로 변환
            encoded_input = self.tokenizer_general(text, padding=True, truncation=True, max_length=256, return_tensors='pt')
            
            # 2. AI 모델에 토큰 입력해서 벡터 생성
            with torch.no_grad():
                model_output = self.embedding_model_general(**encoded_input)
            
            # 3. Mean Pooling 사용 (모든 토큰의 평균)
            attention_mask = encoded_input['attention_mask']
            token_embeddings = model_output.last_hidden_state
            
            # 패딩 토큰 제외하고 평균 계산
            input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
            sentence_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
            
            # 4. 벡터 정규화 (크기를 1로 만듦)
            sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
            
            # 5. PyTorch 텐서를 파이썬 리스트로 변환해서 반환
            return sentence_embeddings.squeeze().cpu().numpy().tolist()
            
        except Exception as e:
            print(f"일반 임베딩 생성 실패: {e}")
            raise
    
    def preprocess_diary(self, raw_diary: str, max_retries: int = 3) -> str:
        """일기 전처리 - 문법 및 문맥 정리"""
        prompt = load_prompt("diary_preprocess").format(raw_diary=raw_diary)
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
        prompt = load_prompt("diary_chunking").format(diary_text=diary_text)
        for attempt in range(max_retries):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "너는 텍스트를 의미 단위로 나누는 전문 청크 분석기야. 줄바꿈이나 불필요한 공백 없이 깔끔한 JSON만 출력해."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
                content = response.choices[0].message.content.strip()
                if "```json" in content:
                    content = content.split("```json")[1].split("```")[0].strip()
                elif "```" in content:
                    content = content.split("```")[1].split("```")[0].strip()
                
                # 모든 줄바꿈과 공백 정리
                content = content.replace('\n', '').replace('\r', '').replace('  ', ' ').strip()
                
                # JSON 파싱 전에 추가 검증
                if not content.startswith('[') or not content.endswith(']'):
                    print(f"⚠️ 유효하지 않은 JSON 배열 형식: {content}")
                    time.sleep(1)
                    continue
                
                return json.loads(content)
            except json.JSONDecodeError as e:
                print(f"⚠️ JSON 파싱 실패 {attempt+1}회: {e}")
                print(f"📝 문제가 된 내용: {content}")
                # JSON 파싱 실패 시 더 강력한 정리 시도
                try:
                    # 대괄호 안의 내용만 추출
                    start = content.find('[')
                    end = content.rfind(']')
                    if start != -1 and end != -1:
                        content = content[start:end+1]
                        return json.loads(content)
                except:
                    pass
                time.sleep(1)
            except Exception as e:
                print(f"⚠️ 청크 분할 실패 {attempt+1}회: {e}")
                time.sleep(1)
        return []
    
    def extract_emotion_situation(self, text: str, max_retries: int = 3) -> Tuple[Optional[str], Optional[str]]:
        """감정과 상황 추출"""
        system_prompt = load_prompt("emotion_situation_extraction")
        
        for attempt in range(max_retries):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": system_prompt + " 줄바꿈이나 불필요한 공백 없이 깔끔한 JSON만 출력해."},
                        {"role": "user", "content": text}
                    ],
                    temperature=0.3
                )
                content = response.choices[0].message.content.strip()
                
                if "```json" in content:
                    content = content.split("```json")[1].split("```")[0].strip()
                elif "```" in content:
                    content = content.split("```")[1].split("```")[0].strip()
                
                # 모든 줄바꿈과 공백 정리
                content = content.replace('\n', '').replace('\r', '').replace('  ', ' ').strip()
                
                # JSON 파싱 전에 추가 검증
                if not content.startswith('{') or not content.endswith('}'):
                    print(f"⚠️ 유효하지 않은 JSON 형식: {content}")
                    time.sleep(1)
                    continue
                
                result = json.loads(content)
                return result.get("감정"), result.get("상황")
            except json.JSONDecodeError as e:
                print(f"⚠️ JSON 파싱 실패 {attempt+1}회: {e}")
                print(f"📝 문제가 된 내용: {content}")
                # JSON 파싱 실패 시 더 강력한 정리 시도
                try:
                    # 중괄호 안의 내용만 추출
                    start = content.find('{')
                    end = content.rfind('}')
                    if start != -1 and end != -1:
                        content = content[start:end+1]
                        result = json.loads(content)
                        return result.get("감정"), result.get("상황")
                except:
                    pass
                time.sleep(1)
            except Exception as e:
                print(f"⚠️ 감정/상황 추출 실패 {attempt+1}회: {e}")
                time.sleep(1)
        
        return None, None
    
    def map_to_categories(self, emotion: str, situation: str, max_retries: int = 3) -> Tuple[Optional[str], Optional[str]]:
        """감정과 상황을 카테고리로 매핑"""
        prompt = load_prompt("category_mapping").format(emotion=emotion, situation=situation)
        
        for attempt in range(max_retries):
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "너는 감정과 상황을 정확히 사전 카테고리에 매핑하는 AI야. 반드시 JSON 형식으로 출력해. 감정카테고리와 상황카테고리라는 정확한 key를 사용해. 줄바꿈이나 불필요한 공백 없이 깔끔한 JSON만 출력해."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.0
                )
                content = response.choices[0].message.content.strip()
                
                # JSON 코드 블록 제거
                if "```json" in content:
                    content = content.split("```json")[1].split("```")[0].strip()
                elif "```" in content:
                    content = content.split("```")[1].split("```")[0].strip()
                
                # 모든 줄바꿈과 공백 정리
                content = content.replace('\n', '').replace('\r', '').replace('  ', ' ').strip()
                
                # 디버깅을 위한 로그 추가
                print(f"       🔍 GPT 응답 원본: {content}")
                
                # JSON 파싱 전에 추가 검증
                if not content.startswith('{') or not content.endswith('}'):
                    print(f"       ❌ 유효하지 않은 JSON 형식: {content}")
                    time.sleep(1)
                    continue
                
                result = json.loads(content)
                emotion_category = result.get("감정카테고리")
                situation_category = result.get("상황카테고리")
                
                print(f"       ✅ 파싱 성공 - 감정: {emotion_category}, 상황: {situation_category}")
                return emotion_category, situation_category
                
            except json.JSONDecodeError as e:
                print(f"       ❌ JSON 파싱 실패 {attempt+1}회: {e}")
                print(f"       📝 문제가 된 내용: {content}")
                # JSON 파싱 실패 시 더 강력한 정리 시도
                try:
                    # 중괄호 안의 내용만 추출
                    start = content.find('{')
                    end = content.rfind('}')
                    if start != -1 and end != -1:
                        content = content[start:end+1]
                        result = json.loads(content)
                        emotion_category = result.get("감정카테고리")
                        situation_category = result.get("상황카테고리")
                        print(f"       ✅ 재시도 파싱 성공 - 감정: {emotion_category}, 상황: {situation_category}")
                        return emotion_category, situation_category
                except:
                    pass
                time.sleep(1)
            except Exception as e:
                print(f"       ⚠️ 카테고리 매핑 실패 {attempt+1}회: {e}")
                time.sleep(1)
        
        print(f"       ❌ 최대 재시도 횟수 초과")
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
            print(f"       🔍 과거 일기 검색 (사용자: {user_id}, 제외 날짜: {today})")
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
                print(f"       📊 검색된 후보: {len(similar_results['documents'][0])}개")
                for i, (doc, doc_embedding) in enumerate(zip(similar_results['documents'][0], similar_results['embeddings'][0])):
                    similarity = self.calculate_cosine_similarity_torch(current_embedding, doc_embedding)
                    print(f"         후보 {i+1} 유사도: {similarity:.3f}")
                    if similarity >= 0.7:
                        similar_diaries.append(doc)
                        print(f"         ✅ 유사도 {similarity:.3f}로 선택됨")
                    else:
                        print(f"         ❌ 유사도 {similarity:.3f}로 제외됨")
                print(f"       📝 최종 선택된 과거 일기: {len(similar_diaries)}개")
            else:
                print(f"       ⚠️ 사용자 과거 일기 없음")
        except Exception as e:
            print(f"       ❌ 과거 일기 검색 중 오류 발생: {e}")
        
        return similar_diaries
    
    def find_relevant_advice(self, current_embedding: List[float], emotion_category: str, situation_category: str) -> List[str]:
        """관련 조언 검색"""
        advice_list = []
        
        try:
            print(f"       💡 조언 검색 (감정: {emotion_category}, 상황: {situation_category})")
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
                print(f"       📊 검색된 조언 후보: {len(advice_results['documents'][0])}개")
                for i, (doc, doc_embedding) in enumerate(zip(advice_results["documents"][0], advice_results["embeddings"][0])):
                    similarity = self.calculate_cosine_similarity_torch(current_embedding, doc_embedding)
                    print(f"         조언 {i+1} 유사도: {similarity:.3f}")
                    if similarity >= 0.7 and doc:
                        advice_list.append(doc)
                        print(f"         ✅ 유사도 {similarity:.3f}로 선택됨")
                    else:
                        print(f"         ❌ 유사도 {similarity:.3f}로 제외됨")
                print(f"       📝 최종 선택된 조언: {len(advice_list)}개")
            else:
                print(f"       ⚠️ 필터 조건에 맞는 조언 없음")
        except Exception as e:
            print(f"       ❌ 조언 검색 중 오류 발생: {e}")
        
        return advice_list
    
    def generate_final_advice(self, advice_list: List[str]) -> Optional[str]:
        """조언 통합 및 최종 조언 생성"""
        if not advice_list:
            print("       ⚠️ 통합할 조언이 없음")
            return None
        
        print(f"       🔄 {len(advice_list)}개 조언 통합 시작")
        advice_list_formatted = "\n".join(f"- {a}" for a in advice_list)
        advice_prompt = load_prompt("advice_integration").format(advice_list_formatted=advice_list_formatted)
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
            print(f"       ✅ 통합 조언 생성 완료")
            return advice
        except Exception as e:
            print(f"       ❌ 통합 조언 생성 실패: {e}")
            return None
    
    def find_relevant_quote(self, advice: str) -> Optional[str]:
        """관련 인용문 검색"""
        if not advice:
            print("       ⚠️ 조언이 없어서 명언 검색 불가")
            return None
        
        try:
            print(f"       💬 명언 검색 시작")
            advice_emb = self.embed_text_general(advice)
            quote_results = self.quote_col.query(
                query_embeddings=[advice_emb], 
                n_results=3, 
                include=["documents", "distances", "metadatas"]
            )
            
            print(f"       📊 검색된 명언 후보: {len(quote_results.get('documents', [[]])[0])}개")
            best_quote = None
            best_similarity = -1
            
            for i, (doc, dist, meta) in enumerate(zip(
                quote_results.get("documents", [[]])[0],
                quote_results.get("distances", [[]])[0],
                quote_results.get("metadatas", [[]])[0]
            )):
                cosine_similarity = 1 - dist
                msg = meta.get("message", doc)
                author = meta.get("author", "")
                
                print(f"         명언 {i+1} 유사도: {cosine_similarity:.3f}")
                if cosine_similarity > best_similarity and cosine_similarity >= 0.65:
                    if author:
                        quote_str = f'"{msg}" - {author}'
                    else:
                        quote_str = f'"{msg}"'
                    best_quote = quote_str
                    best_similarity = cosine_similarity
                    print(f"         ✅ 유사도 {cosine_similarity:.3f}로 선택됨")
                else:
                    print(f"         ❌ 유사도 {cosine_similarity:.3f}로 제외됨")
            
            if best_quote:
                print(f"       📝 최종 선택된 명언: {best_quote[:50]}...")
            else:
                print(f"       ⚠️ 적절한 명언 없음")
            
            return best_quote
        except Exception as e:
            print(f"       ❌ 명언 검색 중 오류 발생: {e}")
            return None
    
    def generate_comment(self, current_diary: str, advice: str, similar_past_diaries: List[str], quote: Optional[str]) -> str:
        """AI 코멘트 생성"""
        print(f"       🤖 AI 코멘트 생성 시작")
        print(f"         일기 길이: {len(current_diary)}자")
        print(f"         조언: {advice[:50]}..." if advice else "         조언: 없음")
        print(f"         과거 일기: {len(similar_past_diaries)}개")
        print(f"         명언: {quote[:50] if quote else '없음'}...")
        
        generator = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, n=3)
        
        system_prompt = "당신은 사용자의 감정을 진심으로 이해하고 위로해주는 따뜻한 선생님입니다."
        
        if quote:
            similar_past_diaries_section = f'\n과거 유사 일기 기록:\n{similar_past_diaries}' if similar_past_diaries else ''
            quote_section = f'\n관련 인용문:\n{quote}'
            human_prompt = load_prompt("comment_generation").format(
                current_diary=current_diary,
                advice=advice,
                similar_past_diaries_section=similar_past_diaries_section,
                quote_section=quote_section
            )
        else:
            similar_past_diaries_section = f'\n과거 유사 일기 기록:\n{similar_past_diaries}' if similar_past_diaries else ''
            human_prompt = load_prompt("comment_generation_no_quote").format(
                current_diary=current_diary,
                advice=advice,
                similar_past_diaries_section=similar_past_diaries_section
            )
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt)
        ]
        
        print(f"         🔄 3개 코멘트 생성 중...")
        response = generator.generate([messages])
        comments = [gen.text.strip() for gen in response.generations[0]]
        
        print(f"         📝 생성된 코멘트들:")
        for i, comment in enumerate(comments, 1):
            print(f"           {i}. {comment[:100]}...")
        
        # 최종 코멘트 선택
        print(f"         🎯 최종 코멘트 선택 중...")
        selector = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, n=1)
        
        select_system = SystemMessage(content="당신은 공정하고 객관적인 평가자입니다.")
        select_human = HumanMessage(content=load_prompt("comment_selection").format(
            comment1=comments[0],
            comment2=comments[1],
            comment3=comments[2]
        ))
        
        selection = selector.invoke([select_system, select_human])
        final_comment = selection.content.strip()
        
        print(f"         📊 선택 결과: {final_comment}")
        
        # 번호 제거
        if final_comment and any(final_comment.startswith(f"{i})") for i in range(1, 4)):
            for i in range(1, 4):
                if final_comment.startswith(f"{i})"):
                    final_comment = final_comment[len(f"{i})"):].strip()
                    print(f"         ✅ 최종 선택된 코멘트: {i}번")
                    break
        
        return final_comment
    
    def extract_emotion_keywords(self, chunks: List[str]) -> List[str]:
        """감정 키워드 추출"""
        if not chunks:
            return []
        
        chunks_formatted = "\n".join(f"- {chunk}" for chunk in chunks)
        prompt = load_prompt("emotion_keywords").format(chunks_formatted=chunks_formatted)
        
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
        print("\n" + "="*80)
        print("📝 일기 분석 시작")
        print("="*80)
        
        # 1. 일기 전처리
        print("\n🔧 1단계: 일기 전처리")
        processed_diary = self.preprocess_diary(raw_diary)
        print(f"   원본 일기 길이: {len(raw_diary)}자")
        print(f"   전처리 후 길이: {len(processed_diary)}자")
        print(f"   전처리된 일기: {processed_diary[:100]}...")
        
        # 2. 의미 단위 청크 분할
        print("\n📄 2단계: 의미 단위 청크 분할")
        chunks = self.chunk_diary_by_meaning(processed_diary)
        print(f"   총 청크 수: {len(chunks)}개")
        for i, chunk in enumerate(chunks, 1):
            print(f"   청크 {i}: {chunk[:80]}...")
        
        # 3. 각 청크별 감정/상황 분석 및 조언 수집
        print("\n🔍 3단계: 청크별 분석")
        advice_list = []
        similar_past_diaries = []
        
        for i, chunk in enumerate(chunks, 1):
            print(f"\n   📖 청크 {i} 분석:")
            print(f"   내용: {chunk[:100]}...")
            
            # 감정/상황 추출
            emotion, situation = self.extract_emotion_situation(chunk)
            print(f"   감정: {emotion}")
            print(f"   상황: {situation}")
            
            if emotion and situation:
                # 카테고리 매핑
                emotion_category, situation_category = self.map_to_categories(emotion, situation)
                print(f"   매핑된 감정 카테고리: {emotion_category}")
                print(f"   매핑된 상황 카테고리: {situation_category}")
                
                if emotion_category and situation_category:
                    # 현재 청크 임베딩 생성
                    current_embedding_diary = self.embed_text_diary(chunk)
                    current_embedding = self.embed_text_general(chunk)
                    print(f"   임베딩 생성 완료 (일기용: {len(current_embedding_diary)}차원, 일반용: {len(current_embedding)}차원)")
                    
                    # 유사한 과거 일기 검색
                    similar_diaries = self.find_similar_past_diaries(current_embedding_diary, user_id)
                    similar_past_diaries.extend(similar_diaries)
                    print(f"   유사한 과거 일기: {len(similar_diaries)}개")
                    for j, diary in enumerate(similar_diaries[:2], 1):  # 상위 2개만 출력
                        print(f"     {j}. {diary[:80]}...")
                    
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
                    print(f"   일기 저장 완료 (ID: {chunk_id})")
                    
                    # 관련 조언 검색
                    chunk_advice_list = self.find_relevant_advice(current_embedding, emotion_category, situation_category)
                    advice_list.extend(chunk_advice_list)
                    print(f"   관련 조언: {len(chunk_advice_list)}개")
                    for j, advice in enumerate(chunk_advice_list[:2], 1):  # 상위 2개만 출력
                        print(f"     {j}. {advice[:80]}...")
                else:
                    print("   ❌ 카테고리 매핑 실패")
            else:
                print("   ❌ 감정/상황 추출 실패")
        
        # 4. 최종 조언 생성
        print(f"\n💡 4단계: 최종 조언 생성")
        print(f"   수집된 조언 수: {len(advice_list)}개")
        print("   조언 리스트:")
        for i, advice in enumerate(advice_list, 1):
            print(f"     {i}. {advice}")
        
        final_advice = self.generate_final_advice(advice_list)
        print(f"   최종 통합 조언: {final_advice}")
        
        # 5. 관련 인용문 검색
        print(f"\n💬 5단계: 관련 명언 검색")
        quote = self.find_relevant_quote(final_advice) if final_advice else None
        print(f"   찾은 명언: {quote}")
        
        # 6. AI 코멘트 생성
        print(f"\n🤖 6단계: AI 코멘트 생성")
        comment = self.generate_comment(processed_diary, final_advice or "", similar_past_diaries, quote)
        print(f"   생성된 코멘트: {comment[:200]}...")
        
        # 7. 감정 키워드 추출
        print(f"\n🎭 7단계: 감정 키워드 추출")
        emotion_keywords = self.extract_emotion_keywords(chunks)
        print(f"   추출된 감정 키워드: {emotion_keywords}")
        
        print("\n" + "="*80)
        print("✅ 일기 분석 완료")
        print("="*80)
        
        return DiaryAnalysisResponse(
            processed_diary=processed_diary,
            chunks=chunks,
            advice=final_advice,
            comment=comment,
            quote=quote,
            emotion_keywords=emotion_keywords,
            similar_past_diaries=similar_past_diaries
        ) 