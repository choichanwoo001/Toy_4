from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DiaryEntry(BaseModel):
    content: str
    date: str
    emotion: str
    context: Optional[str] = None
    
class DiarySearchQuery(BaseModel):
    user_utterance: str
    inferred_emotion: Optional[str] = None
    inferred_situation: Optional[str] = None
    time_context: Optional[str] = None
    
class SearchResult(BaseModel):
    content: str
    similarity_score: float
    metadata: dict
    
class RAGResponse(BaseModel):
    analysis: str
    related_entries: List[SearchResult]
    confidence_score: float 