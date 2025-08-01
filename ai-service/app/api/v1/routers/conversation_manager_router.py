# app/api/v1/routers/conversation_manager_router.py
from fastapi import APIRouter, Depends
from app.models.agent import (
    ManageRequest, ManageResponse, ChatRequest, ChatResponse,
    AdvancedChatRequest, AdvancedChatResponse, 
    ConversationSummaryRequest, ConversationSummaryResponse
)
from app.services.conversation_manager import ConversationManager
from app.services.history import RedisHistory

# AgentService import (상위 디렉토리의 chatbot 모듈 사용)
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from chatbot.agent_service import AgentService

conversation_router = APIRouter(
    prefix="/conversation-manager",                  # 👈 기능을 드러내는 prefix
    tags=["conversation-manager"],                   # 👈 문서화 시 명확
)

# Redis 기반 히스토리 관리 (fakeredis 사용)
_history = RedisHistory()

def _user_id_provider():
    # TODO: 실제 환경에선 인증/세션에서 user_id 추출
    return 1

async def _history_loader(user_id: int, limit: int):
    msgs = await _history.load(user_id, limit)
    return [m.model_dump() for m in msgs]

async def _history_saver(user_id: int, speaker: str, message: str):
    await _history.add(user_id, speaker, message)

def get_conversation_manager() -> ConversationManager:
    return ConversationManager(
        user_id_provider=_user_id_provider,
        history_loader=_history_loader,
        history_saver=_history_saver,
    )

@conversation_router.post(
    "/decide",                                      # 👈 역할을 드러내는 엔드포인트
    response_model=ManageResponse,
    summary="대화 관리 에이전트 의사결정(ASK/REPLY) 수행",
    description="전처리→최근 대화→분류를 통해 ASK/REPLY와 handoff_payload를 결정합니다.",
)
async def decide(
    req: ManageRequest,
    cm: ConversationManager = Depends(get_conversation_manager),
):
    result = await cm.handle(req.user_input)
    return result

@conversation_router.get(
    "/history/{user_id}",
    summary="사용자 대화 히스토리 조회",
    description="특정 사용자의 최근 대화 히스토리를 조회합니다.",
)
async def get_history(
    user_id: int,
    limit: int = 10,
    history: RedisHistory = Depends(lambda: _history),
):
    """사용자의 대화 히스토리 조회"""
    messages = await history.load(user_id, limit)
    return {
        "user_id": user_id,
        "message_count": len(messages),
        "messages": [msg.model_dump() for msg in messages]
    }

@conversation_router.delete(
    "/history/{user_id}",
    summary="사용자 대화 히스토리 삭제",
    description="특정 사용자의 대화 히스토리를 삭제합니다.",
)
async def clear_history(
    user_id: int,
    history: RedisHistory = Depends(lambda: _history),
):
    """사용자의 대화 히스토리 삭제"""
    await history.clear(user_id)
    return {"message": f"사용자 {user_id}의 대화 히스토리가 삭제되었습니다."}

@conversation_router.get(
    "/history/{user_id}/count",
    summary="사용자 메시지 개수 조회",
    description="특정 사용자의 저장된 메시지 개수를 조회합니다.",
)
async def get_message_count(
    user_id: int,
    history: RedisHistory = Depends(lambda: _history),
):
    """사용자의 메시지 개수 조회"""
    count = await history.get_user_count(user_id)
    return {"user_id": user_id, "message_count": count}

@conversation_router.post(
    "/chat",
    response_model=ChatResponse,
    summary="채팅 응답 생성",
    description="사용자 메시지에 대한 AI 응답을 생성합니다.",
)
async def chat(
    req: ChatRequest,
    history: RedisHistory = Depends(lambda: _history),
):
    """채팅 응답 생성"""
    user_id = req.user_id or 1  # 기본 사용자 ID
    
    # 사용자 메시지 저장
    await history.add(user_id, "user", req.message)
    
    # 간단한 AI 응답 생성 (실제로는 더 복잡한 로직)
    ai_response = generate_simple_response(req.message)
    
    # AI 응답 저장
    await history.add(user_id, "ai", ai_response)
    
    return ChatResponse(response=ai_response, user_id=user_id)

def generate_simple_response(user_message: str) -> str:
    """간단한 AI 응답 생성 함수"""
    message_lower = user_message.lower()
    
    if any(word in message_lower for word in ["힘들", "지쳐", "우울", "슬프"]):
        return "힘든 마음이 드셨군요. 선생님은 제자님의 그런 감정을 이해한답니다. 무엇이 제자님을 힘들게 했는지 좀 더 이야기해줄 수 있을까요?"
    elif any(word in message_lower for word in ["기분 좋", "행복", "기뻐", "즐거워"]):
        return "기분 좋은 일이 있으셨다니 선생님도 기쁘네요! 어떤 일이었는지 더 자세히 들려주세요!"
    elif any(word in message_lower for word in ["감사", "고마워", "고맙"]):
        return "제자님의 고마운 마음이 선생님에게도 전해져요. 언제든지 필요할 때 말씀해주세요."
    elif "?" in user_message or any(word in message_lower for word in ["어떻게", "왜", "무엇", "언제", "어디서"]):
        return "좋은 질문이네요. 제자님의 궁금증을 더 자세히 설명해주시면 선생님이 더 도움이 될 수 있을 것 같아요."
    else:
        return "선생님은 제자님의 말씀을 잘 들었어요. 더 자세히 이야기해줄 수 있을까요?"

