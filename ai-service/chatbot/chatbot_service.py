"""
챗봇 서비스의 메인 로직을 담당하는 모듈입니다.

이 모듈은 사용자 입력을 받아 의도를 파악하고,
적절한 응답을 생성하는 전체적인 챗봇 파이프라인을 관리합니다.
"""
import logging
import sys
import os
import json
from typing import Dict, Any, Optional, List

# 프로젝트의 다른 모듈을 가져오기 위해 프로젝트 루트 경로를 시스템 경로에 추가합니다.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.vector_db import VectorDatabase
from chatbot.llm_service import LLMService
from chatbot.conversation_manager import ConversationManager
from chatbot.preprocessor import Preprocessor # 새로 추가
from chatbot.prompts.loader import load_prompt
from config.config import Config

# 로깅 설정
logger = logging.getLogger(__name__)


class ConversationManagementAgent:
    """사용자 입력 분석 및 대화 흐름 제어를 담당하는 에이전트"""
    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def classify_intent(self, user_input: str, conversation_history: str) -> Dict[str, Any]:
        """사용자 입력을 바탕으로 의도를 '단순 감정 표현', '복합 사건 서술', '모호함'으로 분류"""
        prompt = load_prompt("intent_classification").format(
            user_input=user_input,
            conversation_history=conversation_history
        )
        response_str = self.llm_service.get_response(prompt)
        try:
            # The entire response is a JSON object.
            return json.loads(response_str)
        except json.JSONDecodeError:
            logger.error(f"의도 분류를 위한 LLM 응답에서 JSON 디코딩 실패: {response_str}")
            # 다른 텍스트가 포함된 문자열에서 JSON을 추출하려고 시도
            try:
                json_part = response_str[response_str.find('{'):response_str.rfind('}')+1]
                return json.loads(json_part)
            except (json.JSONDecodeError, IndexError):
                logger.error(f"의도 분류 응답에서 JSON을 추출할 수 없음: {response_str}")
                return {"intent": "Error", "reason": "LLM 응답 파싱 실패"}


    def analyze_chunk(self, chunk: str) -> Dict[str, Any]:
        """개별 청크의 내용을 요약하고 감정/상황 태그를 추출"""
        prompt = load_prompt("complex_event_analysis").format(user_input=chunk)
        response_str = self.llm_service.get_response(prompt)
        try:
            return json.loads(response_str)
        except json.JSONDecodeError:
            logger.error(f"청크 분석을 위한 LLM 응답에서 JSON 디코딩 실패: {response_str}")
            return {}


class RagAgent:
    """RAG 검색을 담당하는 에이전트"""
    def __init__(self, vector_db: VectorDatabase):
        self.vector_db = vector_db

    def search(self, query: str, n_results: int = 5, similarity_threshold: float = 0.5, emotion_filter: List[str] = None, situation_filter: str = None) -> Optional[str]:
        """Vector DB에서 관련 정보를 검색하고, 기준치 이상의 결과만 반환"""
        logger.info(f"RAG 검색 시작: query='{query}', threshold={similarity_threshold}, emotion_filter='{emotion_filter}', situation_filter='{situation_filter}'")

        # 먼저 샘플 데이터 몇 개를 가져와서 메타데이터 형식 확인
        sample_results = self.vector_db.collection.get(limit=3)
        if sample_results and sample_results.get('metadatas'):
            logger.info(f"샘플 메타데이터 확인: {sample_results['metadatas'][:3]}")

        search_results = self.vector_db.search_similar_advice(
            query, 
            n_results=n_results,
            emotion_filter=emotion_filter,
            situation_filter=situation_filter
        )
        
        if not search_results or not search_results.get("documents"):
            logger.info("RAG 검색 결과 없음.")
            return None

        filtered_advice = []
        similarity_scores = []
        for doc, dist in zip(search_results["documents"][0], search_results["distances"][0]):
            similarity = 1 - dist
            if similarity >= similarity_threshold:
                filtered_advice.append(doc)
                similarity_scores.append(f"{similarity:.3f}")
        
        if not filtered_advice:
            logger.info(f"유사도 {similarity_threshold} 이상인 문서를 찾지 못했습니다.")
            return None
            
        # 유사도 정보와 함께 결과 구성
        rag_data_with_scores = []
        for advice, score in zip(filtered_advice, similarity_scores):
            rag_data_with_scores.append(f"[유사도: {score}] {advice}")
        
        rag_data = "\n- ".join(rag_data_with_scores)
        logger.info(f"RAG 검색 완료. {len(filtered_advice)}개의 관련 문서 발견. 유사도: {similarity_scores}")
        return rag_data


