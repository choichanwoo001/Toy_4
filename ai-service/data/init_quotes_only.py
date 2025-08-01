"""
명언 데이터만 초기화하는 스크립트
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.vector_db import VectorDatabase
from data.sample_advice_data import QUOTES_DATA

def init_quotes_only():
    """명언 데이터만 초기화"""
    print("💬 명언 데이터만 초기화 시작...")
    
    # 벡터 데이터베이스 초기화
    vector_db = VectorDatabase()
    vector_db.initialize()
    
    # 명언 컬렉션만 리셋
    print("🗑️ 명언 컬렉션 삭제 중...")
    vector_db.reset_quotes_collection()
    
    # 명언 데이터만 추가
    print("💬 명언 데이터 추가 중...")
    success_count = 0
    total_count = len(QUOTES_DATA)
    
    for quote in QUOTES_DATA:
        if vector_db.add_quote(quote):
            success_count += 1
        else:
            print(f"❌ 명언 데이터 추가 실패: {quote.get('document', '')[:50]}...")
    
    print(f"✅ 명언 데이터 초기화 완료!")
    print(f"📊 총 {total_count}개 중 {success_count}개 추가 성공")
    
    # 명언 컬렉션 정보 출력
    quotes_info = vector_db.quotes_collection.count()
    print(f"📈 현재 명언 컬렉션 상태:")
    print(f"   - 컬렉션: {vector_db.config.QUOTES_COLLECTION_NAME}")
    print(f"   - 데이터 수: {quotes_info}")
    print(f"   - 임베딩 모델: {vector_db.config.EMBEDDING_MODEL}")

if __name__ == "__main__":
    init_quotes_only() 