"""
과거 일기 데이터만 초기화하는 스크립트
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.vector_db import VectorDatabase
from data.sample_advice_data import SAMPLE_PAST_DIARY_DATA

def init_past_diaries_only():
    """과거 일기 데이터만 초기화"""
    print("📖 과거 일기 데이터만 초기화 시작...")
    
    # 벡터 데이터베이스 초기화
    vector_db = VectorDatabase()
    vector_db.initialize()
    
    # 과거 일기 컬렉션만 리셋
    print("🗑️ 과거 일기 컬렉션 삭제 중...")
    vector_db.reset_past_diaries_collection()
    
    # 과거 일기 데이터만 추가
    print("📖 과거 일기 데이터 추가 중...")
    success_count = 0
    total_count = len(SAMPLE_PAST_DIARY_DATA)
    
    for diary in SAMPLE_PAST_DIARY_DATA:
        if vector_db.add_past_diary(diary):
            success_count += 1
        else:
            print(f"❌ 과거 일기 데이터 추가 실패: {diary.get('document', '')[:50]}...")
    
    print(f"✅ 과거 일기 데이터 초기화 완료!")
    print(f"📊 총 {total_count}개 중 {success_count}개 추가 성공")
    
    # 과거 일기 컬렉션 정보 출력
    diaries_info = vector_db.past_diaries_collection.count()
    print(f"📈 현재 과거 일기 컬렉션 상태:")
    print(f"   - 컬렉션: {vector_db.config.PAST_DIARIES_COLLECTION_NAME}")
    print(f"   - 데이터 수: {diaries_info}")
    print(f"   - 임베딩 모델: {vector_db.config.EMBEDDING_MODEL}")

if __name__ == "__main__":
    init_past_diaries_only() 