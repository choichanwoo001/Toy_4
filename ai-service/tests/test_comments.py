import pytest
import json
from typing import Dict, Any
from unittest.mock import Mock, patch
from pydantic import ValidationError

# 상대 경로로 import
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from services.comment_generator import (
    CommentGenerator, 
    CommentGenerationResult, 
    ProcessingStatus,
    DiaryChunk,
    PreprocessingResult
)

class TestCommentGeneration:
    """댓글/피드백 생성 테스트"""
    
    def setup_method(self):
        """각 테스트 전에 실행되는 설정"""
        self.generator = CommentGenerator()
    
    def test_successful_comment_generation(self):
        """정상적인 댓글 생성 테스트"""
        # Given: 의미 있는 일기 입력
        user_input = "오늘 친구와 만나서 정말 행복했다. 맛있는 음식도 먹고 좋은 대화도 나눴다. 내일도 이런 날이 있었으면 좋겠다."
        
        # When: 댓글 생성 실행
        result = self.generator.process_diary_input(user_input)
        
        # Then: 성공 상태 확인
        assert result.status == ProcessingStatus.SUCCESS
        assert len(result.chunks) >= 1
        assert result.preprocessing_result.is_valid
        assert result.error_message is None
        
        # 청크 내용 검증
        for chunk in result.chunks:
            assert isinstance(chunk, DiaryChunk)
            assert chunk.content
            assert chunk.semantic_meaning
            assert chunk.word_count > 0
    
    def test_bland_diary_detection(self):
        """무미건조한 일기 감지 테스트"""
        # Given: 너무 짧거나 의미 없는 입력
        bland_inputs = [
            "안녕",
            "그냥",
            "오늘도",
            "일반적인 하루였다"
        ]
        
        for input_text in bland_inputs:
            # When: 댓글 생성 실행
            result = self.generator.process_diary_input(input_text)
            
            # Then: 무미건조한 일기로 분류
            assert result.status == ProcessingStatus.BLAND_DIARY
            assert result.prompt_c_response is not None
            assert "조금 더 구체적으로" in result.prompt_c_response
    
    def test_prompt_c_feedback_generation(self):
        """프롬프트 C 피드백 생성 테스트"""
        # Given: 무미건조한 일기 입력
        bland_input = "오늘도 그랬다"
        
        # When: 피드백 생성
        result = self.generator.process_diary_input(bland_input)
        
        # Then: 피드백 내용 확인
        assert result.status == ProcessingStatus.BLAND_DIARY
        assert result.prompt_c_response is not None
        assert "💡" in result.prompt_c_response
        assert "예시:" in result.prompt_c_response
        assert "❌" in result.prompt_c_response
        assert "✅" in result.prompt_c_response
    
    def test_prompt_c_error_handling(self):
        """프롬프트 C 에러 처리 테스트"""
        # Given: 빈 입력
        empty_input = ""
        
        # When: 피드백 생성
        result = self.generator.process_diary_input(empty_input)
        
        # Then: 에러 상태 확인
        assert result.status == ProcessingStatus.ERROR
        assert result.error_message is not None
        assert not result.preprocessing_result.is_valid
    
    def test_bland_diary_detection_with_prompt_c(self):
        """프롬프트 C를 통한 무미건조한 일기 감지 테스트"""
        # Given: 다양한 무미건조한 입력들
        test_cases = [
            ("안녕", "너무 짧음"),
            ("그냥", "의미 없음"),
            ("오늘도", "불완전한 문장"),
            ("일반적인 하루였다", "감정 없음")
        ]
        
        for input_text, expected_reason in test_cases:
            # When: 댓글 생성 실행
            result = self.generator.process_diary_input(input_text)
            
            # Then: 무미건조한 일기로 분류되고 피드백 생성
            assert result.status == ProcessingStatus.BLAND_DIARY
            assert result.prompt_c_response is not None
            assert len(result.prompt_c_response) > 50  # 충분한 피드백 길이
    
    def test_prompt_c_feedback_content_analysis(self):
        """프롬프트 C 피드백 내용 분석 테스트"""
        # Given: 다양한 품질의 입력들
        test_cases = [
            ("안녕", "짧음"),
            ("오늘 하루도 무난하게 보냈다", "감정 없음"),
            ("친구를 만났다", "활동만 나열"),
            ("오늘 좋았다", "너무 간단함")
        ]
        
        for input_text, expected_issue in test_cases:
            # When: 피드백 생성
            result = self.generator.process_diary_input(input_text)
            
            # Then: 적절한 피드백 생성
            assert result.status == ProcessingStatus.BLAND_DIARY
            feedback = result.prompt_c_response
            
            # 피드백에 필요한 요소들 포함 확인
            assert "💡" in feedback
            assert "예시:" in feedback
            assert "다시 한 번" in feedback
            assert "😊" in feedback
    
    def test_prompt_c_feedback_tone(self):
        """프롬프트 C 피드백 톤 테스트"""
        # Given: 무미건조한 일기
        bland_input = "오늘도 그랬다"
        
        # When: 피드백 생성
        result = self.generator.process_diary_input(bland_input)
        
        # Then: 친근하고 격려하는 톤 확인
        feedback = result.prompt_c_response
        assert "당신의" in feedback  # 개인화된 표현
        assert "도와주세요" in feedback or "쓰세요" in feedback  # 격려 표현
        assert "😊" in feedback  # 이모지 사용
    
    def test_prompt_c_example_formatting(self):
        """프롬프트 C 예시 형식 테스트"""
        # Given: 무미건조한 일기
        bland_input = "오늘 하루도 무난하게 보냈다"
        
        # When: 피드백 생성
        result = self.generator.process_diary_input(bland_input)
        
        # Then: 예시 형식 확인
        feedback = result.prompt_c_response
        assert "❌" in feedback  # 잘못된 예시
        assert "✅" in feedback  # 올바른 예시
        assert "→" in feedback  # 화살표 표시
    
    def test_prompt_c_feedback_length(self):
        """프롬프트 C 피드백 길이 테스트"""
        # Given: 다양한 길이의 무미건조한 입력들
        test_cases = [
            "안녕",
            "오늘도",
            "그냥",
            "일반적인 하루였다"
        ]
        
        for input_text in test_cases:
            # When: 피드백 생성
            result = self.generator.process_diary_input(input_text)
            
            # Then: 충분한 길이의 피드백 생성
            feedback = result.prompt_c_response
            assert len(feedback) > 100  # 최소 100자 이상
            assert len(feedback) < 1000  # 너무 길지 않음
    
    def test_prompt_c_feedback_consistency(self):
        """프롬프트 C 피드백 일관성 테스트"""
        # Given: 동일한 입력
        input_text = "오늘도 그랬다"
        
        # When: 여러 번 피드백 생성
        results = []
        for _ in range(3):
            result = self.generator.process_diary_input(input_text)
            results.append(result)
        
        # Then: 일관된 결과 확인
        for result in results:
            assert result.status == ProcessingStatus.BLAND_DIARY
            assert result.prompt_c_response is not None
            assert "💡" in result.prompt_c_response