class ResponseGenerationAgent:
    """다양한 시나리오에 맞춰 최종 응답을 생성하는 에이전트"""
    def __init__(self, llm_service: LLMService):
        self.llm_service = llm_service

    def generate_response(self, intent: str, user_input: str, history_str: str, rag_data: Optional[str], chunks_analysis: Optional[str] = None) -> str:
        """분류된 의도와 RAG 데이터 유무에 따라 적절한 프롬프트를 사용하여 응답 생성"""
        prompt = ""
        if intent == "Complex Event" or intent == "복합 사건 서술 (Complex Event)":
            if rag_data:
                logger.info("시나리오: 복합 사건, RAG 데이터 있음")
                prompt = load_prompt("response_with_rag").format(
                    user_input=user_input,
                    rag_data=rag_data,
                    conversation_history=history_str,
                    chunks_analysis=chunks_analysis # 청크 분석 결과 추가
                )
            else:
                logger.info("시나리오: 복합 사건, RAG 데이터 없음")
                prompt = load_prompt("response_without_rag").format(
                    user_input=user_input,
                    conversation_history=history_str
                )
        elif intent == "Simple Emotion" or intent == "단순 감정 표현 (Simple Emotion)":
            logger.info("시나리오: 단순 감정 표현")
            prompt = load_prompt("response_simple_emotion").format(
                user_input=user_input,
                conversation_history=history_str
            )
        elif intent == "Ambiguous" or intent == "모호함 (Ambiguous)":
            logger.info("시나리오: 모호한 입력")
            return "어떤 말씀을 하시는지 더 자세히 설명해주실 수 있나요? 오늘 있었던 일이나 감정에 대해 조금 더 구체적으로 이야기해주시면 제가 더 잘 이해하고 도울 수 있을 것 같아요."
        else:
            logger.warning(f"처리할 수 없는 의도: '{intent}'. 기본 응답을 반환합니다.")
            return "어떤 말씀을 하시는지 이해하기 어려워요. 조금 더 자세히 설명해주실 수 있나요?"

        return self.llm_service.get_response(prompt)


