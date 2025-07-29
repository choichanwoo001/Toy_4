from pydantic import BaseModel
from typing import List, Optional

class DiaryAnalysisRequest(BaseModel):
    """일기 분석 요청 모델"""
    user_id: str
    raw_diary: str

class DiaryAnalysisResponse(BaseModel):
    """일기 분석 응답 모델"""
    processed_diary: str
    chunks: List[str]
    advice: Optional[str]
    comment: str
    quote: Optional[str]
    emotion_keywords: List[str]
    similar_past_diaries: List[str]

class DiaryChunk(BaseModel):
    """일기 청크 모델"""
    content: str
    emotion: str
    situation: str
    emotion_category: str
    situation_category: str

class EmotionSituationExtraction(BaseModel):
    """감정/상황 추출 결과 모델"""
    emotion: str
    situation: str
    emotion_category: str
    situation_category: str 