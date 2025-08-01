"""
MainAgent 클래스에 대한 단위 테스트

이 테스트는 MainAgent의 핵심 기능들을 검증합니다:
- 초기화 및 상태 관리
- 의도 분석 및 전략 수립
- 도구 실행 및 응답 생성
- 대화 관리 및 종료 처리
"""

import pytest
import json
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any, List

from chatbot.main_agent import (
    MainAgent, 
    AgentState, 
    ConversationManagementTool,
    RAGTool,
    ResponseGenerationTool,
    ClarifyTool,
    IntentType,
    StrategyType
)


class TestAgentState:
    """AgentState 클래스 테스트"""
    
    def test_agent_state_initialization(self):
        """AgentState 초기화 테스트"""
        state = AgentState()
        
        assert state.user_input == ""
        assert state.history == []
        assert state.intent is None
        assert state.emotion is None
        assert state.situation is None
        assert state.ambiguity_level == 0.0
        assert state.complexity_score == 0.0
        assert state.requires_clarification is False
        assert state.previous_attempts == []
        assert state.user_input_length == 0
    
    def test_agent_state_update(self):
        """AgentState 업데이트 테스트"""
        state = AgentState()
        user_input = "오늘 정말 힘들었어요"
        history = [{"role": "user", "content": "안녕하세요"}]
        
        state.update(user_input, history)
        
        assert state.user_input == user_input
        assert state.history == history
        assert state.user_input_length == len(user_input)
        assert state.complexity_score > 0
        assert state.ambiguity_level > 0
    
    def test_agent_state_analyze_input_characteristics_short_input(self):
        """짧은 입력에 대한 특성 분석 테스트"""
        state = AgentState()
        state.user_input = "안녕"
        state.analyze_input_characteristics()
        
        assert state.ambiguity_level == 0.8
        assert state.requires_clarification is True
    
    def test_agent_state_analyze_input_characteristics_question(self):
        """질문 입력에 대한 특성 분석 테스트"""
        state = AgentState()
        state.user_input = "어떻게 해야 할까요?"
        state.analyze_input_characteristics()
        
        assert state.ambiguity_level == 0.6
        assert state.requires_clarification is False
    
    def test_agent_state_analyze_input_characteristics_long_input(self):
        """긴 입력에 대한 특성 분석 테스트"""
        state = AgentState()
        state.user_input = "오늘 회사에서 정말 힘든 일이 있었어요. 상사가 저를 무시하는 것 같고, 동료들도 저를 따돌리는 것 같아요. 집에 와서도 계속 그 생각만 하고 있어요."
        state.analyze_input_characteristics()
        
        assert state.ambiguity_level == 0.2
        assert state.complexity_score > 0.5
        assert state.requires_clarification is False
    
    def test_agent_state_update_with_result(self):
        """결과로 상태 업데이트 테스트"""
        state = AgentState()
        result = {
            "intent": "Complex Event",
            "emotion": "슬픔",
            "situation": "직장 문제"
        }
        
        state.update_with_result(result)
        
        assert state.intent == "Complex Event"
        assert state.emotion == "슬픔"
        assert state.situation == "직장 문제"


