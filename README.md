# 일기 관리 시스템

## 테스트 계정 정보

시스템 초기화 시 자동으로 생성되는 테스트 계정:
- **사용자명**: testuser
- **이메일**: test@example.com  
- **비밀번호**: 1234

## 프로젝트 구조

```
Toy_4/
├── backend/          # Spring Boot 백엔드
├── ai-service/       # FastAPI AI 서비스
├── docker-compose.yml
├── docker-compose.dev.yml
├── env.example
└── README.md
```

## Docker 사용법

### 1. 전체 시스템 실행 (권장)

```bash
# 전체 서비스 실행
docker-compose up --build

# 백그라운드 실행
docker-compose up -d --build

# 특정 서비스만 실행
docker-compose up backend ai-service
```

### 2. 개발 환경 실행

```bash
# 개발용 설정으로 실행
docker-compose -f docker-compose.dev.yml up --build
```

### 3. 서비스 관리

```bash
# 서비스 상태 확인
docker-compose ps

# 로그 확인
docker-compose logs
docker-compose logs backend
docker-compose logs ai-service

# 서비스 중지
docker-compose down

# 볼륨까지 삭제 (데이터 초기화)
docker-compose down -v

# 이미지 재빌드
docker-compose build --no-cache
```

### 4. 데이터베이스 접속

```bash
# MySQL 접속
docker exec -it diary_mysql mysql -u diary_user -p diary_db

# Redis 접속
docker exec -it diary_redis redis-cli

# 백엔드 컨테이너 접속
docker exec -it diary_backend /bin/bash

# AI 서비스 컨테이너 접속
docker exec -it diary_ai_service /bin/bash
```

## 초기 데이터 정보

### MySQL 데이터

#### 사용자 데이터
- **테스트 계정**: testuser / 1234
- **초기 포인트**: 100점

#### 스탬프 데이터
1. **행복** (10포인트) - 행복한 하루를 보낸 스탬프
2. **감사** (15포인트) - 감사한 마음을 표현한 스탬프
3. **성장** (20포인트) - 성장하는 모습을 보인 스탬프
4. **도전** (25포인트) - 새로운 도전을 시도한 스탬프
5. **휴식** (10포인트) - 잘 쉬어가는 스탬프

#### 추천 활동 데이터
1. **산책하기** (5포인트) - 자연 속에서 마음을 정리해보세요
2. **독서하기** (10포인트) - 좋은 책을 읽으며 지식을 쌓아보세요
3. **명상하기** (8포인트) - 마음을 차분히 가라앉혀보세요
4. **운동하기** (7포인트) - 몸을 움직여 활력을 되찾아보세요
5. **창작활동** (12포인트) - 창의력을 발휘해보세요

### ChromaDB 데이터 (AI 서비스)

#### 일기 샘플 데이터
- 5개의 샘플 일기 (행복, 성장, 감사, 도전, 학습 감정)
- 각 일기마다 감정 키워드와 날짜 정보 포함

#### 조언 샘플 데이터
- 5개의 AI 조언 (목표설정, 인간관계, 성장, 자기계발, 습관)
- 카테고리별 분류된 조언 데이터

#### 인용구 샘플 데이터
- 5개의 영감을 주는 인용구
- 마하트마 간디, 로버트 콜리어, 벤자민 프랭클린 등

## 서비스 포트 정보

| 서비스 | 포트 | 설명 |
|--------|------|------|
| Backend | 8080 | Spring Boot 애플리케이션 |
| AI Service | 8000 | FastAPI AI 서비스 |
| MySQL | 3308 | 데이터베이스 |
| Redis | 6379 | 캐시 서버 |

## 환경 변수 설정

### 필수 환경 변수
```bash
# .env 파일 생성
cp env.example .env

# OpenAI API 키 설정 (선택사항)
OPENAI_API_KEY=your_openai_api_key_here
```

### 데이터베이스 환경 변수
```bash
# MySQL 설정
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=diary_db
MYSQL_USER=diary_user
MYSQL_PASSWORD=diary_password

# Redis 설정
REDIS_URL=redis://localhost:6379
```

## 데이터 백업 및 복원

### MySQL 데이터 백업
```bash
# 데이터 백업
docker exec diary_mysql mysqldump -u diary_user -p diary_db > backup.sql

# 데이터 복원
docker exec -i diary_mysql mysql -u diary_user -p diary_db < backup.sql
```

### ChromaDB 데이터 백업
```bash
# AI 서비스 데이터 백업
docker cp diary_ai_service:/app/data ./ai_service_backup

# AI 서비스 데이터 복원
docker cp ./ai_service_backup diary_ai_service:/app/data
```

## 문제 해결

### 포트 충돌 문제
```bash
# 포트 사용 확인
netstat -ano | findstr :3308
netstat -ano | findstr :8080

# 포트 변경 (docker-compose.yml 수정)
ports:
  - "3309:3306"  # MySQL 포트 변경
```

### 메모리 부족 문제
```bash
# Docker 메모리 설정 확인
docker system df

# 사용하지 않는 리소스 정리
docker system prune -a
```

### 로그 확인
```bash
# 실시간 로그 확인
docker-compose logs -f

# 특정 서비스 로그
docker-compose logs -f backend
docker-compose logs -f ai-service
```

## 개발 환경 설정

### 로컬 개발 (Docker 없이)
```bash
# 백엔드 실행
cd backend
mvn spring-boot:run

# AI 서비스 실행
cd ai-service
pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### IDE 설정
- **IntelliJ IDEA**: Spring Boot 프로젝트로 import
- **VS Code**: Python 확장 설치 후 AI 서비스 폴더 열기

## 주요 기능

- 일기 작성 및 관리
- AI 기반 일기 분석
- 감정 분석 및 통계
- 스탬프 시스템
- 포인트 시스템
- ChromaDB 기반 벡터 검색

## 기술 스택

- **Backend**: Spring Boot, JPA, MySQL
- **AI Service**: FastAPI, ChromaDB, OpenAI
- **Database**: MySQL, Redis
- **Infrastructure**: Docker, Docker Compose 