class ChatbotService:
    """
    챗봇의 핵심 로직을 처리하는 서비스 클래스.
    여러 에이전트를 조율하여 챗봇 파이프라인을 실행합니다.
    """
    def __init__(self, user_id: str):
        """ChatbotService 인스턴스를 초기화합니다."""
        self.user_id = user_id
        self.config = Config()
        self.vector_db = VectorDatabase()
        self.llm_service = LLMService()
        self.conversation_manager = ConversationManager()
        self.is_initialized = False
        self.preprocessor = Preprocessor(self.llm_service) # Preprocessor 초기화

        # 에이전트 초기화
        self.management_agent = ConversationManagementAgent(self.llm_service)
        self.rag_agent = RagAgent(self.vector_db)
        self.generation_agent = ResponseGenerationAgent(self.llm_service)

    def initialize(self):
        """챗봇 서비스의 모든 구성 요소를 초기화합니다."""
        try:
            logger.info(f"ChatbotService for user '{self.user_id}' initializing...")
            self.vector_db.initialize()
            self.is_initialized = True
            logger.info(f"✅ ChatbotService for user '{self.user_id}' initialized.")
        except Exception as e:
            logger.error(f"❌ ChatbotService initialization failed: {e}")
            self.is_initialized = False
            raise

    def get_response(self, user_input: str) -> Dict[str, Any]:
        """사용자 입력에 대한 챗봇의 응답을 생성하는 메인 메서드입니다."""
        if not self.is_initialized:
            logger.warning("초기화 전에 응답을 요청했습니다.")
            return {"success": False, "response": "챗봇 서비스가 초기화되지 않았습니다."}

        try:
            # 0. 입력 전처리
            preprocessed_input = self.preprocessor.preprocess_diary(user_input)
            logger.info(f"전처리된 입력: {preprocessed_input}")

            # 1. 대화 기록 가져오기
            conversation_history = self.conversation_manager.get_recent_conversation(self.user_id, count=10) # 최근 10개 대화
            history_str = "\n".join([f"{c['role']}: {c['content']}" for c in conversation_history])

            # 2. 대화 관리 에이전트: 사용자 의도 분류
            intent_result = self.management_agent.classify_intent(preprocessed_input, history_str)
            intent = intent_result.get("intent", "Error")
            logger.info(f"사용자 의도 분류 결과: {intent} (이유: {intent_result.get('reason')})")

            # 3. 의도에 따른 분기 처리
            rag_data = None
            chunks_analysis_summary = None

            if intent == "Complex Event" or intent == "복합 사건 서술 (Complex Event)":
                logger.info("복합 사건으로 분류됨. 전체 입력을 단일 청크로 처리합니다.")
                
                # 전체 입력을 하나의 청크로 처리
                chunk = preprocessed_input
                
                # 청크 분석 (감정/상황 태그 추출)
                chunk_analysis = self.management_agent.analyze_chunk(chunk)
                emotion_tag = chunk_analysis.get("emotion")
                situation_tag = chunk_analysis.get("situation")
                logger.info(f"청크 분석 결과: 감정='{emotion_tag}', 상황='{situation_tag}'")
                
                chunks_analysis_summary = f"- 내용: {chunk}\n  - 감정: {emotion_tag}\n  - 상황: {situation_tag}"

                # RAG 검색
                rag_result = self.rag_agent.search(
                    query=chunk,
                    similarity_threshold=0.5,
                    emotion_filter=[emotion_tag] if emotion_tag else None,
                    situation_filter=situation_tag
                )
                if rag_result:
                    rag_data = rag_result
                    logger.info("RAG 검색 결과를 찾았습니다.")
                else:
                    logger.info("RAG 검색 결과가 없습니다.")


            # 4. 응답 생성 에이전트: 최종 응답 생성
            response = self.generation_agent.generate_response(intent, preprocessed_input, history_str, rag_data, chunks_analysis_summary)

            # 5. 대화 기록 저장
            self.conversation_manager.add_to_conversation(self.user_id, 'user', user_input)
            self.conversation_manager.add_to_conversation(self.user_id, 'assistant', response)

            return {"success": True, "response": response}

        except Exception as e:
            logger.error(f"❌ 챗봇 응답 생성 실패: {e}", exc_info=True)
            return {"success": False, "response": "죄송합니다. 답변을 생성하는 동안 오류가 발생했습니다."}


    def end_conversation(self) -> Dict[str, Any]:
        """현재 사용자와의 대화를 종료하고, 전체 대화 내용을 요약하여 제공합니다."""
        if not self.is_initialized:
            return {"success": False, "response": "챗봇 서비스가 초기화되지 않았습니다."}

        try:
            conversation_history = self.conversation_manager.get_recent_conversation(self.user_id, count=self.conversation_manager.max_history_length)
            
            if not conversation_history:
                return {"success": True, "response": "나중에 또 만나요! 언제든지 다시 찾아주세요."}

            history_str = "\n".join([f"{c['role']}: {c['content']}" for c in reversed(conversation_history)])

            prompt = load_prompt("conversation_summary").format(
                conversation_history=history_str
            )
            summary_response = self.llm_service.get_response(prompt)
            
            self.conversation_manager.clear_conversation_history(self.user_id)

            return {"success": True, "response": summary_response}

        except Exception as e:
            logger.error(f"❌ 대화 종료 처리 실패: {e}", exc_info=True)
            return {"success": False, "response": "대화를 마무리하는 중 오류가 발생했습니다."} 