class TestConversationManagementTool:
    """ConversationManagementTool 클래스 테스트"""
    
    def setup_method(self):
        """테스트 설정"""
        self.mock_llm_service = Mock()
        self.tool = ConversationManagementTool(self.mock_llm_service)
    
    def test_analyze_success(self):
        """성공적인 의도 분석 테스트"""
        # Mock 응답 설정
        mock_response = '{"intent": "Complex Event", "emotion": "슬픔", "situation": "직장 문제"}'
        self.mock_llm_service.get_response.return_value = mock_response
        
        state = AgentState()
        state.user_input = "오늘 정말 힘들었어요"
        state.history = [{"role": "user", "content": "안녕하세요"}]
        
        result = self.tool.analyze(state)
        
        assert result["intent"] == "Complex Event"
        assert result["emotion"] == "슬픔"
        assert result["situation"] == "직장 문제"
        self.mock_llm_service.get_response.assert_called_once()
    
    def test_analyze_json_decode_error(self):
        """JSON 파싱 오류 테스트"""
        # 잘못된 JSON 응답 설정
        self.mock_llm_service.get_response.return_value = "invalid json"
        
        state = AgentState()
        state.user_input = "오늘 정말 힘들었어요"
        
        result = self.tool.analyze(state)
        
        assert result["intent"] == "Error"
        assert "LLM 응답 파싱 실패" in result["reason"]
    
    def test_analyze_chunk_success(self):
        """청크 분석 성공 테스트"""
        mock_response = '{"emotion": "슬픔", "situation": "직장 문제"}'
        self.mock_llm_service.get_response.return_value = mock_response
        
        chunk = "오늘 정말 힘들었어요"
        result = self.tool.analyze_chunk(chunk)
        
        assert result["emotion"] == "슬픔"
        assert result["situation"] == "직장 문제"
    
    def test_analyze_chunk_json_error(self):
        """청크 분석 JSON 오류 테스트"""
        self.mock_llm_service.get_response.return_value = "invalid json"
        
        chunk = "오늘 정말 힘들었어요"
        result = self.tool.analyze_chunk(chunk)
        
        assert result == {}


class TestRAGTool:
    """RAGTool 클래스 테스트"""
    
    def setup_method(self):
        """테스트 설정"""
        self.mock_vector_db = Mock()
        self.tool = RAGTool(self.mock_vector_db)
    
    def test_execute_with_filters(self):
        """필터가 있는 검색 테스트"""
        # Mock 검색 결과 설정
        mock_results = {
            "documents": [["조언1", "조언2"]],
            "distances": [[0.1, 0.3]]
        }
        self.mock_vector_db.search_similar_advice.return_value = mock_results
        
        state = AgentState()
        state.user_input = "오늘 정말 힘들었어요"
        state.emotion = "슬픔"
        state.situation = "직장 문제"
        
        result = self.tool.execute(state)
        
        assert result is not None
        assert "조언1" in result
        assert "조언2" in result
        self.mock_vector_db.search_similar_advice.assert_called_once_with(
            "오늘 정말 힘들었어요", 5, emotion_filter=["슬픔"], situation_filter="직장 문제"
        )
    
    def test_execute_with_emotion_filter_only(self):
        """감정 필터만 있는 검색 테스트"""
        mock_results = {
            "documents": [["조언1"]],
            "distances": [[0.2]]
        }
        self.mock_vector_db.search_similar_advice.return_value = mock_results
        
        state = AgentState()
        state.user_input = "오늘 정말 힘들었어요"
        state.emotion = "슬픔"
        
        result = self.tool.execute(state)
        
        assert result is not None
        self.mock_vector_db.search_similar_advice.assert_called_once_with(
            "오늘 정말 힘들었어요", 5, emotion_filter=["슬픔"]
        )
    
    def test_execute_general_search(self):
        """일반 검색 테스트"""
        mock_results = {
            "documents": [["조언1"]],
            "distances": [[0.2]]
        }
        self.mock_vector_db.search_similar_advice.return_value = mock_results
        
        state = AgentState()
        state.user_input = "오늘 정말 힘들었어요"
        
        result = self.tool.execute(state)
        
        assert result is not None
        self.mock_vector_db.search_similar_advice.assert_called_once_with(
            "오늘 정말 힘들었어요", 5
        )
    
    def test_execute_no_results(self):
        """검색 결과가 없는 경우 테스트"""
        self.mock_vector_db.search_similar_advice.return_value = {"documents": [[]]}
        
        state = AgentState()
        state.user_input = "오늘 정말 힘들었어요"
        
        result = self.tool.execute(state)
        
        assert result is None
    
    def test_format_results_with_low_similarity(self):
        """낮은 유사도 결과 필터링 테스트"""
        mock_results = {
            "documents": [["조언1", "조언2"]],
            "distances": [[0.8, 0.2]]  # 0.8은 유사도 임계값(0.5)보다 낮음
        }
        self.mock_vector_db.search_similar_advice.return_value = mock_results
        
        state = AgentState()
        state.user_input = "오늘 정말 힘들었어요"
        
        result = self.tool.execute(state)
        
        # 0.8 유사도는 필터링되어 조언2만 포함되어야 함
        assert result is not None
        assert "조언2" in result
        assert "조언1" not in result


