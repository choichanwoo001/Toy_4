#!/bin/bash

# 색상 정의
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== 인생, 쓰다 - Docker 실행 스크립트 ===${NC}"

# 환경 변수 파일 확인
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠️  .env 파일이 없습니다. env.example을 복사합니다.${NC}"
    cp env.example .env
    echo -e "${YELLOW}⚠️  .env 파일에서 OPENAI_API_KEY를 설정해주세요.${NC}"
    exit 1
fi

# Docker 설치 확인
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker가 설치되어 있지 않습니다.${NC}"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}❌ Docker Compose가 설치되어 있지 않습니다.${NC}"
    exit 1
fi

# 기존 컨테이너 정리
echo -e "${YELLOW}🧹 기존 컨테이너를 정리합니다...${NC}"
docker-compose down

# 이미지 빌드
echo -e "${YELLOW}🔨 Docker 이미지를 빌드합니다...${NC}"
docker-compose build

# 서비스 시작
echo -e "${YELLOW}🚀 서비스를 시작합니다...${NC}"
docker-compose up -d

# 서비스 상태 확인
echo -e "${YELLOW}⏳ 서비스가 시작될 때까지 기다립니다...${NC}"
sleep 30

# 서비스 상태 확인
echo -e "${BLUE}📊 서비스 상태 확인:${NC}"
docker-compose ps

echo -e "${GREEN}✅ 모든 서비스가 시작되었습니다!${NC}"
echo -e "${BLUE}🌐 접속 URL:${NC}"
echo -e "  - 백엔드: ${GREEN}http://localhost:8080${NC}"
echo -e "  - AI 서비스: ${GREEN}http://localhost:8000${NC}"
echo -e "  - MySQL: ${GREEN}localhost:3306${NC}"
echo -e "  - Redis: ${GREEN}localhost:6379${NC}"

echo -e "${YELLOW}📝 로그 확인: docker-compose logs -f${NC}"
echo -e "${YELLOW}🛑 서비스 중지: docker-compose down${NC}" 