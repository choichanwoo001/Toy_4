#!/usr/bin/env python3
"""
RAG 에이전트 데모 스크립트
실제 사용자 입력으로 RAG 에이전트를 테스트할 수 있습니다.
"""

import logging
import sys
import os

# 프로젝트 루트를 Python 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from app.services.rag_agent import RAGAgent
from app.services.data_loader import DataLoader

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def setup_test_data():
    """테스트 데이터 설정"""
    print("=== 테스트 데이터 설정 중 ===")
    
    data_loader = DataLoader()
    
    # 기존 데이터 확인
    collection_info = data_loader.get_collection_info()
    print(f"현재 컬렉션 정보: {collection_info}")
    
    # 데이터가 충분하지 않으면 새로 생성
    if collection_info.get('count', 0) < 10:
        print("샘플 데이터 생성 중...")
        sample_entries = data_loader.generate_sample_diary_data(30)
        success = data_loader.load_data_to_chroma(sample_entries)
        
        if success:
            print(f"✅ {len(sample_entries)}개 샘플 데이터가 성공적으로 로드되었습니다.")
        else:
            print("❌ 데이터 로드에 실패했습니다.")
            return False
    else:
        print(f"✅ 기존 데이터 {collection_info['count']}개가 있습니다.")
    
    return True

def test_rag_agent():
    """RAG 에이전트 테스트"""
    print("\n=== RAG 에이전트 테스트 ===")
    
    # RAG 에이전트 초기화
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
            # RAG 처리
            response = rag_agent.process_query(query)
            
            # 결과 출력
            print(f"분석 결과:")
            print(f"  신뢰도: {response.confidence_score:.3f}")
            print(f"  관련 엔트리 수: {len(response.related_entries)}")
            
            if response.related_entries:
                print("  관련 엔트리 (상위 3개):")
                for j, entry in enumerate(response.related_entries[:3], 1):
                    print(f"    {j}. {entry.content[:60]}...")
                    print(f"       유사도: {entry.similarity_score:.3f}, 감정: {entry.metadata.get('emotion', 'N/A')}")
            
            print(f"\n  분석 텍스트:")
            print(f"  {response.analysis}")
            
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            logger.error(f"쿼리 처리 중 오류: {e}")

def interactive_test():
    """대화형 테스트"""
    print("\n=== 대화형 테스트 ===")
    print("사용자 입력을 입력하세요. 'quit'를 입력하면 종료됩니다.")
    
    rag_agent = RAGAgent()
    
    while True:
        try:
            user_input = input("\n사용자 입력: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '종료']:
                print("테스트를 종료합니다.")
                break
            
            if not user_input:
                continue
            
            print("처리 중...")
            response = rag_agent.process_query(user_input)
            
            print(f"\n=== RAG 응답 ===")
            print(f"신뢰도: {response.confidence_score:.3f}")
            print(f"관련 엔트리 수: {len(response.related_entries)}")
            
            if response.related_entries:
                print("\n관련 엔트리:")
                for i, entry in enumerate(response.related_entries, 1):
                    print(f"{i}. {entry.content}")
                    print(f"   유사도: {entry.similarity_score:.3f}, 감정: {entry.metadata.get('emotion', 'N/A')}")
            
            print(f"\n분석:")
            print(response.analysis)
            
        except KeyboardInterrupt:
            print("\n테스트를 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            logger.error(f"대화형 테스트 중 오류: {e}")

def main():
    """메인 함수"""
    print("🚀 RAG 에이전트 데모 시작")
    
    # 1. 테스트 데이터 설정
    if not setup_test_data():
        print("❌ 테스트 데이터 설정에 실패했습니다.")
        return
    
    # 2. 자동 테스트
    test_rag_agent()
    
    # 3. 대화형 테스트
    try:
        interactive_test()
    except KeyboardInterrupt:
        print("\n프로그램이 중단되었습니다.")
    
    print("✅ RAG 에이전트 데모 완료")

if __name__ == "__main__":
    main() 