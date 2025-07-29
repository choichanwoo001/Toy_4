import json, re
from typing import Any

# JSON 블록을 찾기 위한 정규식
_JSON_RE = re.compile(r"\{.*\}|\[.*\]", re.S)

def parse_json_str(raw: str) -> Any:
    """
    LLM 응답에서 JSON을 추출하고 파싱하는 함수
    
    특징:
    - 코드 블록이나 설명 텍스트 제거
    - JSON 객체 또는 배열 자동 감지
    - 에러 시 명확한 예외 메시지
    
    Args:
        raw: LLM 원본 응답 텍스트
        
    Returns:
        Any: 파싱된 JSON 객체/배열
        
    Raises:
        ValueError: JSON을 찾을 수 없는 경우
        json.JSONDecodeError: JSON 파싱 실패 시
    """
    raw = raw.strip()
    
    # 이미 JSON으로 시작하는 경우
    if raw.startswith("{") or raw.startswith("["):
        return json.loads(raw)
    
    # 텍스트 중에서 JSON 블록 찾기
    m = _JSON_RE.search(raw)
    if not m:
        raise ValueError("No JSON found in LLM output")
    
    return json.loads(m.group(0)) 