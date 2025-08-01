#!/bin/bash

# 색상 정의
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== 인생, 쓰다 - Docker 서비스 중지 ===${NC}"

# Docker Compose 설치 확인
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}❌ Docker Compose가 설치되어 있지 않습니다.${NC}"
    exit 1
fi

# 서비스 중지
echo -e "${YELLOW}🛑 서비스를 중지합니다...${NC}"
docker-compose down

# 볼륨 삭제 (선택사항)
read -p "볼륨도 함께 삭제하시겠습니까? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}🗑️  볼륨을 삭제합니다...${NC}"
    docker-compose down -v
    echo -e "${GREEN}✅ 볼륨이 삭제되었습니다.${NC}"
else
    echo -e "${GREEN}✅ 서비스가 중지되었습니다. (볼륨은 유지)${NC}"
fi

echo -e "${BLUE}📊 현재 실행 중인 컨테이너:${NC}"
docker ps 