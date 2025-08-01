"""
LLM(Large Language Model) 상호작용을 위한 서비스 모듈입니다.

OpenAI의 GPT 모델과 같은 LLM을 호출하고, 응답을 받아오는
핵심 로직을 캡슐화합니다.
"""

from openai import OpenAI
import logging
from config.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMService:
    """
    LLM API와의 통신을 담당하는 서비스 클래스.
    """
    def __init__(self):
        """
        LLMService 인스턴스를 초기화합니다.
        API 키와 클라이언트를 설정합니다.
        """
        self.config = Config()
        self.client = None
        self._initialize_client()

    def _initialize_client(self):
        """OpenAI 클라이언트를 초기화합니다."""
        try:
            if not self.config.OPENAI_API_KEY:
                raise ValueError("OpenAI API 키가 설정되지 않았습니다. .env 파일을 확인해주세요.")
            
            self.client = OpenAI(api_key=self.config.OPENAI_API_KEY)
            logger.info("✅ OpenAI 클라이언트가 성공적으로 초기화되었습니다.")
            
        except Exception as e:
            logger.error(f"❌ OpenAI 클라이언트 초기화에 실패했습니다: {e}")
            raise

    def get_response(self, prompt: str, system_message: str = "You are a helpful assistant.") -> str:
        """
        주어진 프롬프트와 시스템 메시지를 사용하여 LLM으로부터 응답을 생성합니다.

        Args:
            prompt (str): 모델에게 전달할 메인 프롬프트(사용자 메시지).
            system_message (str): 모델의 역할이나 페르소나를 정의하는 시스템 메시지.

        Returns:
            str: LLM이 생성한 응답 텍스트.
                 오류 발생 시, 에러 메시지를 담은 문자열을 반환합니다.
        """
        if not self.client:
            error_msg = "클라이언트가 초기화되지 않아 응답을 생성할 수 없습니다."
            logger.error(error_msg)
            return error_msg

        try:
            logger.debug(f"LLM 요청 시작: 시스템 메시지='{system_message[:50]}...', 프롬프트='{prompt[:50]}...'")
            
            response = self.client.chat.completions.create(
                model=self.config.GPT_MODEL,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.config.MAX_TOKENS,
                temperature=self.config.TEMPERATURE
            )
            
            content = response.choices[0].message.content.strip()
            logger.debug("LLM 응답 수신 완료.")
            return content
            
        except Exception as e:
            logger.error(f"❌ LLM 응답 생성 중 오류가 발생했습니다: {e}")
            return f"죄송합니다. 응답을 생성하는 중에 오류가 발생했습니다: {e}"

# 이 모듈이 직접 실행될 때 간단한 테스트를 수행하기 위한 코드
if __name__ == '__main__':
    try:
        # LLMService 인스턴스 생성
        llm_service = LLMService()

        # 테스트용 프롬프트
        test_prompt = "대한민국의 수도는 어디인가요?"
        test_system_message = "당신은 지리 전문가입니다. 모든 답변은 한국어로 간결하게 해주세요."

        # 응답 받아오기
        print(f"질문: {test_prompt}")
        advice = llm_service.get_response(test_prompt, system_message=test_system_message)
        
        # 결과 출력
        print(f"답변: {advice}")

    except Exception as e:
        print(f"테스트 중 오류 발생: {e}") 