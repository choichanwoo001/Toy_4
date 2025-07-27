#!/usr/bin/env python3
"""
RAG 에이전트 간단 데모 스크립트
ChromaDB 없이도 기본 기능을 테스트할 수 있습니다.
"""

import sys
import os
import logging

# 프로젝트 루트를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from app.services.rag_agent import RAGAgent
from app.models.diary import DiarySearchQuery

# 로깅 설정
logging.basicConfig(level=logging.INFO)

def test_basic_functions():
    """기본 RAG 기능 테스트 (ChromaDB 없이)"""
    print("=== RAG 에이전트 기본 기능 테스트 ===")
    
    # RAG 에이전트 초기화 (ChromaDB는 모킹됨)
    rag_agent = RAGAgent()
    
    # 테스트 쿼리들
    test_queries = [
        "요즘 계속 우울한데 이번 주에 내가 뭐 때문에 그런지 모르겠어",
        "오늘 회의에서 내 의견이 무시당한 것 같아서 속상했다",
        "친구들과 만나기로 했는데 갑자기 기분이 안 좋아져서 취소했다",
        "오늘 프로젝트가 성공적으로 완료되어서 정말 기뻤다",
        "동료가 내 일을 방해해서 정말 화가 났다",
        "내일 중요한 발표가 있어서 긴장된다",
        "오늘은 날씨가 좋아서 산책을 다녀왔다"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n--- 테스트 쿼리 {i} ---")
        print(f"사용자 입력: {query}")
        
        try:
            # 1. 사용자 입력 분석
            parsed_query = rag_agent.analyze_user_input(query)
            print(f"분석 결과:")
            print(f"  감정: {parsed_query.inferred_emotion}")
            print(f"  상황: {parsed_query.inferred_situation}")
            print(f"  시간: {parsed_query.time_context}")
            
            # 2. 검색 쿼리 생성
            query_keywords, where_filter = rag_agent.generate_search_query(parsed_query)
            print(f"검색 키워드: {query_keywords[:5]}...")  # 상위 5개만 표시
            print(f"필터 조건: {where_filter}")
            
            # 3. 신뢰도 계산 테스트
            test_entries = [
                {"content": "테스트 일기 1", "similarity": 0.8, "metadata": {"emotion": "우울"}},
                {"content": "테스트 일기 2", "similarity": 0.6, "metadata": {"emotion": "우울"}}
            ]
            
            from app.models.diary import SearchResult
            search_results = [
                SearchResult(
                    content=entry["content"],
                    similarity_score=entry["similarity"],
                    metadata=entry["metadata"]
                )
                for entry in test_entries
            ]
            
            confidence = rag_agent._calculate_confidence(search_results)
            print(f"신뢰도 점수: {confidence:.3f}")
            
            # 4. 분석 텍스트 생성
            analysis = rag_agent._generate_analysis_text(query, "테스트 컨텍스트", search_results)
            print(f"분석 텍스트: {analysis[:100]}...")
            
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            import traceback
            traceback.print_exc()

def test_emotion_extraction():
    """감정 추출 기능 상세 테스트"""
    print("\n=== 감정 추출 기능 테스트 ===")
    
    rag_agent = RAGAgent()
    
    emotion_test_cases = [
        ("요즘 계속 우울하다", "우울"),
        ("오늘 정말 기뻤다", "기쁨"),
        ("동료가 내 일을 방해해서 화가 났다", "화남"),
        ("내일 발표가 있어서 불안하다", "불안"),
        ("오늘은 평화로웠다", "평온"),
        ("오늘 날씨가 좋다", None)  # 감정 없음
    ]
    
    for text, expected_emotion in emotion_test_cases:
        result = rag_agent._extract_emotion(text)
        status = "✅" if result == expected_emotion else "❌"
        print(f"{status} '{text}' -> {result} (예상: {expected_emotion})")

def test_situation_extraction():
    """상황 추출 기능 상세 테스트"""
    print("\n=== 상황 추출 기능 테스트 ===")
    
    rag_agent = RAGAgent()
    
    situation_test_cases = [
        ("회의에서 내 의견이 무시당했다", "업무"),
        ("부모님과 다퉜다", "가족"),
        ("친구들과 만났다", "친구"),
        ("건강검진을 받았다", "건강"),
        ("오늘 날씨가 좋다", None)  # 상황 없음
    ]
    
    for text, expected_situation in situation_test_cases:
        result = rag_agent._extract_situation(text)
        status = "✅" if result == expected_situation else "❌"
        print(f"{status} '{text}' -> {result} (예상: {expected_situation})")

def test_time_context_extraction():
    """시간 컨텍스트 추출 기능 상세 테스트"""
    print("\n=== 시간 컨텍스트 추출 기능 테스트 ===")
    
    rag_agent = RAGAgent()
    
    time_test_cases = [
        ("이번 주에 계속 우울했다", "이번_주"),
        ("오늘 기분이 좋다", "오늘"),
        ("어제 일이 많았다", "어제"),
        ("기분이 좋다", None)  # 시간 없음
    ]
    
    for text, expected_time in time_test_cases:
        result = rag_agent._extract_time_context(text)
        status = "✅" if result == expected_time else "❌"
        print(f"{status} '{text}' -> {result} (예상: {expected_time})")

def main():
    """메인 함수"""
    print("🚀 RAG 에이전트 간단 데모 시작")
    
    try:
        # 1. 감정 추출 테스트
        test_emotion_extraction()
        
        # 2. 상황 추출 테스트
        test_situation_extraction()
        
        # 3. 시간 컨텍스트 추출 테스트
        test_time_context_extraction()
        
        # 4. 기본 기능 통합 테스트
        test_basic_functions()
        
        print("\n✅ 모든 테스트가 완료되었습니다!")
        
    except Exception as e:
        print(f"❌ 데모 실행 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 