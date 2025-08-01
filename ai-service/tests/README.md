# MainAgent 테스트 가이드

이 디렉토리는 MainAgent 클래스와 관련 컴포넌트들에 대한 포괄적인 테스트를 포함합니다.

## 테스트 구조

```
tests/
├── __init__.py              # 테스트 패키지 초기화
├── conftest.py              # pytest 설정 및 공통 fixture
├── test_main_agent.py       # MainAgent 단위 테스트
└── README.md               # 이 파일
```

## 테스트 범위

### 1. AgentState 클래스 테스트
- 초기화 및 상태 관리
- 입력 특성 분석 (복잡도, 모호성)
- 결과 기반 상태 업데이트

### 2. 도구(Tool) 클래스 테스트
- **ConversationManagementTool**: 의도 분석 및 청크 분석
- **RAGTool**: 벡터 검색 및 결과 필터링
- **ResponseGenerationTool**: 응답 생성 로직
- **ClarifyTool**: 명확화 요청

### 3. MainAgent 클래스 테스트
- 초기화 및 의존성 관리
- Perceive-Decide-Act 사이클
- 대화 관리 및 종료 처리
- 오류 처리 및 예외 상황

### 4. 통합 테스트
- 전체 대화 흐름 시뮬레이션
- 다양한 입력 유형별 처리
- 도구 간 상호작용 검증

## 테스트 실행 방법

### 1. 테스트 실행기 사용 (권장)

```bash
# 전체 테스트 실행
python run_tests.py

# 단위 테스트만 실행
python run_tests.py --unit

# 통합 테스트만 실행
python run_tests.py --integration

# 특정 테스트 파일 실행
python run_tests.py --file test_main_agent.py

# 커버리지 리포트와 함께 실행
python run_tests.py --coverage

# 빠른 테스트 실행 (느린 테스트 제외)
python run_tests.py --fast

# 의존성 확인
python run_tests.py --check-deps

# 테스트 정보 출력
python run_tests.py --info
```

### 2. pytest 직접 사용

```bash
# 전체 테스트 실행
pytest tests/ -v

# 특정 테스트 클래스 실행
pytest tests/test_main_agent.py::TestMainAgent -v

# 특정 테스트 메서드 실행
pytest tests/test_main_agent.py::TestMainAgent::test_initialize_success -v

# 마커를 사용한 테스트 실행
pytest tests/ -m unit -v
pytest tests/ -m integration -v
pytest tests/ -m "not slow" -v

# 커버리지와 함께 실행
pytest tests/ --cov=chatbot --cov-report=html --cov-report=term -v
```

## 테스트 마커

- `@pytest.mark.unit`: 단위 테스트
- `@pytest.mark.integration`: 통합 테스트
- `@pytest.mark.slow`: 느린 테스트 (실제 API 호출 등)

## 테스트 설정

### 환경 변수
테스트는 다음 환경 변수들을 사용합니다:
- `OPENAI_API_KEY`: 테스트용 API 키
- `GPT_MODEL`: 사용할 GPT 모델
- `EMBEDDING_MODEL`: 임베딩 모델
- `CHROMA_PERSIST_DIRECTORY`: 벡터 DB 저장 경로

### Mock 설정
- **LLMService**: 실제 API 호출 대신 Mock 응답 사용
- **VectorDatabase**: 실제 벡터 DB 대신 Mock 검색 결과 사용
- **ConversationManager**: 실제 Redis 대신 fakeredis 사용

## 커버리지 목표

현재 테스트는 다음 영역들을 커버합니다:
- AgentState 클래스: 100%
- ConversationManagementTool: 95%
- RAGTool: 90%
- ResponseGenerationTool: 95%
- ClarifyTool: 100%
- MainAgent 클래스: 85%

## 문제 해결

### 1. 의존성 오류
```bash
pip install pytest pytest-cov pytest-asyncio
```

### 2. Import 오류
```bash
# 프로젝트 루트에서 실행
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### 3. Mock 관련 오류
- 테스트에서 올바른 경로로 import 확인
- Mock 객체가 올바르게 설정되었는지 확인

### 4. 테스트 실패 시
1. 로그 확인: `pytest tests/ -v -s`
2. 특정 테스트만 실행: `pytest tests/test_main_agent.py::TestMainAgent::test_specific_method -v -s`
3. 디버깅 모드: `pytest tests/ --pdb`

## 테스트 작성 가이드

### 새로운 테스트 추가 시

1. **테스트 클래스 구조**:
```python
class TestNewFeature:
    def setup_method(self):
        """테스트 설정"""
        pass
    
    def test_feature_success(self):
        """성공 케이스 테스트"""
        pass
    
    def test_feature_failure(self):
        """실패 케이스 테스트"""
        pass
```

2. **Mock 사용 예시**:
```python
def test_with_mock(self):
    with patch('module.Class') as mock_class:
        mock_instance = Mock()
        mock_class.return_value = mock_instance
        mock_instance.method.return_value = "expected_result"
        
        # 테스트 로직
        result = function_under_test()
        
        assert result == "expected_result"
        mock_instance.method.assert_called_once()
```

3. **Fixture 사용**:
```python
def test_with_fixture(self, sample_user_inputs):
    user_input = sample_user_inputs["simple_emotion"]
    # 테스트 로직
```

## 지속적 통합 (CI)

테스트는 다음 상황에서 자동으로 실행됩니다:
- Pull Request 생성 시
- main 브랜치에 push 시
- 수동 트리거 시

## 추가 리소스

- [pytest 공식 문서](https://docs.pytest.org/)
- [unittest.mock 문서](https://docs.python.org/3/library/unittest.mock.html)
- [pytest-cov 문서](https://pytest-cov.readthedocs.io/)

## 기여하기

새로운 테스트를 추가할 때:
1. 기존 테스트 패턴을 따르세요
2. 적절한 마커를 사용하세요
3. 명확한 테스트 이름과 문서화를 제공하세요
4. Mock을 사용하여 외부 의존성을 격리하세요 