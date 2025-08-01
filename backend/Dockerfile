FROM openjdk:21-jdk-slim

WORKDIR /app

# Maven 설치
RUN apt-get update && \
    apt-get install -y maven && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# pom.xml 복사
COPY pom.xml .

# Maven 의존성 다운로드
RUN mvn dependency:go-offline -B

# 소스 코드 복사
COPY src src

# 애플리케이션 빌드
RUN mvn package -DskipTests

# 실행 가능한 JAR 파일만 복사
RUN cp target/*.jar app.jar

# 포트 노출
EXPOSE 8080

# 애플리케이션 실행
ENTRYPOINT ["java", "-jar", "app.jar"] 