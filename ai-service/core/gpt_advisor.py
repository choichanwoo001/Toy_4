"""
GPT 기반 조언 생성 모듈
검색된 유사 조언들을 바탕으로 개인화된 조언을 생성
"""

from openai import OpenAI
from typing import List, Dict, Any
import logging
from config.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GPTAdvisor:
    def __init__(self):
        """GPT 조언자 초기화"""
        self.config = Config()
        self.client = None
        self.initialize()
    
    def initialize(self):
        """OpenAI 클라이언트 초기화"""
        try:
            if not self.config.OPENAI_API_KEY:
                raise ValueError("OpenAI API 키가 설정되지 않았습니다. .env 파일을 확인해주세요.")
            
            self.client = OpenAI(
                api_key=self.config.OPENAI_API_KEY
            )
            logger.info("OpenAI 클라이언트 초기화 완료")
            
        except Exception as e:
            logger.error(f"OpenAI 클라이언트 초기화 실패: {e}")
            raise
    
    def format_retrieved_advice(self, search_results: Dict[str, Any]) -> str:
        """검색된 조언들을 포맷팅"""
        try:
            documents = search_results.get('documents', [[]])[0]
            metadatas = search_results.get('metadatas', [[]])[0]
            distances = search_results.get('distances', [[]])[0]
            
            if not documents:
                return "유사한 조언을 찾을 수 없습니다."
            
            logger.info(f"조언 검색 결과: {len(documents)}개")
            
            formatted_advice = []
            for i, (doc, meta, distance) in enumerate(zip(documents, metadatas, distances), 1):
                category = meta.get("category", "일반")
                emotion_type = meta.get("emotion_type", "")
                advice_type = meta.get("advice_type", "")
                
                # 유사도를 백분율로 변환 (거리가 작을수록 유사도가 높음)
                similarity = (1 - distance) * 100
                
                formatted_advice.append(
                    f"[조언 {i}] ({category} - {emotion_type}) [유사도: {similarity:.1f}%]\n"
                    f"{doc}\n"
                    f"(조언 유형: {advice_type})\n"
                )
                
                logger.info(f"조언 {i}: 유사도 {similarity:.1f}% - {doc[:30]}...")
            
            logger.info(f"조언 포맷팅 완료: {len(formatted_advice)}개")
            return "\n".join(formatted_advice)
            
        except Exception as e:
            logger.error(f"조언 포맷팅 실패: {e}")
            return "조언 포맷팅 중 오류가 발생했습니다."
    
    def create_prompt(self, user_diary: str, retrieved_advice: str, quotes_hint: str = "", past_diaries_hint: str = "") -> str:
        """GPT 프롬프트 생성"""
        return f"""[사용자 일기]
{user_diary}

[참고 정보]
- 유사 조언: {retrieved_advice}
- 관련 명언: {quotes_hint}
- 과거 일기: {past_diaries_hint}"""
    
    def generate_advice(self, user_diary: str, search_results: Dict[str, Any]) -> str:
        """일기를 바탕으로 개인화된 조언 생성"""
        try:
            # 검색된 조언들 포맷팅
            retrieved_advice = self.format_retrieved_advice(search_results)
            
            # 유사한 명언 검색
            from core.vector_db import VectorDatabase
            vector_db = VectorDatabase()
            similar_quotes = vector_db.search_similar_quotes(user_diary)
            
            # 명언 힌트 포맷팅
            quotes_hint = ""
            if similar_quotes['documents'][0]:
                quotes_list = []
                logger.info(f"명언 검색 결과: {len(similar_quotes['documents'][0])}개")
                
                for i, (quote, metadata, distance) in enumerate(zip(
                    similar_quotes['documents'][0], 
                    similar_quotes['metadatas'][0], 
                    similar_quotes['distances'][0]
                )):
                    author = metadata.get('author', '알 수 없음')
                    # 유사도를 백분율로 변환 (거리가 작을수록 유사도가 높음)
                    similarity = (1 - distance) * 100
                    quotes_list.append(f"- {quote} ({author}) [유사도: {similarity:.1f}%]")
                    logger.info(f"명언 {i+1}: 유사도 {similarity:.1f}% - {quote[:30]}...")
                
                quotes_hint = "\n".join(quotes_list)
                logger.info(f"명언 힌트 생성 완료: {len(quotes_list)}개")
            else:
                logger.info("명언 검색 결과가 없습니다.")
            
            # 유사한 과거 일기 검색
            similar_past_diaries = vector_db.search_similar_past_diaries(user_diary)
            
            # 과거 일기 힌트 포맷팅
            past_diaries_hint = ""
            if similar_past_diaries['documents'][0]:
                diaries_list = []
                logger.info(f"과거 일기 검색 결과: {len(similar_past_diaries['documents'][0])}개")
                
                for i, (diary, metadata, distance) in enumerate(zip(
                    similar_past_diaries['documents'][0], 
                    similar_past_diaries['metadatas'][0], 
                    similar_past_diaries['distances'][0]
                )):
                    date = metadata.get('date', '날짜 없음')
                    emotion = metadata.get('emotion', '감정 없음')
                    # 유사도를 백분율로 변환 (거리가 작을수록 유사도가 높음)
                    similarity = (1 - distance) * 100
                    diaries_list.append(f"- {diary} (날짜: {date}, 감정: {emotion}) [유사도: {similarity:.1f}%]")
                    logger.info(f"과거 일기 {i+1}: 유사도 {similarity:.1f}% - {diary[:30]}...")
                
                past_diaries_hint = "\n".join(diaries_list)
                logger.info(f"과거 일기 힌트 생성 완료: {len(diaries_list)}개")
            else:
                logger.info("과거 일기 검색 결과가 없습니다.")
            
            # 프롬프트 생성
            prompt = self.create_prompt(user_diary, retrieved_advice, quotes_hint, past_diaries_hint)
            
            # GPT API 호출
            response = self.client.chat.completions.create(
                model=self.config.GPT_MODEL,
                messages=[
                    {"role": "system", "content": """당신은 따뜻하고 공감능력이 뛰어난 심리상담사입니다.
사용자의 일기를 읽고, 주어진 '조언 생성 원칙'에 따라 종합적인 조언을 제공해주세요.

[조언 생성 원칙]
1. 감정 공감: 사용자의 감정을 충분히 이해하고 공감해주세요.
2. 현실적 조언: 실현 가능하고 구체적인 해결 방안을 제시해주세요.
3. 위로와 격려: 따뜻한 위로와 희망적인 메시지를 포함해주세요.
4. 성장 관점: 이 경험을 통해 성장할 수 있는 방향을 제시해주세요.
5. 가독성: 문단과 문장을 나누어 가독성 좋게 작성해주세요.

**[분기별 지침]**
*   **만약 '참고 정보'가 제공되면 (RAG 방식):**
    *   **6. RAG 활용:** 제공된 '참고 정보'(유사 조언, 명언, 과거 일기)를 적극적으로 활용하여, "과거에도 비슷한 감정을 느끼셨군요" 또는 "이런 명언이 있듯이..." 와 같이 자연스럽게 내용을 연결하며 조언해주세요.
*   **만약 '참고 정보'가 없다면 (프롬프트 방식):**
    *   **6. 자율성:** 참고 정보 없이, 당신의 전문 지식과 분석력을 바탕으로 자율적으로 조언을 생성해주세요.
    *   **7. 명언 생성:** 일기 내용에 어울리는 명언을 직접 생성하거나 떠올려 조언에 포함시켜주세요.

[출력 형식]
- 조언은 한국어로 자연스럽고 따뜻한 말투로 작성해주세요.
- 전체 길이는 2~4개의 완결된 문장으로 간결하게 구성해주세요. 절대 중간에 끊기면 안 됩니다."""},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.config.MAX_TOKENS,
                temperature=self.config.TEMPERATURE
            )
            
            advice = response.choices[0].message.content.strip()
            logger.info("조언 생성 완료")
            
            return advice
            
        except Exception as e:
            logger.error(f"조언 생성 실패: {e}")
            return f"죄송합니다. 조언을 생성하는 중에 오류가 발생했습니다: {str(e)}"
    
    def generate_simple_advice(self, user_diary: str) -> str:
        """검색 결과 없이 단순 조언 생성 (fallback)"""
        try:
            prompt = f"""[사용자 일기]
{user_diary}"""

            response = self.client.chat.completions.create(
                model=self.config.GPT_MODEL,
                messages=[
                    {"role": "system", "content": """당신은 따뜻하고 공감능력이 뛰어난 심리상담사입니다.
사용자의 일기를 읽고, 주어진 '조언 생성 원칙'에 따라 종합적인 조언을 제공해주세요.

[조언 생성 원칙]
1. 감정 공감: 사용자의 감정을 충분히 이해하고 공감해주세요.
2. 현실적 조언: 실현 가능하고 구체적인 해결 방안을 제시해주세요.
3. 위로와 격려: 따뜻한 위로와 희망적인 메시지를 포함해주세요.
4. 성장 관점: 이 경험을 통해 성장할 수 있는 방향을 제시해주세요.
5. 가독성: 문단과 문장을 나누어 가독성 좋게 작성해주세요.

**[분기별 지침]**
*   **만약 '참고 정보'가 제공되면 (RAG 방식):**
    *   **6. RAG 활용:** 제공된 '참고 정보'(유사 조언, 명언, 과거 일기)를 적극적으로 활용하여, "과거에도 비슷한 감정을 느끼셨군요" 또는 "이런 명언이 있듯이..." 와 같이 자연스럽게 내용을 연결하며 조언해주세요.
*   **만약 '참고 정보'가 없다면 (프롬프트 방식):**
    *   **6. 자율성:** 참고 정보 없이, 당신의 전문 지식과 분석력을 바탕으로 자율적으로 조언을 생성해주세요.
    *   **7. 명언 생성:** 일기 내용에 어울리는 명언을 직접 생성하거나 떠올려 조언에 포함시켜주세요.

[출력 형식]
- 조언은 한국어로 자연스럽고 따뜻한 말투로 작성해주세요.
- 전체 길이는 2~4개의 완결된 문장으로 간결하게 구성해주세요. 절대 중간에 끊기면 안 됩니다."""},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.config.MAX_TOKENS,
                temperature=self.config.TEMPERATURE
            )
            
            advice = response.choices[0].message.content.strip()
            logger.info("단순 조언 생성 완료")
            
            return advice
            
        except Exception as e:
            logger.error(f"단순 조언 생성 실패: {e}")
            return "죄송합니다. 현재 조언 서비스에 문제가 있습니다. 잠시 후 다시 시도해주세요." 