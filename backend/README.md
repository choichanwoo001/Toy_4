# Backend Project

Spring Boot 3.2.0, Java 21, MySQL, Thymeleaf를 사용한 백엔드 프로젝트입니다.

## 환경 설정

### 1. 환경변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 내용을 입력하세요:

```bash
# Database Configuration
DB_NAME=rebuild_db
DB_USERNAME=root
DB_PASSWORD=your_actual_mysql_password

# Server Configuration
SERVER_PORT=8080

# Application Configuration
SPRING_PROFILES_ACTIVE=dev
```

### 2. 데이터베이스 설정

MySQL에서 다음 명령을 실행하여 데이터베이스를 생성하세요:

```sql
CREATE DATABASE rebuild_db;
```

### 3. 애플리케이션 실행

```bash
# Maven으로 실행
mvn spring-boot:run

# 또는 JAR 파일로 실행
mvn clean package
java -jar target/backend-0.0.1-SNAPSHOT.jar
```

## 프로젝트 구조

```
backend/
├── src/
│   ├── main/
│   │   ├── java/com/example/backend/
│   │   │   ├── BackendApplication.java
│   │   │   ├── controller/
│   │   │   │   └── HomeController.java
│   │   │   ├── service/
│   │   │   │   └── TestService.java
│   │   │   ├── repository/
│   │   │   │   └── TestRepository.java
│   │   │   └── entity/
│   │   │       └── TestEntity.java
│   │   └── resources/
│   │       ├── application.yml
│   │       └── templates/
│   │           └── home.html
│   └── test/
├── .env.example
├── .gitignore
└── pom.xml
```

## 주요 기능

- Hello World 테스트
- 데이터베이스 연결 테스트
- 메시지 저장 및 조회 기능
- Thymeleaf 템플릿 렌더링

## 접속 URL

- 메인 페이지: http://localhost:8080
- 테스트 페이지: http://localhost:8080 (테스트 섹션 포함)

## 주의사항

- `.env` 파일은 절대 Git에 커밋하지 마세요
- 실제 MySQL 비밀번호를 사용하세요
- 환경변수는 `application.yml`에서 관리됩니다 