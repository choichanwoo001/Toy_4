from pathlib import Path

# 프롬프트 파일 경로 정의
PROMPT_DIR = Path(__file__).parent.parent / "prompts"

# 프롬프트 파일 매핑 (이름 -> 파일 경로)
PROMPT_FILES = {
    "preprocess": PROMPT_DIR / "preprocess_prompt.txt",  # 입력 전처리 프롬프트
    "classify": PROMPT_DIR / "classify_prompt.txt",      # 발화 분류 프롬프트
    "ask": PROMPT_DIR / "ask_again_prompt.txt",          # 재질문 생성 프롬프트
    "recent": PROMPT_DIR / "recent_prompt.txt",          # 최근 대화 로드 프롬프트
    "intent_classification": PROMPT_DIR / "intent_classification_prompt.txt",  # 의도 분류 프롬프트
    "complex_event_analysis": PROMPT_DIR / "complex_event_analysis_prompt.txt",  # 복합 사건 분석 프롬프트
    "response_with_rag": PROMPT_DIR / "response_with_rag_prompt.txt",  # RAG 검색 성공 시 응답 프롬프트
    "response_without_rag": PROMPT_DIR / "response_without_rag_prompt.txt",  # RAG 검색 실패 시 응답 프롬프트
    "response_simple_emotion": PROMPT_DIR / "response_simple_emotion_prompt.txt",  # 단순 감정 응답 프롬프트
    "conversation_summary": PROMPT_DIR / "conversation_summary_prompt.txt",  # 대화 요약 프롬프트
    "diary_correction": PROMPT_DIR / "diary_correction_prompt.txt",  # 일기 수정 프롬프트
    "diary_chunking": PROMPT_DIR / "diary_chunking_prompt.txt"  # 일기 청킹 프롬프트
}

def load_prompt(name: str) -> str:
    """
    프롬프트 파일을 로드하는 함수
    
    Args:
        name: 프롬프트 이름 (preprocess, classify, ask, recent)
        
    Returns:
        str: 프롬프트 내용
        
    Raises:
        FileNotFoundError: 프롬프트 파일이 없는 경우
    """
    path = PROMPT_FILES.get(name)
    if not path or not path.exists():
        raise FileNotFoundError(f"Prompt not found: {name}")
    return path.read_text(encoding='utf-8')