class TestCommentIntegration:
    """댓글 생성 통합 테스트"""
    
    def setup_method(self):
        """각 테스트 전에 실행되는 설정"""
        self.generator = CommentGenerator()
    
    def test_comment_generation_in_pipeline(self):
        """파이프라인 내 댓글 생성 테스트"""
        # Given: 의미 있는 일기 입력
        user_input = "오늘 친구와 만나서 정말 행복했다. 맛있는 음식도 먹고 좋은 대화도 나눴다."
        
        # When: 전체 파이프라인 실행
        result = self.generator.process_diary_input(user_input)
        
        # Then: 성공적인 처리 확인
        assert result.status == ProcessingStatus.SUCCESS
        assert len(result.chunks) > 0
        assert result.preprocessing_result.is_valid
        
        # 청크 품질 확인
        for chunk in result.chunks:
            assert len(chunk.content) >= 10
            assert chunk.semantic_meaning != "일반적인 일기"
            assert chunk.word_count >= 3
    
    def test_comment_generation_comparison_with_success_path(self):
        """성공 경로와 댓글 생성 경로 비교 테스트"""
        # Given: 두 가지 다른 입력
        meaningful_input = "오늘 친구와 만나서 정말 행복했다. 맛있는 음식도 먹었다."
        bland_input = "오늘도 그랬다"
        
        # When: 각각 처리
        meaningful_result = self.generator.process_diary_input(meaningful_input)
        bland_result = self.generator.process_diary_input(bland_input)
        
        # Then: 다른 경로로 처리됨
        assert meaningful_result.status == ProcessingStatus.SUCCESS
        assert bland_result.status == ProcessingStatus.BLAND_DIARY
        
        # 의미 있는 입력은 청크 생성
        assert len(meaningful_result.chunks) > 0
        assert meaningful_result.prompt_c_response is None
        
        # 무미건조한 입력은 피드백 생성
        assert len(bland_result.chunks) == 0
        assert bland_result.prompt_c_response is not None
    
    def test_comment_generation_error_scenarios(self):
        """댓글 생성 에러 시나리오 테스트"""
        # Given: 에러가 발생할 수 있는 입력들
        error_inputs = [
            "",  # 빈 입력
            "   ",  # 공백만
            None  # None 입력 (실제로는 문자열로 처리됨)
        ]
        
        for input_text in error_inputs:
            if input_text is None:
                continue  # None은 실제로는 처리되지 않음
            
            # When: 댓글 생성 실행
            result = self.generator.process_diary_input(input_text)
            
            # Then: 에러 상태 확인
            assert result.status == ProcessingStatus.ERROR
            assert result.error_message is not None
            assert not result.preprocessing_result.is_valid
    
    def test_comment_generation_edge_cases(self):
        """댓글 생성 엣지 케이스 테스트"""
        # Given: 엣지 케이스 입력들
        edge_cases = [
            ("a", "한 글자"),
            ("오늘", "불완전한 문장"),
            ("오늘 하루도 무난하게 보냈다. 그냥 평범했다.", "감정 없는 긴 문장")
        ]
        
        for input_text, description in edge_cases:
            # When: 댓글 생성 실행
            result = self.generator.process_diary_input(input_text)
            
            # Then: 적절한 처리
            if len(input_text.strip()) < 5:
                assert result.status == ProcessingStatus.BLAND_DIARY
            else:
                # 결과는 성공이거나 무미건조한 일기
                assert result.status in [ProcessingStatus.SUCCESS, ProcessingStatus.BLAND_DIARY]

if __name__ == "__main__":
    pytest.main([__file__]) 