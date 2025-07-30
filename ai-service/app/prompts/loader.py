from pathlib import Path

# 프롬프트 파일 경로 정의
PROMPT_DIR = Path(__file__).parent

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
    "diary_chunking": PROMPT_DIR / "diary_chunking_prompt.txt",  # 일기 청킹 프롬프트
    "diary_preprocess": PROMPT_DIR / "diary_preprocess_prompt.txt",  # 일기 전처리 프롬프트
    "emotion_situation_extraction": PROMPT_DIR / "emotion_situation_extraction_prompt.txt",  # 감정/상황 추출 프롬프트
    "category_mapping": PROMPT_DIR / "category_mapping_prompt.txt",  # 카테고리 매핑 프롬프트
    "advice_integration": PROMPT_DIR / "advice_integration_prompt.txt",  # 조언 통합 프롬프트
    "comment_generation": PROMPT_DIR / "comment_generation_prompt.txt",  # 코멘트 생성 프롬프트
    "comment_generation_no_quote": PROMPT_DIR / "comment_generation_no_quote_prompt.txt",  # 코멘트 생성 프롬프트 (명언 없음)
    "comment_selection": PROMPT_DIR / "comment_selection_prompt.txt",  # 코멘트 선택 프롬프트
    "emotion_keywords": PROMPT_DIR / "emotion_keywords_prompt.txt"  # 감정 키워드 추출 프롬프트
}

def load_prompt(name: str) -> str:
    """
    프롬프트 파일을 로드하는 함수
    
    Args:
        name: 프롬프트 이름 (preprocess, classify, ask, recent 등)
        
    Returns:
        str: 프롬프트 내용
        
    Raises:
        FileNotFoundError: 프롬프트 파일이 없는 경우
    """
    path = PROMPT_FILES.get(name)
    if not path or not path.exists():
        raise FileNotFoundError(f"Prompt not found: {name}")
    return path.read_text(encoding='utf-8') 