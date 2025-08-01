#!/bin/bash

# AI 서비스 시작 스크립트
# ChromaDB 초기화 후 FastAPI 서버 시작

echo "=== AI 서비스 시작 ==="

# ChromaDB 초기화
echo "ChromaDB 초기화 중..."
python init_chromadb.py

if [ $? -eq 0 ]; then
    echo "ChromaDB 초기화 완료"
else
    echo "ChromaDB 초기화 실패, 하지만 서버는 계속 시작합니다."
fi

# FastAPI 서버 시작
echo "FastAPI 서버 시작 중..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload 