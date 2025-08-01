"""
조언 데이터만 초기화하는 스크립트
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.vector_db import VectorDatabase
from data.sample_advice_data import SAMPLE_ADVICE_DATA

def init_advice_only():
    """조언 데이터만 초기화"""
    print("📝 조언 데이터만 초기화 시작...")
    
    # 벡터 데이터베이스 초기화
    vector_db = VectorDatabase()
    vector_db.initialize()
    
    # 조언 컬렉션만 리셋
    print("🗑️ 조언 컬렉션 삭제 중...")
    vector_db.reset_advice_collection()
    
    # 조언 데이터만 추가
    print("📝 조언 데이터 추가 중...")
    success_count = 0
    total_count = len(SAMPLE_ADVICE_DATA)
    
    for advice in SAMPLE_ADVICE_DATA:
        if vector_db.add_advice(advice):
            success_count += 1
        else:
            print(f"❌ 조언 데이터 추가 실패: {advice.get('content', '')[:50]}...")
    
    print(f"✅ 조언 데이터 초기화 완료!")
    print(f"📊 총 {total_count}개 중 {success_count}개 추가 성공")
    
    # 데이터베이스 정보 출력
    info = vector_db.get_collection_info()
    print(f"📈 현재 조언 컬렉션 상태:")
    print(f"   - 컬렉션: {info.get('name', 'N/A')}")
    print(f"   - 데이터 수: {info.get('count', 0)}")
    print(f"   - 임베딩 모델: {info.get('embedding_model', 'N/A')}")

if __name__ == "__main__":
    init_advice_only() 