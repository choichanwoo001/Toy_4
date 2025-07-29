# AI Service

AI 서비스는 일기 분석 및 댓글 생성, 그리고 채팅 기능을 제공하는 FastAPI 기반 웹 서비스입니다.

## 프로젝트 구조

```
ai-service/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           ├── chat.py          # 채팅 API 엔드포인트
│   │           ├── diary.py         # 일기 처리 API 엔드포인트
│   │           └── health.py        # 헬스체크 API
│   ├── core/
│   │   ├── config.py               # 설정 관리
│   │   └── logger.py               # 로깅 설정
│   ├── db/
│   │   └── chroma_client.py        # 벡터 데이터베이스 클라이언트
│   ├── models/
│   │   └── diary.py                # 데이터 모델
│   ├── services/
│   │   ├── chatbot.py              # 채팅봇 서비스
│   │   ├── chroma_service.py       # 벡터 DB 서비스
│   │   ├── comment_gen.py          # 댓글 생성 서비스
│   │   ├── comment_generator.py    # 댓글/피드백 생성 파이프라인
│   │   └── embedding.py            # 임베딩 서비스
│   └── utils/
│       └── preprocessor.py         # 전처리 유틸리티
├── tests/
│   ├── test_chat.py               # 채팅 기능 테스트
│   ├── test_comments.py           # 댓글/피드백 생성 테스트
│   └── test_preprocessing.py      # 전처리 기능 테스트
├── requirements.txt
├── run_tests.py
└── README.md
```

## 주요 기능

### 1. 댓글/피드백 생성 파이프라인 (`comment_generator.py`)

사용자의 일기를 분석하여 의미 있는 댓글이나 피드백을 생성하는 파이프라인입니다.

**파이프라인 구조:**
```
사용자 일기 입력 → 전처리 → 프롬프트 A → LLM 청킹 → 프롬프트 B → 청크 수 확인 → 프롬프트 C
```

- **전처리**: 문맥 분석, 문법 교정
- **프롬프트 A**: 일기 정제 및 문맥 분석 강화
- **LLM 청킹**: 의미 기반 청크 분리
- **프롬프트 B**: 청크 품질 검증 및 의미 일관성 확인
- **프롬프트 C**: 무미건조한 일기에 대한 맞춤형 피드백

### 2. 채팅 기능 (`test_chat.py`)

실제 채팅 대화를 처리하는 기능입니다.

- 사용자 메시지 처리
- 채팅 세션 관리
- 대화 컨텍스트 유지
- 실시간 응답 생성

## 테스트 구조

### 1. 전체 파이프라인 테스트 (`test_chat.py`)
- 채팅 서비스 기능 테스트
- 메시지 처리 및 응답 생성
- 세션 관리 및 컨텍스트 처리
- 채팅 통합 시나리오

### 2. 전처리 전용 테스트 (`test_preprocessing.py`)
- 기본 전처리 기능
- 문법 교정 및 문맥 분석
- 프롬프트 A 적용 테스트
- 강화된 감정/키워드 추출
- 텍스트 정제 및 에러 처리

### 3. 댓글/피드백 생성 테스트 (`test_comments.py`)
- 댓글 생성 파이프라인 전체 테스트
- 프롬프트 C 피드백 생성
- 무미건조한 일기 감지
- 피드백 내용 분석 및 톤 확인
- 통합 시나리오 테스트

## 설치 및 실행

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. 테스트 실행
```bash
python run_tests.py
```

또는 개별 테스트 실행:
```bash
# 채팅 기능 테스트
pytest tests/test_chat.py -v

# 댓글 생성 테스트
pytest tests/test_comments.py -v

# 전처리 기능 테스트
pytest tests/test_preprocessing.py -v
```

### 3. 서비스 실행
```bash
uvicorn app.main:app --reload
```

## API 엔드포인트

### 채팅 API
- `POST /api/v1/chat/message`: 사용자 메시지 처리
- `GET /api/v1/chat/session/{session_id}`: 채팅 세션 조회

### 일기 처리 API
- `POST /api/v1/diary/process`: 일기 입력 처리 및 댓글 생성
- `GET /api/v1/diary/health`: 서비스 상태 확인

## 개발 가이드

### Contract-first 원칙
모든 AI 에이전트의 입출력은 JSON 스키마로 고정되어 있으며, 파싱 실패 시 재요청 또는 폴백을 수행합니다.

### 에러 처리
- LLM 파싱 실패: 재시도 (최대 3회)
- API 타임아웃: 재시도 (최대 2회)
- 폴백 응답: 일반적인 공감 메시지 또는 더 많은 입력 요청

### 관찰성
- 처리 시간, 토큰 사용량, 점수 로깅
- 샘플링 요청을 사람이 검토할 수 있도록 설정

## 라이센스

MIT License 