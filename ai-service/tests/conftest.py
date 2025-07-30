"""
pytest 설정 및 공통 fixture 정의

이 파일은 테스트 실행에 필요한 공통 설정과 fixture들을 정의합니다.
"""

import pytest
import os
import sys
from unittest.mock import Mock, patch

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 테스트용 환경 변수 설정
os.environ.setdefault('OPENAI_API_KEY', 'test-api-key')
os.environ.setdefault('GPT_MODEL', 'gpt-3.5-turbo')
os.environ.setdefault('MAX_TOKENS', '1000')
os.environ.setdefault('TEMPERATURE', '0.7')
os.environ.setdefault('EMBEDDING_MODEL', 'sentence-transformers/all-MiniLM-L6-v2')
os.environ.setdefault('CHROMA_PERSIST_DIRECTORY', './test_chroma_db')
os.environ.setdefault('COLLECTION_NAME', 'test_advice')
os.environ.setdefault('QUOTES_COLLECTION_NAME', 'test_quotes')
os.environ.setdefault('PAST_DIARIES_COLLECTION_NAME', 'test_past_diaries')


@pytest.fixture(scope="session")
def test_user_id():
    """테스트용 사용자 ID"""
    return "test_user_123"


@pytest.fixture(scope="session")
def sample_conversation_history():
    """샘플 대화 기록"""
    return [
        {"role": "user", "content": "안녕하세요"},
        {"role": "assistant", "content": "안녕하세요! 오늘은 어떤 이야기를 나누고 싶으신가요?"},
        {"role": "user", "content": "오늘 정말 힘들었어요"},
        {"role": "assistant", "content": "힘드셨군요. 어떤 일이 있었는지 이야기해주세요."}
    ]


@pytest.fixture(scope="session")
def sample_user_inputs():
    """다양한 사용자 입력 샘플"""
    return {
        "simple_emotion": "기뻐요",
        "complex_event": "오늘 회사에서 정말 힘든 일이 있었어요. 상사가 저를 무시하는 것 같고, 동료들도 저를 따돌리는 것 같아요.",
        "ambiguous": "힘들어요",
        "question": "어떻게 해야 할까요?",
        "long_input": "오늘 회사에서 정말 힘든 일이 있었어요. 상사가 저를 무시하는 것 같고, 동료들도 저를 따돌리는 것 같아요. 집에 와서도 계속 그 생각만 하고 있어요. 어떻게 해야 할지 모르겠어요."
    }


@pytest.fixture(scope="session")
def sample_analysis_results():
    """샘플 의도 분석 결과"""
    return {
        "simple_emotion": {
            "intent": "Simple Emotion",
            "emotion": "기쁨",
            "situation": None
        },
        "complex_event": {
            "intent": "Complex Event",
            "emotion": "슬픔",
            "situation": "직장 문제"
        },
        "ambiguous": {
            "intent": "Ambiguous",
            "emotion": None,
            "situation": None
        }
    }


@pytest.fixture(scope="session")
def sample_rag_results():
    """샘플 RAG 검색 결과"""
    return {
        "documents": [["조언1", "조언2", "조언3"]],
        "distances": [[0.1, 0.3, 0.6]]
    }


@pytest.fixture(scope="session")
def sample_responses():
    """샘플 응답"""
    return {
        "simple_emotion": "정말 기뻐하시는 모습이 보기 좋네요!",
        "complex_event": "정말 힘드셨겠어요. 그런 상황에서 슬프고 답답하셨을 것 같아요. 하지만 당신은 충분히 강한 사람이에요.",
        "clarify": "어떤 말씀을 하시는지 더 자세히 설명해주실 수 있나요? 오늘 있었던 일이나 감정에 대해 조금 더 구체적으로 이야기해주시면 제가 더 잘 이해하고 도울 수 있을 것 같아요."
    }


@pytest.fixture
def mock_llm_service():
    """Mock LLMService"""
    with patch('chatbot.llm_service.LLMService') as mock_class:
        mock_service = Mock()
        mock_class.return_value = mock_service
        yield mock_service


@pytest.fixture
def mock_vector_db():
    """Mock VectorDatabase"""
    with patch('core.vector_db.VectorDatabase') as mock_class:
        mock_db = Mock()
        mock_class.return_value = mock_db
        yield mock_db


@pytest.fixture
def mock_conversation_manager():
    """Mock ConversationManager"""
    with patch('chatbot.conversation_manager.ConversationManager') as mock_class:
        mock_manager = Mock()
        mock_class.return_value = mock_manager
        yield mock_manager


@pytest.fixture
def mock_agent_dependencies(mock_llm_service, mock_vector_db, mock_conversation_manager):
    """모든 의존성이 모킹된 상태"""
    return {
        'llm_service': mock_llm_service,
        'vector_db': mock_vector_db,
        'conversation_manager': mock_conversation_manager
    }


@pytest.fixture
def clean_test_environment():
    """테스트 환경 정리"""
    yield


# 테스트 마커 정의
def pytest_configure(config):
    """pytest 설정"""
    config.addinivalue_line(
        "markers", "unit: 단위 테스트"
    )
    config.addinivalue_line(
        "markers", "integration: 통합 테스트"
    )
    config.addinivalue_line(
        "markers", "slow: 느린 테스트"
    )


# 테스트 결과 요약 출력
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """테스트 결과 요약"""
    print("\n" + "="*50)
    print("테스트 결과 요약")
    print("="*50)
    
    if exitstatus == 0:
        print("모든 테스트가 성공했습니다!")
    else:
        print("일부 테스트가 실패했습니다.")
    
    print("="*50) 