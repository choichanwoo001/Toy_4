#!/usr/bin/env python3
"""
일기 분석 기능 테스트 스크립트
"""

import asyncio
import sys
import os

# 프로젝트 루트를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.diary_analyzer import DiaryAnalyzer

async def test_diary_analysis():
    """일기 분석 기능 테스트"""
    
    print("=== 일기 분석 기능 테스트 ===\n")
    
    # DiaryAnalyzer 초기화
    analyzer = DiaryAnalyzer()
    
    # 테스트용 일기 데이터
    test_diary = """
    오늘은 정말 힘든 하루였다. 회사에서 프로젝트 마감일이 다가와서 스트레스를 받았어. 
    하지만 팀원들과 함께 문제를 해결하면서 뿌듯함도 느꼈다. 
    특히 민수 씨가 도와준 덕분에 어려운 부분을 잘 해결할 수 있었다.
    """
    
    print("📝 테스트 일기:")
    print(test_diary.strip())
    print("\n" + "="*50 + "\n")
    
    try:
        # 일기 분석 실행
        result = await analyzer.analyze_diary("test_user_123", test_diary.strip())
        
        print("✅ 분석 완료!")
        print(f"\n📝 전처리된 일기:")
        print(result.processed_diary)
        
        print(f"\n🔍 청크 분할 결과 ({len(result.chunks)}개):")
        for i, chunk in enumerate(result.chunks, 1):
            print(f"{i}. {chunk}")
        
        if result.advice:
            print(f"\n💡 AI 조언:")
            print(result.advice)
        
        print(f"\n💬 AI 코멘트:")
        print(result.comment)
        
        if result.quote:
            print(f"\n📖 관련 인용문:")
            print(result.quote)
        
        if result.emotion_keywords:
            print(f"\n🏷️ 감정 키워드:")
            print(", ".join(result.emotion_keywords))
        
        if result.similar_past_diaries:
            print(f"\n📚 유사한 과거 일기 ({len(result.similar_past_diaries)}개):")
            for i, diary in enumerate(result.similar_past_diaries, 1):
                print(f"{i}. {diary}")
        
        print("\n" + "="*50)
        print("✅ 모든 테스트가 성공적으로 완료되었습니다!")
        
    except Exception as e:
        print(f"❌ 테스트 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()

def test_preprocessing():
    """전처리 기능 테스트"""
    print("\n=== 전처리 기능 테스트 ===\n")
    
    analyzer = DiaryAnalyzer()
    
    raw_text = "오늘은 정말 힘들었어. 회사에서 일이 많아서 스트레스 받았고, 집에 와서도 계속 생각이 나서 잠을 잘 못 잤어."
    
    print("📝 원본 텍스트:")
    print(raw_text)
    
    processed = analyzer.preprocess_diary(raw_text)
    print(f"\n✅ 전처리 결과:")
    print(processed)

def test_chunking():
    """청크 분할 기능 테스트"""
    print("\n=== 청크 분할 기능 테스트 ===\n")
    
    analyzer = DiaryAnalyzer()
    
    diary_text = """
    오늘은 정말 특별한 하루였다. 아침에 일찍 일어나서 산책을 다녀왔는데, 
    새벽 공기의 상쾌함이 정말 좋았다. 그 다음에 카페에서 책을 읽었는데, 
    오랫동안 읽고 싶었던 소설을 마침내 완독할 수 있었다. 
    점심에는 친구와 만나서 맛있는 음식을 먹었고, 오후에는 영화를 보러 갔다. 
    저녁에는 집에 돌아와서 오늘 하루를 정리하며 감사한 마음이 들었다.
    """
    
    print("📝 원본 일기:")
    print(diary_text.strip())
    
    chunks = analyzer.chunk_diary_by_meaning(diary_text.strip())
    print(f"\n✅ 청크 분할 결과 ({len(chunks)}개):")
    for i, chunk in enumerate(chunks, 1):
        print(f"{i}. {chunk}")

if __name__ == "__main__":
    print("🚀 일기 분석 기능 테스트 시작\n")
    
    # 개별 기능 테스트
    test_preprocessing()
    test_chunking()
    
    # 전체 분석 테스트
    asyncio.run(test_diary_analysis()) 