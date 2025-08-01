#!/usr/bin/env python3
"""
ChromaDB 초기화 스크립트
AI 서비스 시작 시 자동으로 실행되어 ChromaDB를 초기화합니다.
"""

import os
import sys
import chromadb
from chromadb.config import Settings
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_chromadb():
    """ChromaDB 초기화 및 기본 컬렉션 생성"""
    try:
        # ChromaDB 클라이언트 생성
        chroma_client = chromadb.PersistentClient(
            path="/app/data/chroma_db",
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )
        
        logger.info("ChromaDB 클라이언트 생성 완료")
        
        # 기본 컬렉션 생성 (이미 존재하면 무시)
        collections = chroma_client.list_collections()
        logger.info(f"기존 컬렉션: {[col.name for col in collections]}")
        
        # 일기 컬렉션 생성
        try:
            diary_collection = chroma_client.create_collection(
                name="diary_collection",
                metadata={"description": "사용자 일기 데이터"}
            )
            logger.info("일기 컬렉션 생성 완료")
        except Exception as e:
            if "already exists" in str(e):
                diary_collection = chroma_client.get_collection("diary_collection")
                logger.info("일기 컬렉션 이미 존재함")
            else:
                raise e
        
        # 조언 컬렉션 생성
        try:
            advice_collection = chroma_client.create_collection(
                name="advice_collection", 
                metadata={"description": "AI 조언 데이터"}
            )
            logger.info("조언 컬렉션 생성 완료")
        except Exception as e:
            if "already exists" in str(e):
                advice_collection = chroma_client.get_collection("advice_collection")
                logger.info("조언 컬렉션 이미 존재함")
            else:
                raise e
        
        # 인용구 컬렉션 생성
        try:
            quote_collection = chroma_client.create_collection(
                name="quote_collection",
                metadata={"description": "영감을 주는 인용구 데이터"}
            )
            logger.info("인용구 컬렉션 생성 완료")
        except Exception as e:
            if "already exists" in str(e):
                quote_collection = chroma_client.get_collection("quote_collection")
                logger.info("인용구 컬렉션 이미 존재함")
            else:
                raise e
        
        # 실제 데이터 파일들에서 데이터 삽입
        insert_real_data(diary_collection, advice_collection, quote_collection)
        
        logger.info("ChromaDB 초기화 완료")
        return True
        
    except Exception as e:
        logger.error(f"ChromaDB 초기화 실패: {e}")
        return False

def insert_real_data(diary_collection, advice_collection, quote_collection):
    """실제 데이터 파일들에서 데이터 삽입"""
    try:
        # data 폴더의 스크립트들을 실행하여 실제 데이터 삽입
        import subprocess
        
        # 현재 작업 디렉토리를 /app으로 변경
        os.chdir("/app")
        
        # 조언 데이터 초기화
        logger.info("조언 데이터 초기화 중...")
        try:
            subprocess.run([sys.executable, "data/init_advice_only.py"], 
                         check=True, capture_output=True, text=True)
            logger.info("조언 데이터 초기화 완료")
        except subprocess.CalledProcessError as e:
            logger.warning(f"조언 데이터 초기화 실패: {e}")
        
        # 인용구 데이터 초기화
        logger.info("인용구 데이터 초기화 중...")
        try:
            subprocess.run([sys.executable, "data/init_quotes_only.py"], 
                         check=True, capture_output=True, text=True)
            logger.info("인용구 데이터 초기화 완료")
        except subprocess.CalledProcessError as e:
            logger.warning(f"인용구 데이터 초기화 실패: {e}")
        
        # 과거 일기 데이터 초기화
        logger.info("과거 일기 데이터 초기화 중...")
        try:
            subprocess.run([sys.executable, "data/init_past_diaries_only.py"], 
                         check=True, capture_output=True, text=True)
            logger.info("과거 일기 데이터 초기화 완료")
        except subprocess.CalledProcessError as e:
            logger.warning(f"과거 일기 데이터 초기화 실패: {e}")
            
    except Exception as e:
        logger.error(f"실제 데이터 삽입 실패: {e}")

if __name__ == "__main__":
    success = init_chromadb()
    if success:
        logger.info("ChromaDB 초기화 성공")
        sys.exit(0)
    else:
        logger.error("ChromaDB 초기화 실패")
        sys.exit(1) 