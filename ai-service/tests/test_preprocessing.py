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
    PreprocessingResult,
    ProcessingStatus
)

class TestPreprocessing:
    """전처리 과정 전용 테스트"""
    
    def setup_method(self):
        """각 테스트 전에 실행되는 설정"""
        self.generator = CommentGenerator()
    
    def test_basic_preprocessing(self):
        """기본 전처리 테스트"""
        # Given: 다양한 입력 텍스트
        test_cases = [
            ("안녕하세요", "안녕하세요."),
            ("오늘 좋았다", "오늘 좋았다."),
            ("친구와 만났다", "친구와 만났다.")
        ]
        
        for input_text, expected_cleaned in test_cases:
            # When: 전처리 수행
            result = self.generator._perform_preprocessing(input_text)
            
            # Then: 전처리 결과 확인
            assert isinstance(result, PreprocessingResult)
            assert result.original_text == input_text
            assert result.cleaned_text == expected_cleaned
            assert result.is_valid == True
            assert "length" in result.context_info
    
    def test_grammar_correction(self):
        """문법 교정 테스트"""
        # Given: 문법 오류가 있는 텍스트
        test_cases = [
            ("안되겠다", "안 돼겠다."),
            ("못되겠다", "못 돼겠다."),
            ("안돼", "안 돼.")
        ]
        
        for input_text, expected_corrected in test_cases:
            # When: 전처리 수행
            result = self.generator._perform_preprocessing(input_text)
            
            # Then: 문법 교정 확인
            assert result.cleaned_text == expected_corrected
            assert len(result.grammar_corrections) > 0
    
    def test_context_analysis(self):
        """문맥 분석 테스트"""
        # Given: 다양한 감정과 활동이 포함된 텍스트
        test_cases = [
            ("오늘 친구와 만나서 행복했다", {"has_emotion": True, "has_activity": True, "tone": "positive"}),
            ("일이 너무 많아서 힘들었다", {"has_emotion": True, "has_activity": True, "tone": "negative"}),
            ("그냥 평범한 하루였다", {"has_emotion": False, "has_activity": False, "tone": "neutral"})
        ]
        
        for input_text, expected_context in test_cases:
            # When: 전처리 수행
            result = self.generator._perform_preprocessing(input_text)
            
            # Then: 문맥 분석 결과 확인
            assert result.context_info["has_emotion"] == expected_context["has_emotion"]
            assert result.context_info["has_activity"] == expected_context["has_activity"]
            assert result.context_info["tone"] == expected_context["tone"]
    
    def test_prompt_a_application(self):
        """프롬프트 A 적용 테스트"""
        # Given: 전처리 결과
        preprocessing_result = self.generator._perform_preprocessing("오늘 친구랑 만났는데 정말 좋았어... 안되겠다 그래도 해보자!!")
        
        # When: 프롬프트 A 적용
        enhanced_result = self.generator._apply_prompt_a(preprocessing_result)
        
        # Then: 프롬프트 A 적용 결과 확인
        assert enhanced_result.context_info.get("prompt_a_applied") == True
        assert "enhanced_emotions" in enhanced_result.context_info
        assert "enhanced_keywords" in enhanced_result.context_info
        
        # 정제된 텍스트 확인
        refined_text = enhanced_result.cleaned_text
        assert "안되" not in refined_text
        assert "안 돼" in refined_text
        assert "!!" not in refined_text
        assert "!" in refined_text
    
    def test_enhanced_emotion_extraction(self):
        """강화된 감정 추출 테스트"""
        # Given: 다양한 감정이 포함된 텍스트들
        test_cases = [
            ("오늘 정말 행복했다", ["행복"]),
            ("친구와 만나서 기뻤다", ["행복"]),
            ("일이 너무 많아서 힘들었다", ["피로"]),
            ("화가 났다", ["분노"]),
            ("우울했다", ["슬픔"]),
            ("걱정이 많다", ["불안"])
        ]
        
        for input_text, expected_emotions in test_cases:
            # When: 강화된 감정 추출
            emotions = self.generator._extract_enhanced_emotions(input_text)
            
            # Then: 예상 감정 확인
            for expected_emotion in expected_emotions:
                assert expected_emotion in emotions
    
    def test_enhanced_keyword_extraction(self):
        """강화된 키워드 추출 테스트"""
        # Given: 다양한 활동이 포함된 텍스트들
        test_cases = [
            ("친구와 만났다", ["인간관계"]),
            ("일을 했다", ["업무/학업"]),
            ("영화를 봤다", ["여가"]),
            ("음식을 먹었다", ["일상"]),
            ("생일 파티를 했다", ["인간관계", "특별한 이벤트"])
        ]
        
        for input_text, expected_keywords in test_cases:
            # When: 강화된 키워드 추출
            keywords = self.generator._extract_enhanced_keywords(input_text)
            
            # Then: 예상 키워드 확인
            for expected_keyword in expected_keywords:
                assert expected_keyword in keywords
    
    def test_text_refinement(self):
        """텍스트 정제 테스트"""
        # Given: 정제가 필요한 텍스트들
        test_cases = [
            ("안되겠다", "안 돼겠다."),
            ("못되겠다", "못 돼겠다."),
            ("그래도", "그래도."),
            ("그런데", "그런데."),
            ("오늘 좋았다...", "오늘 좋았다…"),
            ("정말 좋았다!!", "정말 좋았다!"),
            ("뭐지??", "뭐지?"),
            ("그냥", "그냥.")
        ]
        
        for input_text, expected_refined in test_cases:
            # When: 텍스트 정제
            refined = self.generator._refine_diary_text(input_text)
            
            # Then: 정제 결과 확인
            assert refined == expected_refined
    
    def test_prompt_a_error_handling(self):
        """프롬프트 A 에러 처리 테스트"""
        # Given: 전처리 결과
        preprocessing_result = self.generator._perform_preprocessing("테스트 텍스트")
        
        # Mock을 사용하여 프롬프트 A에서 예외 발생 시뮬레이션
        with patch.object(self.generator, '_refine_diary_text', side_effect=Exception("테스트 에러")):
            # When: 프롬프트 A 적용 (에러 발생)
            result = self.generator._apply_prompt_a(preprocessing_result)
            
            # Then: 에러 처리 확인 (원본 결과 반환)
            assert result == preprocessing_result
    
    def test_preprocessing_invalid_input(self):
        """유효하지 않은 입력 전처리 테스트"""
        # Given: 유효하지 않은 입력들
        invalid_inputs = [
            "",
            "   ",
            "\n\n\n"
        ]
        
        for input_text in invalid_inputs:
            # When: 전처리 수행
            result = self.generator._perform_preprocessing(input_text)
            
            # Then: 유효하지 않음으로 분류
            assert result.is_valid == False
            assert result.cleaned_text == ""
    
    def test_preprocessing_edge_cases(self):
        """전처리 엣지 케이스 테스트"""
        # Given: 엣지 케이스 입력들
        edge_cases = [
            ("a", "a."),
            ("한글", "한글."),
            ("123", "123."),
            ("!@#", "!@#."),
            ("", ""),  # 빈 문자열
            ("   ", "")  # 공백만
        ]
        
        for input_text, expected_cleaned in edge_cases:
            # When: 전처리 수행
            result = self.generator._perform_preprocessing(input_text)
            
            # Then: 예상 결과 확인
            if input_text.strip():
                assert result.cleaned_text == expected_cleaned
                assert result.is_valid == True
            else:
                assert result.is_valid == False
    
    def test_context_info_completeness(self):
        """문맥 정보 완성도 테스트"""
        # Given: 다양한 입력
        test_inputs = [
            "오늘 친구와 만나서 행복했다",
            "일이 너무 많아서 힘들었다",
            "그냥 평범한 하루였다"
        ]
        
        for input_text in test_inputs:
            # When: 전처리 수행
            result = self.generator._perform_preprocessing(input_text)
            
            # Then: 문맥 정보 완성도 확인
            required_keys = ["length", "has_emotion", "has_activity", "tone"]
            for key in required_keys:
                assert key in result.context_info
                assert result.context_info[key] is not None
    
    def test_grammar_corrections_tracking(self):
        """문법 교정 추적 테스트"""
        # Given: 문법 오류가 있는 텍스트
        input_text = "안되겠다 못되겠다"
        
        # When: 전처리 수행
        result = self.generator._perform_preprocessing(input_text)
        
        # Then: 문법 교정 추적 확인
        assert len(result.grammar_corrections) > 0
        assert "안되 → 안 돼" in result.grammar_corrections
        assert "못되 → 못 돼" in result.grammar_corrections
    
    def test_tone_analysis_accuracy(self):
        """톤 분석 정확도 테스트"""
        # Given: 다양한 톤의 텍스트들
        test_cases = [
            ("오늘 정말 행복했다", "positive"),
            ("기뻤다", "positive"),
            ("좋았다", "positive"),
            ("슬펐다", "negative"),
            ("우울했다", "negative"),
            ("힘들었다", "negative"),
            ("그냥 평범했다", "neutral")
        ]
        
        for input_text, expected_tone in test_cases:
            # When: 전처리 수행
            result = self.generator._perform_preprocessing(input_text)
            
            # Then: 톤 분석 정확도 확인
            assert result.context_info["tone"] == expected_tone

if __name__ == "__main__":
    pytest.main([__file__]) 