class TestResponseGenerationTool:
    """ResponseGenerationTool 클래스 테스트"""
    
    def setup_method(self):
        """테스트 설정"""
        self.mock_llm_service = Mock()
        self.tool = ResponseGenerationTool(self.mock_llm_service)
    
    def test_execute_complex_event_with_rag(self):
        """복합 사건 + RAG 데이터가 있는 응답 생성 테스트"""
        self.mock_llm_service.get_response.return_value = "따뜻한 조언"
        
        state = AgentState()
        state.user_input = "오늘 정말 힘들었어요"
        state.intent = "Complex Event"
        state.history = [{"role": "user", "content": "안녕하세요"}]
        
        rag_data = "관련 조언들..."
        result = self.tool.execute(state, rag_data)
        
        assert result == "따뜻한 조언"
        self.mock_llm_service.get_response.assert_called_once()
    
    def test_execute_complex_event_without_rag(self):
        """복합 사건 + RAG 데이터가 없는 응답 생성 테스트"""
        self.mock_llm_service.get_response.return_value = "따뜻한 조언"
        
        state = AgentState()
        state.user_input = "오늘 정말 힘들었어요"
        state.intent = "Complex Event"
        state.history = [{"role": "user", "content": "안녕하세요"}]
        
        result = self.tool.execute(state)
        
        assert result == "따뜻한 조언"
        self.mock_llm_service.get_response.assert_called_once()
    
    def test_execute_simple_emotion(self):
        """단순 감정 표현 응답 생성 테스트"""
        self.mock_llm_service.get_response.return_value = "감정 공감"
        
        state = AgentState()
        state.user_input = "기뻐요"
        state.intent = "Simple Emotion"
        state.history = [{"role": "user", "content": "안녕하세요"}]
        
        result = self.tool.execute(state)
        
        assert result == "감정 공감"
        self.mock_llm_service.get_response.assert_called_once()
    
    def test_execute_unknown_intent(self):
        """알 수 없는 의도에 대한 응답 테스트"""
        state = AgentState()
        state.intent = "Unknown"
        
        result = self.tool.execute(state)
        
        assert "더 자세히 설명해주실 수 있나요" in result


class TestClarifyTool:
    """ClarifyTool 클래스 테스트"""
    
    def setup_method(self):
        """테스트 설정"""
        self.tool = ClarifyTool()
    
    def test_execute(self):
        """명확화 요청 테스트"""
        state = AgentState()
        state.user_input = "힘들어요"
        
        result = self.tool.execute(state)
        
        assert "더 자세히 설명해주실 수 있나요" in result
        assert "구체적으로 이야기해주시면" in result


