#!/usr/bin/env python3
"""
RAG 검색 정보 표시 기능 테스트 스크립트

이 스크립트는 챗봇의 RAG 검색 과정과 유사도 정보가 올바르게 표시되는지 테스트합니다.
"""

import requests
import json
import time

def test_rag_display():
    """RAG 검색 정보 표시 기능을 테스트합니다."""
    
    # 테스트할 메시지들 (다양한 복잡도와 감정을 포함)
    test_messages = [
        "오늘 회사에서 상사한테 혼났어요. 너무 힘들고 우울해요.",
        "친구와 다퉈서 기분이 안 좋아요. 어떻게 화해할 수 있을까요?",
        "새로운 직장에 적응하는데 어려움을 겪고 있어요. 조언해주세요.",
        "가족과의 관계가 복잡해져서 고민이에요.",
        "자신감이 부족해서 새로운 도전을 하기 어려워요."
    ]
    
    print("🔍 RAG 검색 정보 표시 기능 테스트 시작")
    print("=" * 50)
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n📝 테스트 {i}: {message}")
        print("-" * 40)
        
        try:
            # AI 서비스에 직접 요청
            response = requests.post(
                "http://localhost:8000/api/v1/conversation-manager/chat-advanced",
                json={
                    "message": message,
                    "user_id": "test_user_01"
                },
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                
                print(f"✅ 응답 성공")
                print(f"📄 응답: {data.get('response', 'N/A')[:100]}...")
                print(f"🎯 의도: {data.get('intent', 'N/A')}")
                print(f"🔍 RAG 사용: {data.get('rag_used', False)}")
                
                if data.get('rag_used'):
                    print(f"🔎 검색 쿼리: {data.get('search_query', 'N/A')}")
                    print(f"🎭 검색 필터: {data.get('search_filters', {})}")
                    print(f"📊 검색 통계: {data.get('total_searched', 0)}개 중 {data.get('total_filtered', 0)}개 선택")
                    print(f"📈 유사도 점수: {data.get('similarity_scores', [])}")
                    
                    # 유사도 점수 분석
                    scores = data.get('similarity_scores', [])
                    if scores:
                        avg_score = sum(scores) / len(scores)
                        max_score = max(scores)
                        min_score = min(scores)
                        print(f"📊 유사도 분석: 평균={avg_score:.3f}, 최고={max_score:.3f}, 최저={min_score:.3f}")
                else:
                    print("ℹ️ RAG를 사용하지 않았습니다.")
                
            else:
                print(f"❌ 응답 실패: {response.status_code}")
                print(f"오류: {response.text}")
                
        except Exception as e:
            print(f"❌ 요청 실패: {e}")
        
        # 요청 간 간격
        time.sleep(1)
    
    print("\n" + "=" * 50)
    print("🎉 테스트 완료!")

if __name__ == "__main__":
    test_rag_display() 