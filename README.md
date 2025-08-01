# 일기 관리 시스템 - 로컬 테스트 가이드

## ⚠️ 중요 안내
**Docker 환경에서 문제가 발생할 수 있으므로, 로컬 환경에서 테스트를 진행해주세요.**

## 📋 목차
1. [시스템 요구사항](#시스템-요구사항)
2. [로컬 환경 설정](#로컬-환경-설정)
3. [데이터베이스 설정](#데이터베이스-설정)
4. [ChromaDB 설정](#chromadb-설정)
5. [서비스 실행](#서비스-실행)
6. [테스트 시나리오](#테스트-시나리오)
7. [문제 해결](#문제-해결)

## 🖥️ 시스템 요구사항

### 필수 소프트웨어
- **Java 21** (JDK 21)
- **Python 3.9+** (3.11 권장)
- **MySQL 8.0** (또는 MariaDB 10.5+)
- **Redis 6.0+** (선택사항, AI 서비스용)
- **Git** (코드 다운로드용)
- **웹 브라우저** (Chrome, Firefox, Safari 등)

### 권장 사양
- **RAM**: 8GB 이상
- **저장공간**: 10GB 이상 여유 공간
- **OS**: Windows 10/11, macOS, Linux

## ⚙️ 로컬 환경 설정

### 1. 프로젝트 다운로드
```bash
# 프로젝트 클론
git clone [프로젝트_URL]
cd Toy_4

# 또는 압축 파일 다운로드 후 압축 해제
```

### 2. Java 환경 설정
```bash
# Java 21 설치 확인
java -version

# Maven 설치 확인
mvn -version

# Java 21이 설치되지 않은 경우:
# Windows: https://adoptium.net/ 에서 다운로드
# macOS: brew install openjdk@21
# Linux: sudo apt install openjdk-21-jdk
```

### 3. Python 환경 설정
```bash
# Python 버전 확인
python --version

# 가상환경 생성 (권장)
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# AI 서비스 의존성 설치
cd ai-service
pip install -r requirements.txt
cd ..
```

### 4. 환경 변수 설정
```bash
# 환경 변수 파일 복사
cp env.example .env

# .env 파일 편집
# OpenAI API 키가 있다면 설정
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. 포트 확인
다음 포트들이 사용 가능한지 확인:
- **3306**: MySQL 데이터베이스
- **8080**: Spring Boot 백엔드
- **8000**: AI 서비스
- **6379**: Redis (선택사항)

## 🗄️ 데이터베이스 설정

### 1. MySQL 설치 및 설정
```bash
# Windows: https://dev.mysql.com/downloads/installer/
# macOS: brew install mysql
# Linux: sudo apt install mysql-server

# MySQL 서비스 시작
# Windows: 서비스 관리자에서 MySQL 시작
# macOS: brew services start mysql
# Linux: sudo systemctl start mysql

# MySQL 접속
mysql -u root -p

# rebuild_db 데이터베이스 생성
CREATE DATABASE rebuild_db;
CREATE USER 'diary_user'@'localhost' IDENTIFIED BY 'diary_password';
GRANT ALL PRIVILEGES ON rebuild_db.* TO 'diary_user'@'localhost';
FLUSH PRIVILEGES;

# 종료
exit
```

### 2. 초기 데이터 삽입
```bash
# init.sql 파일 실행
mysql -u diary_user -p rebuild_db < backend/src/main/resources/data/init.sql
# 비밀번호: diary_password
```

### 3. 데이터 확인
```bash
# MySQL 접속하여 데이터 확인
mysql -u diary_user -p rebuild_db
# 비밀번호: diary_password

# 테이블 확인
SHOW TABLES;

# 사용자 데이터 확인
SELECT * FROM user;

# 스탬프 데이터 확인
SELECT * FROM stamp;

# 일기 데이터 확인
SELECT * FROM diary LIMIT 5;

# 종료
exit
```

## 🧠 ChromaDB 설정

### 1. AI 서비스 데이터 폴더 확인
```bash
# ai-service/data 폴더 구조 확인
ls -la ai-service/data/

# ChromaDB 폴더 확인
ls -la ai-service/data/chroma_db/
```

### 3. 개별 데이터 초기화 (선택사항)
(TOY_4 폴더에서)
```bash
# 조언 데이터만 초기화
python ai-service/data/init_advice_only.py

# 인용구 데이터만 초기화
python ai-service/data/init_quotes_only.py

# 과거 일기 데이터만 초기화
python ai-service/data/init_past_diaries_only.py
```

### 4. ChromaDB 데이터 확인
```bash
# Python으로 데이터 확인
python -c "
import chromadb
client = chromadb.PersistentClient(path='data/chroma_db')
collections = client.list_collections()
print('컬렉션 목록:', [col.name for col in collections])
for col in collections:
    print(f'{col.name}: {col.count()} 개 데이터')
"
```

## 🚀 서비스 실행

### 1. 백엔드 서비스 실행
```bash
# 프로젝트 루트로 이동
cd ..

# 백엔드 디렉토리로 이동
cd backend

# Maven 의존성 다운로드
mvn clean install

# Spring Boot 애플리케이션 실행
mvn spring-boot:run or BackendApplication.java 실행 
```

### 2. AI 서비스 실행
```bash
# 새 터미널 창에서
cd ai-service

# 가상환경 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# AI 서비스 실행
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Redis 실행 (선택사항)
```bash
# Windows: Redis 설치 후 redis-server 실행
# macOS: brew services start redis
# Linux: sudo systemctl start redis

# Redis 연결 테스트
redis-cli ping
```

### 4. 웹 접속
- **메인 페이지**: http://localhost:8080
- **AI 서비스 API**: http://localhost:8000/docs

## 👤 테스트 시나리오

### 1. 회원가입 및 로그인
1. **회원가입**
   - http://localhost:8080 접속
   - "회원가입" 클릭
   - 테스트 계정 생성: 자유롭게 

2. **로그인**
   - 생성한 계정으로 로그인
   - 메인 페이지 접속 확인

### 2. 데이터베이스 재초기화 (중요!)
회원가입 후 반드시 실행해야 함:
```bash
# init.sql 재실행
mysql -u diary_user -p rebuild_db < backend/src/main/resources/data/init.sql // 수동 초기화 해야함 
# 비밀번호: diary_password
```

### 3. 기능 테스트

#### 일기 작성 테스트
1. **일기 작성**
   - "일기 작성" 메뉴 클릭
   - 감정 선택 (😊, 😍, 😌, 😤, 😴)
   - 일기 내용 작성
   - 저장 버튼 클릭

2. **일기 목록 확인**
   - "일기 목록" 메뉴 클릭
   - 작성한 일기 확인
   - 감정 정보 표시 확인

#### AI 분석 테스트
1. **AI 분석 요청**
   - 일기 작성 후 "AI 분석" 버튼 클릭
   - 분석 결과 확인
   - 감정 분석 결과 확인

2. **채팅 기능**
   - "채팅" 메뉴 클릭
   - AI와 대화 테스트
   - 일기 관련 질문 테스트

#### 포인트 및 스탬프 테스트
1. **포인트 확인**
   - "마이페이지" 메뉴 클릭
   - 현재 포인트 확인 (초기 2000포인트)

2. **스탬프 구매**
   - "포인트샵" 메뉴 클릭
   - 스탬프 목록 확인
   - 원하는 스탬프 구매

3. **스탬프 적용**
   - 일기 작성 시 스탬프 적용
   - 적용된 스탬프 확인

#### 주간 리포트 테스트
1. **주간 리포트 확인**
   - "주간 리포트" 메뉴 클릭
   - 감정 차트 확인
   - 주간 피드백 확인

2. **과거 리포트 확인**
   - 다른 주차 리포트 확인
   - 감정 변화 추이 확인

## 🔧 문제 해결

### 1. 포트 충돌 문제
```bash
# 포트 사용 확인 (Windows)
netstat -ano | findstr :3306
netstat -ano | findstr :8080
netstat -ano | findstr :8000

# 포트 사용 확인 (Linux/Mac)
lsof -i :3306
lsof -i :8080
lsof -i :8000

# 사용 중인 프로세스 종료
# Windows: 작업 관리자에서 해당 프로세스 종료
# Linux/Mac: kill -9 [PID]
```

### 2. 데이터베이스 연결 문제
```bash
# MySQL 서비스 상태 확인
# Windows: 서비스 관리자에서 MySQL 확인
# macOS: brew services list | grep mysql
# Linux: sudo systemctl status mysql

# MySQL 연결 테스트
mysql -u diary_user -p rebuild_db

# 백엔드 애플리케이션 재시작
# Ctrl+C로 중지 후 다시 실행
mvn spring-boot:run
```

### 3. AI 서비스 연결 문제
```bash
# AI 서비스 의존성 재설치
cd ai-service
pip install -r requirements.txt

# ChromaDB 재초기화
python init_chromadb.py

# AI 서비스 재시작
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Java/Maven 문제
```bash
# Java 버전 확인
java -version

# Maven 버전 확인
mvn -version

# Maven 캐시 정리
mvn clean

# 의존성 재다운로드
mvn dependency:resolve
```

### 5. Python 가상환경 문제
```bash
# 가상환경 재생성
rm -rf venv
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 의존성 재설치
pip install -r requirements.txt
```

## 📊 테스트 체크리스트

### 초기 설정
- [ ] Java 21 설치 및 확인
- [ ] Python 3.9+ 설치 및 확인
- [ ] MySQL 8.0 설치 및 실행
- [ ] 프로젝트 다운로드 완료
- [ ] 환경 변수 설정 (.env 파일)
- [ ] 포트 충돌 확인

### 데이터베이스 설정
- [ ] MySQL 서비스 실행
- [ ] rebuild_db 데이터베이스 생성
- [ ] diary_user 계정 생성
- [ ] init.sql 실행 완료
- [ ] 초기 데이터 확인

### ChromaDB 설정
- [ ] Python 가상환경 생성 및 활성화
- [ ] AI 서비스 의존성 설치
- [ ] ChromaDB 초기화 완료
- [ ] 샘플 데이터 확인

### 서비스 실행
- [ ] 백엔드 서비스 실행 (8080 포트)
- [ ] AI 서비스 실행 (8000 포트)
- [ ] 웹 접속 확인 (http://localhost:8080)
- [ ] AI 서비스 접속 확인 (http://localhost:8000/docs)

### 기능 테스트
- [ ] 회원가입 완료
- [ ] 로그인 성공
- [ ] init.sql 재실행 완료
- [ ] 일기 작성 테스트
- [ ] AI 분석 테스트
- [ ] 포인트/스탬프 테스트
- [ ] 주간 리포트 테스트

## 📞 지원

### 로그 확인 방법
```bash
# 백엔드 로그 확인
# Spring Boot 콘솔에서 실시간 로그 확인

# AI 서비스 로그 확인
# uvicorn 콘솔에서 실시간 로그 확인
```

### 주요 파일 위치
- **데이터베이스 설정**: `backend/src/main/resources/application.yml`
- **초기 데이터**: `backend/src/main/resources/data/init.sql`
- **환경 변수**: `.env`
- **AI 서비스 설정**: `ai-service/app/main.py`
- **ChromaDB 데이터**: `ai-service/data/chroma_db/`

### 테스트 계정 정보
- **사용자명**: testuser
- **이메일**: test@example.com
- **비밀번호**: 1234
- **초기 포인트**: 2000포인트

## 🎯 주요 기능

### 백엔드 기능
- ✅ 사용자 관리 (회원가입/로그인)
- ✅ 일기 작성 및 관리
- ✅ 감정 분석 및 통계
- ✅ 포인트 시스템
- ✅ 스탬프 시스템
- ✅ 주간 리포트

### AI 서비스 기능
- ✅ 일기 내용 분석
- ✅ 감정 분석
- ✅ AI 조언 제공
- ✅ ChromaDB 기반 벡터 검색
- ✅ 실시간 채팅

### 데이터베이스
- ✅ MySQL: 사용자, 일기, 포인트, 스탬프 데이터
- ✅ ChromaDB: AI 분석용 벡터 데이터
- ✅ Redis: 캐시 및 세션 관리 (선택사항)

---

**⚠️ 중요**: 회원가입 후 반드시 `init.sql`을 재실행해야 모든 기능이 정상 작동합니다! 