class TestMainAgent:
    """MainAgent 클래스 테스트"""
    
    def setup_method(self):
        """테스트 설정"""
        self.user_id = "test_user_123"
        
        # 의존성 모킹
        with patch('chatbot.main_agent.LLMService') as mock_llm_class, \
             patch('chatbot.main_agent.VectorDatabase') as mock_vector_db_class, \
             patch('chatbot.main_agent.ConversationManager') as mock_conversation_manager_class:
            
            self.mock_llm_service = Mock()
            self.mock_vector_db = Mock()
            self.mock_conversation_manager = Mock()
            
            mock_llm_class.return_value = self.mock_llm_service
            mock_vector_db_class.return_value = self.mock_vector_db
            mock_conversation_manager_class.return_value = self.mock_conversation_manager
            
            self.agent = MainAgent(self.user_id)
    
    def test_main_agent_initialization(self):
        """MainAgent 초기화 테스트"""
        assert self.agent.user_id == self.user_id
        assert self.agent.is_initialized is False
        assert hasattr(self.agent, 'tools')
        assert hasattr(self.agent, 'state')
        assert isinstance(self.agent.state, AgentState)
    
    def test_initialize_success(self):
        """성공적인 초기화 테스트"""
        self.mock_vector_db.initialize.return_value = None
        
        self.agent.initialize()
        
        assert self.agent.is_initialized is True
        self.mock_vector_db.initialize.assert_called_once()
    
    def test_initialize_failure(self):
        """초기화 실패 테스트"""
        self.mock_vector_db.initialize.side_effect = Exception("초기화 실패")
        
        with pytest.raises(Exception):
            self.agent.initialize()
        
        assert self.agent.is_initialized is False
    
    def test_perceive(self):
        """상황 인지 테스트"""
        user_input = "오늘 정말 힘들었어요"
        mock_history = [{"role": "user", "content": "안녕하세요"}]
        self.mock_conversation_manager.get_recent_conversation.return_value = mock_history
        
        state = self.agent.perceive(user_input)
        
        assert state.user_input == user_input
        assert state.history == mock_history
        assert state.user_input_length == len(user_input)
        self.mock_conversation_manager.get_recent_conversation.assert_called_once_with(
            self.user_id, count=10
        )
    
    def test_decide_ambiguous_input(self):
        """모호한 입력에 대한 의사결정 테스트"""
        self.agent.state.user_input = "힘들어요"
        self.agent.state.requires_clarification = True
        
        # Mock 의도 분석 결과
        mock_analysis_result = {"intent": "Ambiguous"}
        self.agent.tools['conversation_management'].analyze.return_value = mock_analysis_result
        
        plan = self.agent.decide()
        
        assert plan == ['clarify']
        self.agent.tools['conversation_management'].analyze.assert_called_once()
    
    def test_decide_complex_event(self):
        """복합 사건에 대한 의사결정 테스트"""
        self.agent.state.user_input = "오늘 회사에서 정말 힘든 일이 있었어요"
        
        # Mock 의도 분석 결과
        mock_analysis_result = {"intent": "Complex Event"}
        self.agent.tools['conversation_management'].analyze.return_value = mock_analysis_result
        
        plan = self.agent.decide()
        
        assert plan == ['rag', 'response_generation']
    
    def test_decide_simple_emotion(self):
        """단순 감정에 대한 의사결정 테스트"""
        self.agent.state.user_input = "기뻐요"
        
        # Mock 의도 분석 결과
        mock_analysis_result = {"intent": "Simple Emotion"}
        self.agent.tools['conversation_management'].analyze.return_value = mock_analysis_result
        
        plan = self.agent.decide()
        
        assert plan == ['response_generation']
    
    def test_act_success(self):
        """성공적인 도구 실행 테스트"""
        plan = ['rag', 'response_generation']
        
        # Mock 도구 실행 결과
        self.agent.tools['rag'].execute.return_value = "관련 조언들..."
        self.agent.tools['response_generation'].execute.return_value = "따뜻한 응답"
        
        results = self.agent.act(plan)
        
        assert results['rag_data'] == "관련 조언들..."
        assert results['response'] == "따뜻한 응답"
        self.agent.tools['rag'].execute.assert_called_once()
        self.agent.tools['response_generation'].execute.assert_called_once()
    
    def test_act_tool_failure(self):
        """도구 실행 실패 테스트"""
        plan = ['rag']
        
        # Mock 도구 실행 실패
        self.agent.tools['rag'].execute.side_effect = Exception("도구 실행 실패")
        
        results = self.agent.act(plan)
        
        assert "도구 실행 중 오류 발생" in results['rag']
    
    def test_get_response_success(self):
        """성공적인 응답 생성 테스트"""
        self.agent.is_initialized = True
        
        # Mock 의존성들
        self.mock_conversation_manager.get_recent_conversation.return_value = []
        self.agent.tools['conversation_management'].analyze.return_value = {"intent": "Simple Emotion"}
        self.agent.tools['response_generation'].execute.return_value = "따뜻한 응답"
        
        user_input = "오늘 정말 힘들었어요"
        result = self.agent.get_response(user_input)
        
        assert result["success"] is True
        assert result["response"] == "따뜻한 응답"
        self.mock_conversation_manager.add_to_conversation.assert_called()
    
    def test_get_response_not_initialized(self):
        """초기화되지 않은 에이전트 테스트"""
        self.agent.is_initialized = False
        
        result = self.agent.get_response("안녕하세요")
        
        assert result["success"] is False
        assert "초기화되지 않았습니다" in result["response"]
    
    def test_get_response_exception(self):
        """응답 생성 중 예외 발생 테스트"""
        self.agent.is_initialized = True
        self.mock_conversation_manager.get_recent_conversation.side_effect = Exception("오류")
        
        result = self.agent.get_response("안녕하세요")
        
        assert result["success"] is False
        assert "오류가 발생했습니다" in result["response"]
    
    def test_end_conversation_success(self):
        """성공적인 대화 종료 테스트"""
        self.agent.is_initialized = True
        
        # Mock 대화 기록
        mock_history = [
            {"role": "user", "content": "안녕하세요"},
            {"role": "assistant", "content": "안녕하세요!"}
        ]
        self.mock_conversation_manager.get_recent_conversation.return_value = mock_history
        self.mock_llm_service.get_response.return_value = "대화 요약"
        
        result = self.agent.end_conversation()
        
        assert result["success"] is True
        assert result["response"] == "대화 요약"
        self.mock_conversation_manager.clear_conversation_history.assert_called_once_with(self.user_id)
    
    def test_end_conversation_no_history(self):
        """대화 기록이 없는 종료 테스트"""
        self.agent.is_initialized = True
        self.mock_conversation_manager.get_recent_conversation.return_value = []
        
        result = self.agent.end_conversation()
        
        assert result["success"] is True
        assert "나중에 또 만나요" in result["response"]
    
    def test_end_conversation_not_initialized(self):
        """초기화되지 않은 에이전트의 대화 종료 테스트"""
        self.agent.is_initialized = False
        
        result = self.agent.end_conversation()
        
        assert result["success"] is False
        assert "초기화되지 않았습니다" in result["response"]


