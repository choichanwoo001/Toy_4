from typing import List, Literal, Optional, Dict, Any
from pydantic import BaseModel, Field

# ----- 공통 -----

class SafetyFlags(BaseModel):
    self_harm: bool
    violence: bool
    abuse: bool
    medical: bool
    sexual: bool
    minors: bool
    illegal: bool
    privacy: bool

# ----- preprocess -----

class PreprocessResult(BaseModel):
    spelling_check: Literal["오타 없음", "의심 오타 있음"]
    normalization: Literal["완료", "필요"]
    length: str
    language: Literal["한국어", "기타"]
    concerns: str
    safety_flags: SafetyFlags
    severity: int = Field(ge=0, le=3)
    safety_notes: Optional[str] = ""
    escalate_recommended: bool
    pass_: bool = Field(alias="pass")
    correction_suggestion: Optional[str] = None
    normalization_example: Optional[str] = None
    fail_reasons: Optional[List[str]] = None

    class Config:
        populate_by_name = True

# ----- classify -----

class ClassifySignals(BaseModel):
    has_emotion_words: bool
    has_event_sequence: bool
    has_question_mark: bool

class ClassifyResult(BaseModel):
    route_type: Literal["Ambiguous", "Complex", "Simple"]
    primary_type: Literal["SimpleEmotion", "ComplexEvent", "QuestionRequest"]
    confidence: float = Field(ge=0.0, le=1.0)
    route_confidence: float = Field(ge=0.0, le=1.0)
    ambiguous: bool
    reason: str
    signals: ClassifySignals
    safety_flags: SafetyFlags
    severity: int = Field(ge=0, le=3)
    escalate_recommended: bool

# ----- recent -----

class RecentMessage(BaseModel):
    speaker: Literal["user", "ai"]
    message: str

# ----- ask -----

class AskQuestion(BaseModel):
    id: str
    text: str
    kind: Literal["single", "multi", "free"]
    options: Optional[List[str]] = None
    allow_free_text: Optional[bool] = None
    required: bool = True

class AskNextExpected(BaseModel):
    target_type: Optional[str] = None
    required_fields: Optional[List[str]] = None

class AskDecisionResult(BaseModel):
    decision: Literal["ASK", "REPLY"]
    reason: str
    primary_issues: Optional[List[str]] = None
    questions: Optional[List[AskQuestion]] = None
    next_expected: Optional[AskNextExpected] = None
    handoff_payload: Optional[Dict[str, Any]] = None

# ----- 파이프라인 컨텍스트 -----

class ChatContext(BaseModel):
    user_input: str
    preprocess: Optional[PreprocessResult] = None
    recent_history: List[RecentMessage] = []
    classification: Optional[ClassifyResult] = None
    decision_result: Optional[AskDecisionResult] = None

# ----- API I/O -----

class ManageRequest(BaseModel):
    user_input: str
    user_id: Optional[int] = None

class ManageResponse(AskDecisionResult):
    pass

# ----- 채팅 API I/O -----

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[int] = None

class ChatResponse(BaseModel):
    response: str
    user_id: Optional[int] = None

# ----- 고급 채팅 API I/O (ChatbotService 사용) -----

class AdvancedChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None

class AdvancedChatResponse(BaseModel):
    success: bool
    response: str
    user_id: Optional[str] = None
    intent: Optional[str] = None
    rag_used: Optional[bool] = None

class ConversationSummaryRequest(BaseModel):
    user_id: Optional[str] = None

class ConversationSummaryResponse(BaseModel):
    success: bool
    response: str
    user_id: Optional[str] = None 