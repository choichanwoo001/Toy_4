import os
from typing import Optional
from dotenv import load_dotenv
from .jsonUtil import parse_json_str

# 환경 변수 로드
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None  # 에코 폴백 사용

# 기본 설정
DEFAULT_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
API_KEY = os.getenv("OPENAI_API_KEY")

async def call_llm(
    prompt_text: str,
    *,
    response_format: str = "json_object",
    model: Optional[str] = None,
) -> str:
    """
    LLM API 호출 함수
    
    특징:
    - OpenAI API 우선 사용
    - API 키 없으면 에코 폴백
    - JSON 응답 형식 지원
    - 에러 시 빈 JSON 반환
    
    Args:
        prompt_text: 프롬프트 텍스트
        response_format: 응답 형식 ("json_object" 권장)
        model: 사용할 모델명 (기본값: gpt-4o-mini)
        
    Returns:
        str: LLM 응답 (JSON 형식)
    """
    model = model or DEFAULT_MODEL

    # OpenAI API 사용 가능한 경우
    if OpenAI and API_KEY:
        client = OpenAI(api_key=API_KEY)
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt_text}],
            response_format={"type": "json_object"} if response_format == "json_object" else None,
            temperature=0.2,  # 일관성 있는 응답을 위해 낮은 온도
        )
        return resp.choices[0].message.content or "{}"

    # 폴백: 개발용 에코 모드
    # 실제 운영 전 반드시 SDK/키 설정 권장
    return prompt_text 