"""
사용자 입력을 전처리하는 모듈입니다.

이 모듈은 다음을 포함합니다:
- 문법 교정 및 자연스러운 문장으로 다듬기
- 의미 단위로 일기 내용을 청크(chunk)로 분할하기
"""
import json
import logging
import time
from typing import List, Dict, Any

from chatbot.llm_service import LLMService
from chatbot.prompts.loader import load_prompt

logger = logging.getLogger(__name__)

class Preprocessor:
    """사용자 입력 전처리를 담당하는 클래스"""

    def __init__(self, llm_service: LLMService):
        """
        초기화 메서드
        Args:
            llm_service (LLMService): LLM 호출을 위한 서비스 객체
        """
        self.llm_service = llm_service
        self.max_retries = 3

    def preprocess_diary(self, raw_diary: str) -> str:
        """
        일기 내용을 문법적으로 다듬고 문맥을 매끄럽게 정리합니다.
        
        Args:
            raw_diary (str): 원본 일기 내용
        
        Returns:
            str: 수정된 일기 내용
        """
        prompt = load_prompt("diary_correction").format(raw_diary=raw_diary)
        system_message = "너는 문장 교정에 특화된 한국어 편집기야. 일기를 자연스럽게 고쳐줘."

        for attempt in range(self.max_retries):
            try:
                response_str = self.llm_service.get_response(prompt, system_message)
                if "```" in response_str:
                    content = response_str.split("```")[1].strip()
                    if content.startswith("text"):
                        content = content[4:].strip()
                    return content
                return response_str # 응답이 형식을 따르지 않는 경우
            except Exception as e:
                logger.warning(f"일기 전처리 실패 {attempt + 1}회: {e}")
                time.sleep(1)
        return raw_diary # 실패 시 원본 반환

    # def chunk_diary_by_meaning(self, diary_text: str) -> List[str]:
    #     """
    #     일기를 의미 단위로 나눠 문장 단위의 청크로 만듭니다.

    #     Args:
    #         diary_text (str): 전처리된 일기 내용

    #     Returns:
    #         List[str]: 의미 단위로 분할된 청크 리스트
    #     """
    #     prompt = load_prompt("diary_chunking").format(diary_text=diary_text)
    #     messages = [
    #         {"role": "system", "content": "너는 텍스트를 의미 단위로 나누는 전문 청크 분석기야."},
    #         {"role": "user", "content": prompt}
    #     ]

    #     for attempt in range(self.max_retries):
    #         try:
    #             response_str = self.llm_service.get_response(messages=messages, temperature=0.3)
    #             if "```json" in response_str:
    #                 content = response_str.split("```json")[1].split("```")[0].strip()
    #             else:
    #                 # ```json이 없는 경우 대체 방법
    #                 content = response_str[response_str.find('['):response_str.rfind(']')+1]
                
    #             return json.loads(content)
    #         except Exception as e:
    #             logger.warning(f"청크 분할 실패 {attempt + 1}회: {e}")
    #             time.sleep(1)
    #     return [] # 실패 시 빈 리스트 반환 