# 전역 AgentService 인스턴스들을 관리하는 딕셔너리
_agent_instances = {}

def get_agent_service(user_id: str) -> AgentService:
    """사용자별 AgentService 인스턴스를 관리"""
    if user_id not in _agent_instances:
        agent_service = AgentService(user_id=user_id)
        agent_service.initialize()
        _agent_instances[user_id] = agent_service
    return _agent_instances[user_id]

@conversation_router.post(
    "/chat-advanced",
    response_model=AdvancedChatResponse,
    summary="고급 채팅 응답 생성 (Agent 기반)",
    description="AgentService를 사용하여 자율적 의사결정과 동적 전략 수립으로 AI 응답을 생성합니다.",
)
async def chat_advanced(req: AdvancedChatRequest):
    """고급 AgentService를 사용한 채팅 응답 생성"""
    user_id = req.user_id or "web_user_01"
    
    try:
        # AgentService 인스턴스 가져오기 (필요시 초기화)
        agent_service = get_agent_service(user_id)
        
        # AgentService로 응답 생성
        result = agent_service.get_response(req.message)
        
        # 에이전트 상태 정보 가져오기
        agent_state = agent_service.get_agent_state()
        
        # RAG 정보 추출
        rag_info = result.get('rag_info', {})
        rag_used = bool(rag_info.get('results', {}).get('documents', [[]])[0])
        
        # 유사도 점수 추출
        similarity_scores = []
        if rag_info.get('results', {}).get('distances'):
            distances = rag_info['results']['distances'][0]
            similarity_scores = [1 - dist for dist in distances]
        
        # 검색 필터 정보
        search_filters = rag_info.get('filters', {})
        
        return AdvancedChatResponse(
            success=result["success"],
            response=result["response"],
            user_id=user_id,
            intent=agent_state.get("intent"),
            rag_used=rag_used,
            rag_details=rag_info,
            search_query=rag_info.get('query'),
            search_filters=search_filters,
            similarity_scores=similarity_scores,
            total_searched=len(rag_info.get('results', {}).get('documents', [[]])[0]) if rag_info.get('results') else None,
            total_filtered=len([s for s in similarity_scores if s >= 0.5]) if similarity_scores else None
        )
        
    except Exception as e:
        return AdvancedChatResponse(
            success=False,
            response=f"죄송합니다. 시스템 오류가 발생했습니다: {str(e)}",
            user_id=user_id,
            intent=None,
            rag_used=None
        )

@conversation_router.post(
    "/conversation-summary",
    response_model=ConversationSummaryResponse,
    summary="대화 요약 및 종료",
    description="현재 대화를 종료하고 전체 대화 내용을 요약하여 제공합니다.",
)
async def end_conversation(req: ConversationSummaryRequest):
    """대화 종료 및 요약"""
    user_id = req.user_id or "web_user_01"
    
    try:
        if user_id in _agent_instances:
            agent_service = _agent_instances[user_id]
            result = agent_service.end_conversation()
            
            # 인스턴스 제거 (새로운 대화를 위해)
            del _agent_instances[user_id]
            
            return ConversationSummaryResponse(
                success=result["success"],
                response=result["response"],
                user_id=user_id
            )
        else:
            return ConversationSummaryResponse(
                success=True,
                response="아직 대화가 시작되지 않았습니다.",
                user_id=user_id
            )
            
    except Exception as e:
        return ConversationSummaryResponse(
            success=False,
            response=f"대화 요약 중 오류가 발생했습니다: {str(e)}",
            user_id=user_id
        )

@conversation_router.get(
    "/agent-state/{user_id}",
    summary="에이전트 상태 조회",
    description="특정 사용자의 에이전트 상태 정보를 조회합니다.",
)
async def get_agent_state(user_id: str):
    """에이전트 상태 조회"""
    try:
        if user_id in _agent_instances:
            agent_service = _agent_instances[user_id]
            state = agent_service.get_agent_state()
            return {
                "user_id": user_id,
                "agent_state": state
            }
        else:
            return {
                "user_id": user_id,
                "agent_state": {"error": "에이전트가 초기화되지 않았습니다."}
            }
    except Exception as e:
        return {
            "user_id": user_id,
            "agent_state": {"error": f"상태 조회 중 오류 발생: {str(e)}"}
        } 