class TestMainAgentIntegration:
    """MainAgent 통합 테스트"""
    
    @pytest.fixture
    def mock_agent(self):
        """Mock MainAgent 설정"""
        with patch('chatbot.main_agent.LLMService') as mock_llm_class, \
             patch('chatbot.main_agent.VectorDatabase') as mock_vector_db_class, \
             patch('chatbot.main_agent.ConversationManager') as mock_conversation_manager_class:
            
            mock_llm_service = Mock()
            mock_vector_db = Mock()
            mock_conversation_manager = Mock()
            
            mock_llm_class.return_value = mock_llm_service
            mock_vector_db_class.return_value = mock_vector_db
            mock_conversation_manager_class.return_value = mock_conversation_manager
            
            agent = MainAgent("test_user")
            agent.is_initialized = True
            
            # Mock 도구들 설정
            agent.tools['conversation_management'].analyze.return_value = {
                "intent": "Complex Event",
                "emotion": "슬픔",
                "situation": "직장 문제"
            }
            agent.tools['rag'].execute.return_value = "관련 조언들..."
            agent.tools['response_generation'].execute.return_value = "따뜻한 조언"
            
            yield agent
    
    def test_full_conversation_flow(self, mock_agent):
        """전체 대화 흐름 테스트"""
        user_input = "오늘 회사에서 정말 힘든 일이 있었어요"
        
        result = mock_agent.get_response(user_input)
        
        assert result["success"] is True
        assert result["response"] == "따뜻한 조언"
        
        # 도구들이 올바른 순서로 호출되었는지 확인
        mock_agent.tools['conversation_management'].analyze.assert_called_once()
        mock_agent.tools['rag'].execute.assert_called_once()
        mock_agent.tools['response_generation'].execute.assert_called_once()
    
    def test_simple_emotion_flow(self, mock_agent):
        """단순 감정 표현 흐름 테스트"""
        # 단순 감정으로 설정
        mock_agent.tools['conversation_management'].analyze.return_value = {
            "intent": "Simple Emotion"
        }
        
        user_input = "기뻐요"
        result = mock_agent.get_response(user_input)
        
        assert result["success"] is True
        # RAG 도구는 호출되지 않아야 함
        mock_agent.tools['rag'].execute.assert_not_called()
        mock_agent.tools['response_generation'].execute.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 