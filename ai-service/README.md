# AI Service - RAG 에이전트

일기 데이터를 기반으로 한 감정 분석 및 상담 RAG(Retrieval-Augmented Generation) 에이전트입니다.

## 🚀 주요 기능

- **사용자 입력 분석**: 감정, 상황, 시간 컨텍스트 자동 추출
- **벡터 검색**: ChromaDB를 활용한 의미적 유사도 기반 검색
- **RAG 응답 생성**: 관련 일기 데이터를 기반으로 한 분석 및 조언
- **신뢰도 평가**: 검색 결과의 품질을 평가하는 신뢰도 점수

## 📁 프로젝트 구조

```
ai-service/
├── app/
│   ├── api/                    # FastAPI 엔드포인트
│   ├── core/                   # 설정 및 로깅
│   ├── db/                     # 데이터베이스 클라이언트
│   │   └── chroma_client.py    # ChromaDB 클라이언트
│   ├── models/                 # 데이터 모델
│   │   └── diary.py           # 일기 관련 모델
│   ├── services/               # 비즈니스 로직
│   │   ├── rag_agent.py       # RAG 에이전트 (핵심)
│   │   ├── embedding.py       # 임베딩 서비스
│   │   ├── data_loader.py     # 데이터 로더
│   │   └── chroma_service.py  # ChromaDB 서비스
│   └── utils/                  # 유틸리티
├── tests/                      # 테스트 파일
│   └── test_rag_agent.py      # RAG 에이전트 테스트
├── test_rag_demo.py           # 데모 스크립트
└── requirements.txt           # 의존성
```

## 🛠️ 설치 및 설정

### 1. 의존성 설치

```bash
cd ai-service
pip install -r requirements.txt
```

### 2. 환경 설정

```bash
# 가상환경 생성 (선택사항)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

## 🧪 테스트 방법

### 1. 단위 테스트 실행

```bash
# 전체 테스트 실행
pytest tests/ -v

# 특정 테스트만 실행
pytest tests/test_rag_agent.py::TestRAGAgent::test_emotion_extraction -v

# 통합 테스트만 실행
pytest tests/test_rag_agent.py -m integration -v
```

### 2. 데모 스크립트 실행

```bash
# 대화형 데모 실행
python test_rag_demo.py
```

### 3. 개별 모듈 테스트

```python
# Python 인터프리터에서 직접 테스트
from app.services.rag_agent import RAGAgent
from app.services.data_loader import DataLoader

# 데이터 로더로 샘플 데이터 생성
data_loader = DataLoader()
sample_entries = data_loader.generate_sample_diary_data(20)
data_loader.load_data_to_chroma(sample_entries)

# RAG 에이전트 테스트
rag_agent = RAGAgent()
response = rag_agent.process_query("요즘 계속 우울한데 이번 주에 내가 뭐 때문에 그런지 모르겠어")
print(response.analysis)
```

## 🔧 RAG 에이전트 동작 원리

### 1. 사용자 입력 분석

```python
user_input = "요즘 계속 우울한데 이번 주에 회사에서 힘들었다"

# 분석 결과
{
    "user_utterance": "요즘 계속 우울한데 이번 주에 회사에서 힘들었다",
    "inferred_emotion": "우울",
    "inferred_situation": "업무", 
    "time_context": "이번_주"
}
```

### 2. 검색 쿼리 생성

- **감정 키워드**: "우울", "슬픔", "절망", "무기력"
- **시간 필터**: 이번 주 (7일)
- **상황 필터**: 업무 관련

### 3. 벡터 검색

```python
# ChromaDB에서 유사한 일기 검색
search_results = chroma_client.search(
    query_embeddings=[query_embedding],
    n_results=15,
    where_filter={
        "context": "업무",
        "date": {"$gte": "2024-11-18", "$lte": "2024-11-24"}
    }
)
```

### 4. 유사도 기반 필터링

- 코사인 유사도 계산
- 상위 5개 결과 선택
- 신뢰도 점수 계산

### 5. 응답 생성

관련 일기 데이터를 기반으로 분석 및 조언 생성

## 📊 테스트 시나리오

### 기본 테스트 쿼리

1. **우울한 감정**: "요즘 계속 우울한데 이번 주에 내가 뭐 때문에 그런지 모르겠어"
2. **업무 스트레스**: "오늘 회의에서 내 의견이 무시당한 것 같아서 속상했다"
3. **사회적 불안**: "친구들과 만나기로 했는데 갑자기 기분이 안 좋아져서 취소했다"
4. **성취감**: "오늘 프로젝트가 성공적으로 완료되어서 정말 기뻤다"
5. **분노**: "동료가 내 일을 방해해서 정말 화가 났다"
6. **불안**: "내일 중요한 발표가 있어서 긴장된다"
7. **평온**: "오늘은 날씨가 좋아서 산책을 다녀왔다"

### 예상 결과

- **감정 추출**: 정확한 감정 키워드 매칭
- **상황 인식**: 업무, 가족, 친구, 건강 등 상황 분류
- **시간 컨텍스트**: 오늘, 어제, 이번 주 등 시간 범위 설정
- **유사도 검색**: 관련 일기 엔트리 검색 및 유사도 점수
- **신뢰도 평가**: 검색 결과 품질에 따른 신뢰도 점수

## 🔍 모니터링 및 디버깅

### 로그 확인

```python
import logging
logging.basicConfig(level=logging.INFO)

# RAG 에이전트 실행 시 상세 로그 확인
rag_agent = RAGAgent()
response = rag_agent.process_query("테스트 쿼리")
```

### 성능 메트릭

- **검색 시간**: 벡터 검색 소요 시간
- **유사도 점수**: 검색 결과의 평균 유사도
- **신뢰도 점수**: 전체 응답의 신뢰도
- **관련 엔트리 수**: 검색된 관련 일기 개수

## 🚀 향후 개선 사항

1. **LLM 통합**: 실제 LLM을 사용한 응답 생성
2. **감정 분석 고도화**: 더 정교한 감정 분류
3. **컨텍스트 윈도우**: 대화 히스토리 기반 컨텍스트
4. **개인화**: 사용자별 맞춤 분석
5. **실시간 학습**: 새로운 일기 데이터 자동 학습

## 📝 API 사용 예시

```python
from app.services.rag_agent import RAGAgent

# RAG 에이전트 초기화
rag_agent = RAGAgent()

# 쿼리 처리
response = rag_agent.process_query("사용자 입력")

# 결과 확인
print(f"분석: {response.analysis}")
print(f"신뢰도: {response.confidence_score}")
print(f"관련 엔트리 수: {len(response.related_entries)}")

for entry in response.related_entries:
    print(f"- {entry.content} (유사도: {entry.similarity_score:.3f})")
```
