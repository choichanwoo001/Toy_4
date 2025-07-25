# AI Service

## 가상환경 세팅 및 실행 방법

1. Python 3.8 이상 설치
2. (선택) 프로젝트 루트에서 가상환경 생성 및 활성화
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. 패키지 설치
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. 환경변수 파일(.env) 작성 (예시)
   ```env
   PORT=8000
   MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2
   ```
5. FastAPI 서버 실행
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 프로젝트 구조

```
ai-service/
├── app/                      # FastAPI 메인 애플리케이션
│   ├── main.py               # FastAPI 엔트리포인트
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/    # API 엔드포인트 (diary, chat, health 등)
│   │       └── __init__.py
│   ├── services/             # 비즈니스 로직, 외부 서비스 연동
│   ├── db/                   # DB 클라이언트 및 쿼리
│   ├── models/               # Pydantic 데이터 모델
│   ├── core/                 # 설정, 로깅 등 핵심 유틸
│   └── utils/                # 텍스트 전처리 등 유틸 함수
├── tests/                    # 단위 테스트 코드
├── Dockerfile                # 도커 이미지 빌드 파일
├── docker-compose.yml        # 서비스 및 DB 통합 실행
├── requirements.txt          # Python 패키지 목록
├── README.md                 # 프로젝트 설명
└── .env                      # 환경변수 파일
```

## 폴더/파일 설명

- **app/main.py**: FastAPI 앱의 진입점입니다.
- **app/api/v1/endpoints/**: REST API 엔드포인트 구현 (예: diary.py, chat.py, health.py)
- **app/services/**: ChromaDB, 임베딩, 챗봇 등 주요 서비스 로직 구현
- **app/db/**: DB 클라이언트 및 쿼리 관련 코드 (예: chroma_client.py)
- **app/models/**: Pydantic을 활용한 데이터 모델 정의 (요청/응답 스키마)
- **app/core/**: 환경설정(config.py), 로깅(logger.py) 등 핵심 설정
- **app/utils/**: 텍스트 전처리 등 보조 유틸 함수
- **tests/**: 주요 기능별 단위 테스트 코드
- **Dockerfile**: AI 서비스 컨테이너 빌드용 파일
- **docker-compose.yml**: ChromaDB 등 외부 서비스와 통합 실행 환경
- **requirements.txt**: 필요한 Python 패키지 목록
- **.env**: 환경변수 파일 (PORT, MODEL_NAME 등)

## 예시: 엔드포인트 추가

새로운 API 엔드포인트를 추가하려면 `app/api/v1/endpoints/`에 파일을 생성하고, `main.py`에서 라우터로 등록하세요.

## 예시: 서비스 로직 추가

임베딩, 챗봇 등 주요 기능은 `app/services/`에 모듈로 분리해 구현합니다.

---

문의사항이나 기여는 이슈/PR로 남겨주세요. 