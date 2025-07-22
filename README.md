# Rebuild Project

Spring Boot, MySQL, Thymeleaf를 사용한 웹 애플리케이션 프로젝트입니다.

## 프로젝트 구조

```
rebuild/
├── .gitignore         # 프로젝트 전체 gitignore
├── README.md          # 프로젝트 전체 설명
├── backend/           # Spring Boot 백엔드 애플리케이션
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   └── com/example/backend/
│   │   │   │       ├── BackendApplication.java
│   │   │   │       ├── controller/
│   │   │   │       │   └── HomeController.java
│   │   │   │       ├── service/
│   │   │   │       │   └── TestService.java
│   │   │   │       ├── repository/
│   │   │   │       │   └── TestRepository.java
│   │   │   │       └── entity/
│   │   │   │           └── TestEntity.java
│   │   │   └── resources/
│   │   │       ├── application.yml
│   │   │       └── templates/
│   │   │           └── home.html
│   │   └── test/
│   ├── .env           # 환경변수 (gitignore에 포함)
│   ├── env.example    # 환경변수 예시
│   ├── .gitignore     # 백엔드 전용 gitignore
│   ├── README.md      # 백엔드 설명
│   └── pom.xml
└── ai-service/        # AI 서비스 (향후 개발 예정)
    └── README.md
```

## 기술 스택

### Backend
- **Spring Boot**: 3.2.0
- **Java**: 21
- **Jakarta EE**: 10
- **MySQL**: 8.2.0
- **Thymeleaf**: 템플릿 엔진
- **JPA/Hibernate**: ORM
- **Maven**: 빌드 도구

## 실행 방법

### 사전 요구사항
- Java 21 이상
- MySQL 8.0 이상
- Maven

### 데이터베이스 설정
1. MySQL에서 `rebuild_db` 데이터베이스 생성
2. `backend/env.example`을 참고하여 `backend/.env` 파일 생성
3. `.env` 파일에서 실제 MySQL 비밀번호 설정

### 애플리케이션 실행
```bash
cd backend
mvn spring-boot:run
```

애플리케이션이 실행되면 `http://localhost:8080`에서 확인할 수 있습니다.

## 개발 환경 설정

### IDE 설정
- IntelliJ IDEA 또는 Eclipse STS 권장
- Spring Boot DevTools 활성화 (선택사항)

### 데이터베이스 설정
- MySQL 서버 실행
- 데이터베이스 생성: `CREATE DATABASE rebuild_db;`
- 사용자 권한 설정 (필요시) 