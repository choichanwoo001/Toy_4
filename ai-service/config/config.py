import os
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

class Config:
    # OpenAI API 설정
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # 임베딩 모델 설정 (HuggingFace)
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # 한국어 성능이 좋은 모델
    EMBEDDING_MODEL_DIARY = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    
    # ChromaDB 설정
    CHROMA_PERSIST_DIRECTORY = "ai-service/data/chroma_db"  # 데이터베이스 저장 경로
    COLLECTION_NAME = "diary_advice"  # 기본 조언 컬렉션
    QUOTES_COLLECTION_NAME = "diary_quotes"  # 명언 컬렉션
    PAST_DIARIES_COLLECTION_NAME = "diary_past_diaries"  # 과거 일기 컬렉션
    
    # 검색 설정
    TOP_K_RESULTS = 5  # 더 많은 후보 검색
    
    # GPT 모델 설정
    GPT_MODEL = "gpt-4"
    MAX_TOKENS = 1000
    TEMPERATURE = 0.5
    
    # 시스템 메시지
    SYSTEM_MESSAGE = """당신은 따뜻하고 공감능력이 뛰어난 심리상담사입니다. 
사용자의 일기를 읽고 비슷한 상황의 조언들을 참고하여 
현실적이면서도 위로가 되는 조언을 제공해주세요.""" 