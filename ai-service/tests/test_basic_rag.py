import pytest
import logging
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta

from app.services.rag_agent import RAGAgent
from app.models.diary import DiarySearchQuery, SearchResult, RAGResponse

# 로깅 설정
logging.basicConfig(level=logging.INFO)

class TestBasicRAG:
    """ChromaDB 없이 테스트할 수 있는 기본 RAG 기능"""
    
    @pytest.fixture
    def rag_agent(self):
        """RAG 에이전트 인스턴스 생성 (ChromaDB 모킹)"""
        with patch('app.services.rag_agent.ChromaClient') as mock_chroma:
            # ChromaDB 클라이언트 모킹
            mock_client = MagicMock()
            mock_collection = MagicMock()
            
            # 검색 결과 모킹
            mock_collection.query.return_value = {
                "documents": [["오늘 회의에서 내 의견이 무시당한 것 같아서 속상했다."]],
                "embeddings": [[0.1, 0.2, 0.3, 0.4, 0.5]],
                "metadatas": [{"date": "2024-11-20", "emotion": "우울", "context": "업무"}]
            }
            mock_collection.count.return_value = 1
            
            mock_client.get_collection.return_value = mock_collection
            mock_client.create_collection.return_value = mock_collection
            
            mock_chroma.return_value = mock_client
            
            return RAGAgent()
    
    def test_emotion_extraction(self, rag_agent):
        """감정 추출 테스트"""
        # 우울한 감정 테스트
        result = rag_agent._extract_emotion("요즘 계속 우울한 기분이 들고 있다")
        assert result == "우울"
        
        # 기쁜 감정 테스트
        result = rag_agent._extract_emotion("오늘 정말 기뻤다")
        assert result == "기쁨"
        
        # 화난 감정 테스트
        result = rag_agent._extract_emotion("동료가 내 일을 방해해서 화가 났다")
        assert result == "화남"
        
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
        
        # 친구 상황 테스트
        result = rag_agent._extract_situation("친구들과 만났다")
        assert result == "친구"
        
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
        
        # 어제 테스트
        result = rag_agent._extract_time_context("어제 일이 많았다")
        assert result == "어제"
        
        # 시간 컨텍스트가 없는 경우
        result = rag_agent._extract_time_context("기분이 좋다")
        assert result is None
    
    def test_user_input_analysis(self, rag_agent):
        """사용자 입력 분석 테스트"""
        test_cases = [
            {
                "input": "요즘 계속 우울한데 이번 주에 회사에서 힘들었다",
                "expected_emotion": "우울",
                "expected_situation": "업무",
                "expected_time": "이번_주"
            },
            {
                "input": "오늘 친구들과 만나서 정말 기뻤다",
                "expected_emotion": "기쁨",
                "expected_situation": "친구",
                "expected_time": "오늘"
            },
            {
                "input": "동료가 내 일을 방해해서 화가 났다",
                "expected_emotion": "화남",
                "expected_situation": "업무",
                "expected_time": None
            }
        ]
        
        for case in test_cases:
            result = rag_agent.analyze_user_input(case["input"])
            
            assert isinstance(result, DiarySearchQuery)
            assert result.user_utterance == case["input"]
            assert result.inferred_emotion == case["expected_emotion"]
            assert result.inferred_situation == case["expected_situation"]
            assert result.time_context == case["expected_time"]
    
    def test_search_query_generation(self, rag_agent):
        """검색 쿼리 생성 테스트"""
        test_cases = [
            {
                "parsed_query": DiarySearchQuery(
                    user_utterance="요즘 우울하다",
                    inferred_emotion="우울",
                    inferred_situation="업무",
                    time_context="이번_주"
                ),
                "expected_keywords": ["우울", "슬픔"],
                "expected_context": "업무"
            },
            {
                "parsed_query": DiarySearchQuery(
                    user_utterance="오늘 기뻤다",
                    inferred_emotion="기쁨",
                    inferred_situation="친구",
                    time_context="오늘"
                ),
                "expected_keywords": ["기쁨", "행복"],
                "expected_context": "친구"
            }
        ]
        
        for case in test_cases:
            query_keywords, where_filter = rag_agent.generate_search_query(case["parsed_query"])
            
            # 키워드에 감정 키워드가 포함되어야 함
            for expected_keyword in case["expected_keywords"]:
                assert expected_keyword in query_keywords
            
            # 필터에 상황이 포함되어야 함
            assert where_filter["context"] == case["expected_context"]
    
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
        
        # 중간 유사도의 결과
        medium_similarity_entries = [
            SearchResult(content="test1", similarity_score=0.6, metadata={}),
            SearchResult(content="test2", similarity_score=0.5, metadata={})
        ]
        confidence = rag_agent._calculate_confidence(medium_similarity_entries)
        assert 0.4 < confidence < 0.7
    
    def test_analysis_text_generation(self, rag_agent):
        """분석 텍스트 생성 테스트"""
        # 관련 엔트리가 있는 경우
        related_entries = [
            SearchResult(
                content="오늘 회의에서 내 의견이 무시당한 것 같아서 속상했다.",
                similarity_score=0.8,
                metadata={"date": "2024-11-20", "emotion": "우울", "context": "업무"}
            ),
            SearchResult(
                content="요즘 계속 우울한 기분이 들고 아무것도 하고 싶지 않다.",
                similarity_score=0.7,
                metadata={"date": "2024-11-19", "emotion": "우울", "context": "업무"}
            )
        ]
        
        analysis = rag_agent._generate_analysis_text(
            "요즘 계속 우울한데 이번 주에 내가 뭐 때문에 그런지 모르겠어",
            "관련 일기 내용",
            related_entries
        )
        
        assert "우울" in analysis
        assert "0.750" in analysis  # 평균 유사도
        assert len(analysis) > 100
    
    def test_analysis_text_generation_empty(self, rag_agent):
        """빈 결과에 대한 분석 텍스트 생성 테스트"""
        analysis = rag_agent._generate_analysis_text(
            "테스트 쿼리",
            "",
            []
        )
        
        assert "찾을 수 없어서" in analysis
        assert len(analysis) > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 