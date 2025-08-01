"""
에이전트 기반 챗봇 서비스

MainAgent를 사용하여 자율적 의사결정과 동적 전략 수립을 통해
사용자 입력에 대한 적절한 응답을 생성하는 서비스입니다.
"""
import logging
from typing import Dict, Any

from chatbot.main_agent import MainAgent

logger = logging.getLogger(__name__)


class AgentService:
    """
    MainAgent를 사용하는 챗봇 서비스 클래스.
    
    기존 ChatbotService의 기능을 MainAgent로 대체하여
    더 자율적이고 지능적인 응답을 제공합니다.
    """
    
    def __init__(self, user_id: str):
        """
        AgentService 인스턴스를 초기화합니다.
        
        Args:
            user_id (str): 사용자 식별자
        """
        self.user_id = user_id
        self.agent = MainAgent(user_id)
        self.is_initialized = False
    
    def initialize(self):
        """
        에이전트 서비스를 초기화합니다.
        """
        try:
            logger.info(f"AgentService for user '{self.user_id}' initializing...")
            self.agent.initialize()
            self.is_initialized = True
            logger.info(f"✅ AgentService for user '{self.user_id}' initialized.")
        except Exception as e:
            logger.error(f"❌ AgentService initialization failed: {e}")
            self.is_initialized = False
            raise
    
    def get_response(self, user_input: str) -> Dict[str, Any]:
        """
        사용자 입력에 대한 응답을 생성합니다.
        
        Args:
            user_input (str): 사용자 입력 메시지
            
        Returns:
            Dict[str, Any]: 응답 결과
                - success (bool): 성공 여부
                - response (str): 생성된 응답
                - rag_info (Dict): RAG 검색 정보 (있는 경우)
        """
        if not self.is_initialized:
            logger.warning("초기화 전에 응답을 요청했습니다.")
            return {"success": False, "response": "에이전트 서비스가 초기화되지 않았습니다."}
        
        try:
            logger.info(f"사용자 입력 처리 시작: '{user_input[:50]}...'")
            
            # MainAgent를 통해 응답 생성
            result = self.agent.get_response(user_input)
            
            # RAG 정보가 있으면 추가
            if hasattr(self.agent, 'last_rag_info') and self.agent.last_rag_info:
                result['rag_info'] = self.agent.last_rag_info
            
            logger.info(f"응답 생성 완료: 성공={result['success']}")
            return result
            
        except Exception as e:
            logger.error(f"❌ 에이전트 서비스 응답 생성 실패: {e}", exc_info=True)
            return {"success": False, "response": "죄송합니다. 답변을 생성하는 동안 오류가 발생했습니다."}
    
    def end_conversation(self) -> Dict[str, Any]:
        """
        현재 사용자와의 대화를 종료하고 요약을 제공합니다.
        
        Returns:
            Dict[str, Any]: 대화 종료 결과
                - success (bool): 성공 여부
                - response (str): 대화 요약 또는 종료 메시지
        """
        if not self.is_initialized:
            return {"success": False, "response": "에이전트 서비스가 초기화되지 않았습니다."}
        
        try:
            logger.info(f"대화 종료 처리 시작: user_id={self.user_id}")
            
            result = self.agent.end_conversation()
            
            logger.info(f"대화 종료 완료: 성공={result['success']}")
            return result
            
        except Exception as e:
            logger.error(f"❌ 대화 종료 처리 실패: {e}", exc_info=True)
            return {"success": False, "response": "대화를 마무리하는 중 오류가 발생했습니다."}
    
    def get_agent_state(self) -> Dict[str, Any]:
        """
        현재 에이전트의 상태 정보를 반환합니다.
        
        Returns:
            Dict[str, Any]: 에이전트 상태 정보
        """
        if not self.is_initialized:
            return {"error": "에이전트가 초기화되지 않았습니다."}
        
        state = self.agent.state
        return {
            "user_id": self.user_id,
            "is_initialized": self.is_initialized,
            "complexity_score": state.complexity_score,
            "ambiguity_level": state.ambiguity_level,
            "requires_clarification": state.requires_clarification,
            "intent": state.intent,
            "emotion": state.emotion,
            "situation": state.situation,
            "user_input_length": state.user_input_length
        } 