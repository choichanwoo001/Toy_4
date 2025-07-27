import pytest
import logging
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta
import tempfile
import shutil
import os

from app.services.rag_agent import RAGAgent
from app.services.data_loader import DataLoader
from app.models.diary import DiarySearchQuery, SearchResult, RAGResponse

# 로깅 설정
logging.basicConfig(level=logging.INFO)

class TestRAGAgent:
    @pytest.fixture
    def rag_agent(self):
        """RAG 에이전트 인스턴스 생성"""
        return RAGAgent()
    
    @pytest.fixture
    def data_loader(self):
        """데이터 로더 인스턴스 생성"""
        return DataLoader()
    
    def test_emotion_extraction(self, rag_agent):
        """감정 추출 테스트"""
        # 우울한 감정 테스트
        result = rag_agent._extract_emotion("요즘 계속 우울한 기분이 들고 있다")
        assert result == "우울"
        
        # 기쁜 감정 테스트
        result = rag_agent._extract_emotion("오늘 정말 기뻤다")
        assert result == "기쁨"
        
        # 감정이 없는 경우
        result = rag_agent._extract_emotion("오늘 날씨가 좋다")
        assert result is None
    
    def test_situation_extraction(self, rag_agent):
        """상황 추출 테스트"""
        # 업무 상황 테스트
        result = rag_agent._extract_situation("회의에서 내 의견이 무시당했다")
        assert result == "업무"
        
        # 가족 상황 테스트
        result = rag_agent._extract_situation("부모님과 다퉜다")
        assert result == "가족"
        
        # 상황이 없는 경우
        result = rag_agent._extract_situation("오늘 날씨가 좋다")
        assert result is None
    
    def test_time_context_extraction(self, rag_agent):
        """시간 컨텍스트 추출 테스트"""
        # 이번 주 테스트
        result = rag_agent._extract_time_context("이번 주에 계속 우울했다")
        assert result == "이번_주"
        
        # 오늘 테스트
        result = rag_agent._extract_time_context("오늘 기분이 좋다")
        assert result == "오늘"
        
        # 시간 컨텍스트가 없는 경우
        result = rag_agent._extract_time_context("기분이 좋다")
        assert result is None
    
    def test_user_input_analysis(self, rag_agent):
        """사용자 입력 분석 테스트"""
        user_input = "요즘 계속 우울한데 이번 주에 회사에서 힘들었다"
        
        result = rag_agent.analyze_user_input(user_input)
        
        assert isinstance(result, DiarySearchQuery)
        assert result.user_utterance == user_input
        assert result.inferred_emotion == "우울"
        assert result.inferred_situation == "업무"
        assert result.time_context == "이번_주"
    
    def test_search_query_generation(self, rag_agent):
        """검색 쿼리 생성 테스트"""
        parsed_query = DiarySearchQuery(
            user_utterance="요즘 우울하다",
            inferred_emotion="우울",
            inferred_situation="업무",
            time_context="이번_주"
        )
        
        query_keywords, where_filter = rag_agent.generate_search_query(parsed_query)
        
        # 키워드에 감정 키워드가 포함되어야 함
        assert "우울" in query_keywords
        assert "슬픔" in query_keywords
        
        # 필터에 상황과 시간이 포함되어야 함
        assert where_filter["context"] == "업무"
        assert "date" in where_filter
    
    @pytest.mark.integration
    def test_full_rag_pipeline(self, rag_agent, data_loader):
        """전체 RAG 파이프라인 통합 테스트"""
        # 임시 디렉토리 사용
        with tempfile.TemporaryDirectory() as temp_dir:
            # ChromaDB 경로를 임시 디렉토리로 변경
            original_persist_dir = "./chroma_db"
            temp_persist_dir = os.path.join(temp_dir, "chroma_db")
            
            try:
                # 1. 샘플 데이터 생성 및 로드
                sample_entries = data_loader.generate_sample_diary_data(20)
                success = data_loader.load_data_to_chroma(sample_entries)
                assert success is True
                
                # 2. RAG 쿼리 처리
                user_input = "요즘 계속 우울한데 이번 주에 내가 뭐 때문에 그런지 모르겠어"
                
                response = rag_agent.process_query(user_input)
                
                # 3. 응답 검증
                assert isinstance(response, RAGResponse)
                assert response.analysis is not None
                assert len(response.analysis) > 0
                assert 0.0 <= response.confidence_score <= 1.0
                
                print(f"\n=== RAG 응답 테스트 결과 ===")
                print(f"사용자 입력: {user_input}")
                print(f"분석: {response.analysis}")
                print(f"신뢰도: {response.confidence_score}")
                print(f"관련 엔트리 수: {len(response.related_entries)}")
                
                if response.related_entries:
                    print("관련 엔트리:")
                    for i, entry in enumerate(response.related_entries[:3]):
                        print(f"  {i+1}. {entry.content[:50]}... (유사도: {entry.similarity_score:.3f})")
                        
            except Exception as e:
                pytest.fail(f"통합 테스트 실패: {e}")
    
    def test_confidence_calculation(self, rag_agent):
        """신뢰도 계산 테스트"""
        # 빈 결과
        confidence = rag_agent._calculate_confidence([])
        assert confidence == 0.0
        
        # 높은 유사도의 결과
        high_similarity_entries = [
            SearchResult(content="test1", similarity_score=0.9, metadata={}),
            SearchResult(content="test2", similarity_score=0.8, metadata={})
        ]
        confidence = rag_agent._calculate_confidence(high_similarity_entries)
        assert confidence > 0.6
        
        # 낮은 유사도의 결과
        low_similarity_entries = [
            SearchResult(content="test1", similarity_score=0.3, metadata={}),
            SearchResult(content="test2", similarity_score=0.2, metadata={})
        ]
        confidence = rag_agent._calculate_confidence(low_similarity_entries)
        assert confidence < 0.5

if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 