from __future__ import annotations
import json
from typing import Optional, List, Any, Callable
from pydantic import ValidationError

from app.prompts.loader import load_prompt
from app.utils.llm import call_llm
from app.utils.jsonUtil import parse_json_str
from app.models.agent import (
    ChatContext, PreprocessResult, ClassifyResult, AskDecisionResult,
    RecentMessage, ManageResponse, SafetyFlags
)

# 타입 별칭 정의
HistoryLoader = Callable[[int, int], Any]  # 사용자ID, 제한수 -> 대화 히스토리
HistorySaver  = Callable[[int, str, str], Any]  # 사용자ID, 화자, 메시지 -> 저장
UserIdProvider = Callable[[], Optional[int]]  # 현재 사용자ID 반환

class ConversationManager:
    """
    대화 관리 파이프라인을 처리하는 메인 클래스
    
    처리 흐름:
    1. 전처리 (안전성 검사, 형식 검증)
    2. 최근 대화 로드
    3. 분류 (의도 파악, 라우팅 결정)
    4. 재질문 판단 (ASK vs REPLY)
    """
    
    def __init__(
        self,
        user_id_provider: Optional[UserIdProvider] = None,
        history_loader: Optional[HistoryLoader] = None,
        history_saver: Optional[HistorySaver] = None,
    ):
        self.user_id_provider = user_id_provider
        self.history_loader = history_loader
        self.history_saver = history_saver

    async def handle(self, user_input: str) -> ManageResponse:
        """
        사용자 입력을 처리하는 메인 메서드
        
        Args:
            user_input: 사용자 입력 텍스트
            
        Returns:
            ManageResponse: 처리 결과 (ASK/REPLY 결정)
        """
        user_id = self.user_id_provider() if self.user_id_provider else None
        ctx = ChatContext(user_input=user_input)

        # 1) 전처리: 안전성 검사, 형식 검증
        ctx.preprocess = await self._run_preprocess(ctx.user_input)

        # 2) 최근 대화 로드: 컨텍스트 제공
        ctx.recent_history = await self._load_recent(user_id)

        # 3) 분류: 의도 파악, 라우팅 결정
        ctx.classification = await self._run_classify(ctx.user_input)

        # 4) 재질문 판단: ASK vs REPLY 결정
        ctx.decision_result = await self._decide_and_maybe_ask(ctx)

        # 대화 로그 저장 (선택적)
        if self.history_saver and user_id is not None:
            await self.history_saver(user_id, "user", user_input)

        return ManageResponse(**ctx.decision_result.model_dump())

    async def _run_preprocess(self, user_input: str) -> PreprocessResult:
        """
        입력 전처리: 안전성 검사, 형식 검증
        
        - 오타 검사, 정규화, 길이 검증
        - 안전성 플래그 (자해, 폭력 등) 검사
        - 언어 감지, 우려사항 파악
        """
        prompt = load_prompt("preprocess")
        raw = await call_llm(f"{prompt}\n\n{user_input}", response_format="json_object")
        data = parse_json_str(raw)
        return PreprocessResult.model_validate(data)

    async def _load_recent(self, user_id: Optional[int]) -> List[RecentMessage]:
        """
        최근 대화 히스토리 로드 (최신 5개)
        
        최신 메시지가 배열 앞쪽에 오도록 정렬
        """
        if not self.history_loader or user_id is None:
            return []
        items = await self.history_loader(user_id, 5)
        return [RecentMessage.model_validate(x) for x in items]

    async def _run_classify(self, user_input: str) -> ClassifyResult:
        """
        사용자 발화 분류: 의도 파악, 라우팅 결정
        
        - route_type: Simple/Complex/Ambiguous
        - primary_type: SimpleEmotion/ComplexEvent/QuestionRequest
        - confidence: 분류 신뢰도 (0.0~1.0)
        - 안전성 플래그 재검사
        """
        prompt = load_prompt("classify")
        raw = await call_llm(f"{prompt}\n\n{user_input}", response_format="json_object")
        data = parse_json_str(raw)
        return ClassifyResult.model_validate(data)

    async def _decide_and_maybe_ask(self, ctx: ChatContext) -> AskDecisionResult:
        """
        재질문 판단: ASK vs REPLY 결정
        
        판단 기준:
        1. 고위험 에스컬레이션 우선 처리
        2. 전처리 실패 (pass=False)
        3. 분류 애매함 (route_type=Ambiguous)
        4. 신뢰도 부족 (confidence < 0.60)
        """
        pre = ctx.preprocess
        cla = ctx.classification
        if pre is None or cla is None:
            raise RuntimeError("Pipeline order violation: preprocess/classify missing")

        # 1. 고위험 에스컬레이션 우선 처리
        if pre.escalate_recommended or cla.escalate_recommended:
            print(f"[DEBUG] Escalation detected: pre.escalate_recommended={pre.escalate_recommended}, cla.escalate_recommended={cla.escalate_recommended}")
            return AskDecisionResult(
                decision="REPLY",
                reason="중대 위험 신호 감지 → 위기 대응 플로우로 이관",
                handoff_payload={
                    "type": cla.primary_type,
                    "severity": max(pre.severity, cla.severity),
                    "escalate": True,
                    "safety_flags": cla.safety_flags.model_dump(),
                },
            )

        # 2. 재질문 필요 여부 판단
        is_really_short = (len(ctx.user_input.strip()) <= 5 or len(ctx.user_input.strip().split()) <= 2)
        need_ask = (
            (cla.route_type == "Ambiguous") or
            (cla.confidence < 0.60) or
            (not pre.pass_ and is_really_short)
        )
        print(f"[DEBUG] Decision variables: route_type={cla.route_type}, confidence={cla.confidence}, is_really_short={is_really_short}, pre.pass_={pre.pass_}, need_ask={need_ask}")
        
        # 3. 정보 충분한 경우 REPLY
        if not need_ask:
            print(f"[DEBUG] Decision: REPLY (정보 충분)")
            return AskDecisionResult(
                decision="REPLY",
                reason="정보 충분: 전처리 통과 및 분류 신뢰도 확보",
                handoff_payload={
                    "type": cla.primary_type,
                    "route_type": cla.route_type,
                    "severity": cla.severity,
                    "confidence": cla.confidence,
                },
            )

        # 4. 정보 부족한 경우 ASK (재질문 생성)
        prompt = load_prompt("ask")
        payload = {
            "user_input": ctx.user_input,
            "preprocess": pre.model_dump(by_alias=True),
            "classification": cla.model_dump(),
            "recent_history": [m.model_dump() for m in ctx.recent_history],
        }
        print(f"[DEBUG] Sending to ask prompt: {json.dumps(payload, ensure_ascii=False)}")
        raw = await call_llm(f"{prompt}\n\n{json.dumps(payload, ensure_ascii=False)}", response_format="json_object")
        data = parse_json_str(raw)
        print(f"[DEBUG] Ask prompt response: {data}")
        return AskDecisionResult.model_validate(data) 