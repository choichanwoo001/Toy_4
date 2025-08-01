"""
MainAgent: 자율적 의사결정과 동적 전략 수립을 담당하는 메인 에이전트

이 모듈은 Perceive-Decide-Act 사이클을 통해 사용자 입력에 대한
적절한 응답을 생성하는 핵심 로직을 담당합니다.
- Perceive (인지): 사용자 입력과 대화 이력을 기반으로 현재 상태를 파악합니다.
- Decide (결정): 인지된 상태를 바탕으로 어떤 전략(도구 사용)을 실행할지 결정합니다.
- Act (실행): 결정된 전략에 따라 실제 도구들을 호출하여 응답을 생성합니다.
"""
import logging
import json
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

# 외부 모듈 임포트
from chatbot.llm_service import LLMService # LLM과의 통신을 담당하는 서비스
from chatbot.conversation_manager import ConversationManager # 사용자 대화 이력을 관리하는 서비스
from core.vector_db import VectorDatabase # RAG를 위한 벡터 데이터베이스 서비스
from chatbot.prompts.loader import load_prompt # 프롬프트 템플릿을 로드하는 유틸리티

logger = logging.getLogger(__name__) # 로깅 설정

@dataclass
class AgentState:
    """
    에이전트의 현재 내부 상태를 관리하는 데이터 클래스입니다.
    사용자 입력, 대화 이력, LLM 분석 결과 등을 저장하고 업데이트합니다.
    """
    user_input: str = "" # 현재 사용자 입력
    history: List[Dict[str, str]] = field(default_factory=list) # 현재까지의 대화 이력 (role, content 포함)
    intent: Optional[str] = None # LLM이 분석한 사용자 입력의 의도 (IntentType 값)
    emotion: Optional[str] = None # LLM이 분석한 사용자 입력의 감정
    situation: Optional[str] = None # LLM이 분석한 사용자 입력의 상황 (복합 사건인 경우)
    ambiguity_level: float = 0.0 # 사용자 입력의 모호성 수준 (0.0 ~ 1.0)
    complexity_score: float = 0.0 # 사용자 입력의 복잡도 점수 (0.0 ~ 1.0)
    requires_clarification: bool = False # 명확화가 필요한지 여부 (ambiguity_level에 따라 결정)

    user_input_length: int = 0 # 사용자 입력의 길이

    def update(self, user_input: str, history: List[Dict[str, str]]):
        """
        새로운 사용자 입력과 대화 이력을 기반으로 에이전트 상태를 업데이트합니다.
        입력 특성 분석을 포함합니다.
        Args:
            user_input (str): 현재 사용자 입력.
            history (List[Dict[str, str]]): 업데이트된 대화 이력.
        """
        self.user_input = user_input
        self.history = history
        self.user_input_length = len(user_input)
        self.analyze_input_characteristics() # 입력 특성 분석 메서드 호출

    def analyze_input_characteristics(self):
        """
        사용자 입력의 특성을 분석하여 복잡도 점수와 모호성 레벨을 계산합니다.
        의미적 복잡도, 감정 표현, 사건 서술 등을 종합적으로 고려합니다.
        """
        import re
        
        # 1. 기본 구조적 복잡도 계산
        sentences = re.split(r'[.!?]+', self.user_input.strip())
        sentences = [s.strip() for s in sentences if s.strip()]
        
        word_count = len(self.user_input.split())
        sentence_count = len(sentences)
        
        # 길이 기반 복잡도 (0.0 ~ 0.2)
        length_complexity = min(0.2, len(self.user_input) / 300.0)
        
        # 문장 수 기반 복잡도 (0.0 ~ 0.2)
        sentence_complexity = min(0.2, sentence_count * 0.08)
        
        # 단어 밀도 기반 복잡도 (0.0 ~ 0.2)
        avg_words_per_sentence = word_count / max(sentence_count, 1)
        density_complexity = min(0.2, avg_words_per_sentence / 25.0)
        
        structural_complexity = length_complexity + sentence_complexity + density_complexity
        
        # 2. 의미적 복잡도 분석
        semantic_complexity = 0.0
        
        # 감정 표현 패턴 감지
        emotion_patterns = [
            r'[가-힣]*[가-힣]다$',  # ~다로 끝나는 감정 표현
            r'[가-힣]*[가-힣]어$',  # ~어로 끝나는 감정 표현
            r'[가-힣]*[가-힣]네$',  # ~네로 끝나는 감정 표현
            r'[가-힣]*[가-힣]어요$',  # ~어요로 끝나는 감정 표현
            r'[가-힣]*[가-힣]네요$',  # ~네요로 끝나는 감정 표현
        ]
        
        emotion_matches = 0
        for pattern in emotion_patterns:
            if re.search(pattern, self.user_input):
                emotion_matches += 1
        
        # 사건 서술 패턴 감지
        event_patterns = [
            r'[가-힣]*했[가-힣]*',  # ~했~ 패턴
            r'[가-힣]*했는데',  # ~했는데
            r'[가-힣]*했지만',  # ~했지만
            r'[가-힣]*때문에',  # ~때문에
            r'[가-힣]*그래서',  # ~그래서
            r'[가-힣]*결과',  # ~결과
            r'[가-힣]*발생',  # ~발생
            r'[가-힣]*일어났',  # ~일어났
            r'[가-힣]*경험',  # ~경험
            r'[가-힣]*상황',  # ~상황
            r'[가-힣]*문제',  # ~문제
            r'[가-힣]*고민',  # ~고민
        ]
        
        event_matches = 0
        for pattern in event_patterns:
            if re.search(pattern, self.user_input):
                event_matches += 1
        
        # 복잡한 사고 표현 패턴 감지
        thinking_patterns = [
            r'[가-힣]*생각',  # ~생각
            r'[가-힣]*느낌',  # ~느낌
            r'[가-힣]*이유',  # ~이유
            r'[가-힣]*원인',  # ~원인
            r'[가-힣]*결과',  # ~결과
            r'[가-힣]*영향',  # ~영향
            r'[가-힣]*관계',  # ~관계
            r'[가-힣]*비교',  # ~비교
            r'[가-힣]*대조',  # ~대조
            r'[가-힣]*반면',  # ~반면
            r'[가-힣]*하지만',  # ~하지만
            r'[가-힣]*그런데',  # ~그런데
        ]
        
        thinking_matches = 0
        for pattern in thinking_patterns:
            if re.search(pattern, self.user_input):
                thinking_matches += 1
        
        # 의미적 복잡도 계산
        semantic_complexity += min(0.3, emotion_matches * 0.1)  # 감정 표현
        semantic_complexity += min(0.4, event_matches * 0.15)   # 사건 서술
        semantic_complexity += min(0.3, thinking_matches * 0.1) # 사고 표현
        
        # 3. 최종 복잡도 점수 계산
        self.complexity_score = structural_complexity + semantic_complexity
        self.complexity_score = min(1.0, self.complexity_score)
        
        # 4. 모호성 레벨 계산 (의미적 명확성 고려)
        base_ambiguity = 0.5  # 기본 모호성
        
        # 길이에 따른 모호성 조정
        if len(self.user_input) < 3:
            base_ambiguity += 0.4
        elif len(self.user_input) < 8:
            base_ambiguity += 0.2
        elif len(self.user_input) < 15:
            base_ambiguity += 0.1
        else:
            base_ambiguity -= 0.1
        
        # 의미적 명확성에 따른 모호성 조정
        if emotion_matches > 0:
            base_ambiguity -= 0.2  # 감정 표현이 있으면 명확함
        if event_matches > 0:
            base_ambiguity -= 0.2  # 사건 서술이 있으면 명확함
        if thinking_matches > 0:
            base_ambiguity -= 0.1  # 사고 표현이 있으면 명확함
        
        # 질문 포함 시 모호성 감소
        if '?' in self.user_input:
            base_ambiguity -= 0.3
        
        # 반복 표현 감지 (의미적 단순함)
        repeated_words = re.findall(r'(\b\w+\b)(?:\s+\1)+', self.user_input)
        if repeated_words:
            base_ambiguity += 0.1  # 반복은 모호함 증가
        
        # 모호성 레벨 최종 결정
        self.ambiguity_level = max(0.1, min(1.0, base_ambiguity))
        
        # 5. 명확화 필요 여부 결정
        self.requires_clarification = self.ambiguity_level > 0.6

    def update_with_result(self, result: Dict[str, Any]):
        """
        LLM 분석 도구(ConversationManagementTool)에서 반환된 결과를 기반으로
        에이전트 상태(의도, 감정, 상황)를 업데이트합니다.
        Args:
            result (Dict[str, Any]): LLM 분석 결과 딕셔너리.
        """
        if 'intent' in result:
            self.intent = result['intent']
        if 'emotion' in result:
            self.emotion = result['emotion']
        if 'situation' in result:
            self.situation = result['situation']


class ConversationManagementTool:
    """
    대화 관리 및 사용자 입력의 의도, 감정, 상황을 분석하는 도구입니다.
    주로 LLM을 호출하여 이 작업을 수행합니다.
    """
    def __init__(self, llm_service: LLMService):
        """
        ConversationManagementTool을 초기화합니다.
        Args:
            llm_service (LLMService): LLM과 통신하기 위한 서비스 객체.
        """
        self.llm_service = llm_service
    
    def analyze(self, state: AgentState) -> Dict[str, Any]:
        """
        사용자 입력을 분석하여 의도, 감정, 상황을 추출합니다.
        `intent_classification` 프롬프트를 사용하여 LLM에 요청합니다.
        복합 사건 서술의 경우, 추가적으로 `complex_event_analysis`를 호출하여 감정/상황을 세분화합니다.
        Args:
            state (AgentState): 현재 에이전트의 상태 객체.
        Returns:
            Dict[str, Any]: 분석 결과 (의도, 감정, 상황 등).
        """
        # 대화 이력을 문자열로 포맷팅하여 프롬프트에 포함
        history_str = "\n".join([f"{c['role']}: {c['content']}" for c in state.history])
        
        # 'intent_classification' 프롬프트 로드 및 포맷팅
        prompt = load_prompt("intent_classification").format(
            user_input=state.user_input,
            conversation_history=history_str
        )
        
        try:
            # LLM에 분석 요청
            response_str = self.llm_service.get_response(prompt)
            result = json.loads(response_str) # JSON 형식의 응답을 파싱
            
            # LLM이 복합 사건(Complex Event)으로 분류한 경우, 추가 분석 수행
            if result.get('intent') in ['Complex Event', '복합 사건 서술 (Complex Event)']:
                # user_input 전체에 대해 감정/상황 청크 분석 호출
                chunk_analysis = self.analyze_chunk(state.user_input) 
                result.update(chunk_analysis) # 분석 결과를 기존 결과에 병합
            
            return result
        except json.JSONDecodeError:
            logger.error(f"의도 분류 응답 파싱 실패: {response_str}", exc_info=True) # 에러 로그 상세 기록
            return {"intent": "Error", "reason": "LLM 응답 파싱 실패"}
    
    def analyze_chunk(self, chunk: str) -> Dict[str, Any]:
        """
        주어진 텍스트 청크(여기서는 user_input 전체)를 분석하여
        감정(emotion) 및 상황(situation) 태그를 추출합니다.
        `complex_event_analysis` 프롬프트를 사용합니다.
        Args:
            chunk (str): 분석할 텍스트 청크.
        Returns:
            Dict[str, Any]: 추출된 감정과 상황 딕셔너리.
        """
        # 'complex_event_analysis' 프롬프트 로드 및 포맷팅
        prompt = load_prompt("complex_event_analysis").format(user_input=chunk)
        response_str = self.llm_service.get_response(prompt) # LLM에 요청
        try:
            return json.loads(response_str) # JSON 응답 파싱
        except json.JSONDecodeError:
            logger.error(f"청크 분석 응답 파싱 실패: {response_str}", exc_info=True)
            return {} # 파싱 실패 시 빈 딕셔너리 반환


class RAGTool:
    """
    RAG(Retrieval Augmented Generation) 검색을 담당하는 도구입니다.
    사용자 입력의 감정/상황에 따라 벡터 데이터베이스에서 관련 조언을 검색합니다.
    """
    def __init__(self, vector_db: VectorDatabase):
        """
        RAGTool을 초기화합니다.
        Args:
            vector_db (VectorDatabase): 벡터 데이터베이스 서비스 객체.
        """
        self.vector_db = vector_db
        self.last_search_info = {}  # 마지막 검색 정보를 저장
    
    def execute(self, state: AgentState) -> Optional[str]:
        """
        현재 에이전트 상태(state)에 따라 적절한 RAG 검색 전략을 선택하고 실행합니다.
        감정, 상황 정보가 모두 있다면 필터 검색, 감정만 있다면 감정 필터 검색,
        없다면 일반 검색을 수행합니다.
        Args:
            state (AgentState): 현재 에이전트의 상태 객체.
        Returns:
            Optional[str]: 검색된 관련 조언들을 포맷팅한 문자열 또는 None.
        """
        if state.emotion and state.situation:
            # 감정과 상황 필터를 모두 사용하여 검색
            return self.search_with_filters(state.user_input, state.emotion, state.situation)
        elif state.emotion:
            # 감정 필터만 사용하여 검색
            return self.search_with_emotion_filter(state.user_input, state.emotion)
        else:
            # 필터 없이 일반 검색 (가장 넓은 범위)
            return self.search_general(state.user_input)
    
    def get_last_search_info(self) -> Dict[str, Any]:
        """마지막 검색 정보를 반환합니다."""
        return self.last_search_info.copy()
    
    def search_with_filters(self, query: str, emotion: str, situation: str) -> Optional[str]:
        """
        주어진 쿼리, 감정 필터, 상황 필터를 사용하여 벡터 DB에서 유사한 조언을 검색합니다.
        Args:
            query (str): 검색 쿼리 (사용자 입력).
            emotion (str): 필터링할 감정.
            situation (str): 필터링할 상황.
        Returns:
            Optional[str]: 포맷팅된 검색 결과 문자열 또는 None.
        """
        logger.info(f"필터 검색 실행: 감정='{emotion}', 상황='{situation}'")
        results = self.vector_db.search_similar_advice(
            query, 
            n_results=5, # 상위 5개 결과 검색
            emotion_filter=[emotion], # 감정으로 필터링
            situation_filter=situation # 상황으로 필터링
        )
        
        # 검색 정보 저장
        self.last_search_info = {
            "query": query,
            "filters": {"emotion": emotion, "situation": situation},
            "search_type": "filtered",
            "results": results
        }
        
        return self.format_results(results)
    
    def search_with_emotion_filter(self, query: str, emotion: str) -> Optional[str]:
        """
        주어진 쿼리와 감정 필터를 사용하여 벡터 DB에서 유사한 조언을 검색합니다.
        Args:
            query (str): 검색 쿼리.
            emotion (str): 필터링할 감정.
        Returns:
            Optional[str]: 포맷팅된 검색 결과 문자열 또는 None.
        """
        logger.info(f"감정 필터 검색 실행: 감정='{emotion}'")
        results = self.vector_db.search_similar_advice(
            query, 
            n_results=5,
            emotion_filter=[emotion] # 감정으로만 필터링
        )
        
        # 검색 정보 저장
        self.last_search_info = {
            "query": query,
            "filters": {"emotion": emotion},
            "search_type": "emotion_filtered",
            "results": results
        }
        
        return self.format_results(results)
    
    def search_general(self, query: str) -> Optional[str]:
        """
        주어진 쿼리를 사용하여 벡터 DB에서 필터 없이 일반적인 유사 조언을 검색합니다.
        Args:
            query (str): 검색 쿼리.
        Returns:
            Optional[str]: 포맷팅된 검색 결과 문자열 또는 None.
        """
        logger.info("일반 검색 실행")
        results = self.vector_db.search_similar_advice(query, n_results=5)
        
        # 검색 정보 저장
        self.last_search_info = {
            "query": query,
            "filters": {},
            "search_type": "general",
            "results": results
        }
        
        return self.format_results(results)
    
    def format_results(self, results: Dict[str, Any]) -> Optional[str]:
        """
        벡터 DB 검색 결과를 LLM이 활용하기 좋은 문자열 형태로 포맷팅합니다.
        유사도 임계값(0.5)을 적용하여 관련성 높은 결과만 반환합니다.
        Args:
            results (Dict[str, Any]): 벡터 DB 검색 결과 딕셔너리.
        Returns:
            Optional[str]: 포맷팅된 검색 결과 문자열 (각 항목에 유사도 포함) 또는 None.
        """
        if not results or not results.get("documents"): # 결과가 없거나 문서가 비어있으면 None 반환
            return None
        
        filtered_advice = [] # 필터링된 조언 목록
        similarity_scores = [] # 해당 조언들의 유사도 점수 목록
        search_details = [] # 검색 상세 정보
        
        # 검색된 문서와 거리(distance)를 순회하며 유사도 임계값 적용
        for i, (doc, dist) in enumerate(zip(results["documents"][0], results["distances"][0])):
            similarity = 1 - dist # 거리를 유사도로 변환 (0~1 사이 값)
            if similarity >= 0.5:  # 유사도 임계값 0.5 이상인 경우만 포함
                filtered_advice.append(doc)
                similarity_scores.append(f"{similarity:.3f}") # 소수점 3자리까지 포맷팅
                search_details.append(f"검색 결과 #{i+1}: 유사도 {similarity:.3f}")
        
        if not filtered_advice: # 필터링 후 남은 조언이 없으면 None 반환
            return None
            
        # 검색 과정 요약 정보 추가
        total_searched = len(results["documents"][0])
        total_filtered = len(filtered_advice)
        search_summary = f"🔍 RAG 검색 결과: 총 {total_searched}개 중 {total_filtered}개 선택 (유사도 0.5 이상)\n"
        
        # 각 조언과 해당 유사도 점수를 함께 포맷팅하여 리스트 생성
        rag_data_with_scores = []
        for i, (advice, score) in enumerate(zip(filtered_advice, similarity_scores)):
            rag_data_with_scores.append(f"[유사도: {score}] {advice}")
        
        # 포맷팅된 조언들을 개행 문자와 하이픈으로 연결하여 하나의 문자열로 반환
        formatted_advice = "\n- ".join(rag_data_with_scores)
        
        # 최종 결과에 검색 요약과 상세 정보 포함
        final_result = f"{search_summary}{formatted_advice}"
        
        return final_result


class ResponseGenerationTool:
    """
    LLM을 사용하여 최종 사용자 응답을 생성하는 도구입니다.
    RAG 데이터 유무 및 의도에 따라 다른 프롬프트를 사용합니다.
    """
    def __init__(self, llm_service: LLMService):
        """
        ResponseGenerationTool을 초기화합니다.
        Args:
            llm_service (LLMService): LLM과 통신하기 위한 서비스 객체.
        """
        self.llm_service = llm_service
    
    def execute(self, state: AgentState, rag_data: Optional[str] = None) -> str:
        """
        현재 에이전트 상태와 RAG 데이터를 기반으로 적절한 응답을 생성합니다.
        - 복합 사건: RAG 데이터가 있으면 'response_with_rag', 없으면 'response_without_rag' 사용
        - 단순 감정: 'response_simple_emotion' 사용
        - 그 외: 기본 안내 메시지 반환
        Args:
            state (AgentState): 현재 에이전트의 상태 객체.
            rag_data (Optional[str]): RAG 검색을 통해 얻은 데이터 (있을 수도, 없을 수도 있음).
        Returns:
            str: LLM이 생성한 최종 응답 문자열.
        """
        # 대화 이력을 문자열로 포맷팅
        history_str = "\n".join([f"{c['role']}: {c['content']}" for c in state.history])
        
        # 의도에 따라 다른 프롬프트 로드 및 포맷팅
        if state.intent in ['Complex Event', '복합 사건 서술 (Complex Event)']:
            if rag_data: # RAG 데이터가 있는 경우
                prompt = load_prompt("response_with_rag").format(
                    user_input=state.user_input,
                    rag_data=rag_data, # RAG 데이터를 프롬프트에 포함
                    conversation_history=history_str
                )
            else: # RAG 데이터가 없는 경우 (RAG 검색 결과가 없거나 유사도 임계값 미달)
                prompt = load_prompt("response_without_rag").format(
                    user_input=state.user_input,
                    conversation_history=history_str
                )
        elif state.intent in ['Simple Emotion', '단순 감정 표현 (Simple Emotion)']:
            prompt = load_prompt("response_simple_emotion").format(
                user_input=state.user_input,
                conversation_history=history_str
            )
        else: # 정의되지 않거나 에러 상태의 의도인 경우
            return "어떤 말씀을 하시는지 더 자세히 설명해주실 수 있나요?" # 기본 응답
        
        return self.llm_service.get_response(prompt) # LLM에 응답 생성 요청


class ClarifyTool:
    """
    사용자 입력이 모호하거나 불분명할 때, 명확화를 요청하는 응답을 생성하는 도구입니다.
    """
    def execute(self, state: AgentState) -> str:
        """
        모호한 입력에 대한 명확화 요청 메시지를 반환합니다.
        Args:
            state (AgentState): 현재 에이전트의 상태 객체 (여기서는 직접 사용되지 않음).
        Returns:
            str: 명확화 요청 메시지.
        """
        return "어떤 말씀을 하시는지 더 자세히 설명해주실 수 있나요? 오늘 있었던 일이나 감정에 대해 조금 더 구체적으로 이야기해주시면 제가 더 잘 이해하고 도울 수 있을 것 같아요."


class MainAgent:
    """
    자율적 의사결정과 동적 전략 수립을 담당하는 메인 에이전트입니다.
    
    Perceive-Decide-Act 사이클을 통해 사용자 입력에 대한 적절한 응답을 생성합니다.
    - Perceive (인지): 사용자 입력과 대화 이력을 기반으로 현재 상태를 파악합니다.
    - Decide (결정): 인지된 상태를 바탕으로 어떤 전략(도구 사용)을 실행할지 결정합니다.
    - Act (실행): 결정된 전략에 따라 실제 도구들을 호출하여 응답을 생성합니다.
    """
    
    def __init__(self, user_id: str):
        """
        MainAgent 인스턴스를 초기화합니다.
        Args:
            user_id (str): 사용자 식별자.
        """
        self.user_id = user_id
        self.state = AgentState() # 에이전트의 현재 상태를 관리하는 객체
        self.is_initialized = False # 초기화 완료 여부
        
        # 도구들 초기화
        self.llm_service = LLMService() # LLM과의 통신을 담당하는 서비스
        self.vector_db = VectorDatabase() # RAG를 위한 벡터 데이터베이스 서비스
        self.conversation_manager = ConversationManager() # 사용자 대화 이력을 관리하는 서비스
        
        # 도구들을 딕셔너리로 관리
        self.tools = {
            'conversation_management': ConversationManagementTool(self.llm_service),
            'rag': RAGTool(self.vector_db),
            'response_generation': ResponseGenerationTool(self.llm_service),
            'clarify': ClarifyTool()
        }
        
        # RAG 검색 정보 저장
        self.last_rag_info = {}
    
    def initialize(self):
        """
        에이전트를 사용하기 전에 필요한 초기화 작업을 수행합니다.
        주로 벡터 데이터베이스 초기화와 같은 외부 서비스 준비를 포함합니다.
        """
        try:
            logger.info(f"MainAgent for user '{self.user_id}' initializing...")
            self.vector_db.initialize() # 벡터 DB 초기화
            self.is_initialized = True
            logger.info(f"✅ MainAgent for user '{self.user_id}' initialized.")
        except Exception as e:
            logger.error(f"❌ MainAgent initialization failed: {e}", exc_info=True) # 초기화 실패 시 에러 로그
            self.is_initialized = False
            raise # 초기화 실패는 심각한 오류이므로 예외 다시 발생
    
    def perceive(self, user_input: str) -> AgentState:
        """
        Perceive (인지) 단계:
        사용자 입력과 최신 대화 이력을 가져와 에이전트의 내부 상태(AgentState)를 구성합니다.
        Args:
            user_input (str): 현재 사용자 입력.
        Returns:
            AgentState: 업데이트된 에이전트 상태 객체.
        """
        # 대화 관리자로부터 최근 대화 이력 10개 가져오기
        history = self.conversation_manager.get_recent_conversation(self.user_id, count=10)
        self.state.update(user_input, history) # AgentState 업데이트
        logger.info(f"상태 인지 완료: 복잡도={self.state.complexity_score:.2f}, 모호성={self.state.ambiguity_level:.2f}")
        return self.state
    
    def decide(self) -> List[str]:
        """
        Decide (결정) 단계:
        현재 에이전트 상태를 기반으로 어떤 도구(들)를 실행할지 '실행 계획(plan)'을 수립합니다.
        - ConversationManagementTool을 사용하여 사용자 의도를 먼저 분석합니다.
        - 의도 분석 결과 및 자체적인 모호성/복잡도 판단에 따라 동적으로 전략을 결정합니다.
        Returns:
            List[str]: 실행할 도구 이름(문자열)의 리스트.
        """
        # 1. 대화 관리 도구(LLM)를 사용하여 사용자 의도, 감정, 상황을 분석
        analysis_result = self.tools['conversation_management'].analyze(self.state)
        self.state.update_with_result(analysis_result) # 분석 결과를 에이전트 상태에 반영
        
        intent = analysis_result.get('intent', 'Error') # 분석된 의도 가져오기 (기본값 'Error')
        logger.info(f"의도 분석 결과: {intent}")
        
        # 2. 분석된 의도 및 상태에 따른 동적 전략 수립
        if self.state.requires_clarification or intent in ['Ambiguous', '모호함 (Ambiguous)']:
            # 입력이 너무 모호하거나 LLM이 모호하다고 판단한 경우, 명확화 요청
            plan = ['clarify']
        elif intent in ['Complex Event', '복합 사건 서술 (Complex Event)']:
            # 복합 사건 서술의 경우, RAG 검색 후 응답 생성
            plan = ['rag', 'response_generation']
        elif intent in ['Simple Emotion', '단순 감정 표현 (Simple Emotion)']:
            # 단순 감정 표현의 경우, RAG 없이 바로 응답 생성 (공감 위주)
            plan = ['response_generation']
        else:
            # 그 외의 경우 (예: Error 또는 예상치 못한 의도), 기본 응답 생성
            plan = ['response_generation']
        
        logger.info(f"실행 계획: {plan}")
        return plan
    
    def act(self, plan: List[str]) -> Dict[str, Any]:
        """
        Act (실행) 단계:
        수립된 '실행 계획(plan)'에 따라 지정된 도구들을 순차적으로 실행합니다.
        각 도구의 실행 결과를 저장하고, 특히 RAG 데이터는 응답 생성 도구에 전달합니다.
        Args:
            plan (List[str]): 실행할 도구 이름의 리스트.
        Returns:
            Dict[str, Any]: 각 도구 실행 결과가 담긴 딕셔너리.
        """
        results: Dict[str, Any] = {} # 각 도구의 실행 결과를 저장할 딕셔너리
        rag_data: Optional[str] = None # RAG 검색 결과를 저장할 변수
        
        for tool_name in plan: # 계획에 따라 도구들을 순회하며 실행
            try:
                if tool_name == 'rag':
                    rag_data = self.tools[tool_name].execute(self.state) # RAG 도구 실행
                    results['rag_data'] = rag_data # 결과 저장
                    
                    # RAG 검색 정보 수집
                    rag_tool = self.tools[tool_name]
                    self.last_rag_info = rag_tool.get_last_search_info()
                    results['rag_info'] = self.last_rag_info
                    
                elif tool_name == 'response_generation':
                    # 응답 생성 도구는 RAG 데이터를 인자로 받음
                    response = self.tools[tool_name].execute(self.state, rag_data) 
                    results['response'] = response # 최종 응답 저장
                else:
                    # 그 외 도구들 실행 (예: 'clarify' 등)
                    result = self.tools[tool_name].execute(self.state)
                    results[tool_name] = result # 결과 저장
                
                logger.info(f"도구 '{tool_name}' 실행 완료")
                
            except Exception as e:
                logger.error(f"도구 '{tool_name}' 실행 실패: {e}", exc_info=True) # 도구 실행 실패 시 에러 로그
                results[tool_name] = f"도구 실행 중 오류 발생: {e}" # 오류 메시지 저장
        
        return results
    
    def get_response(self, user_input: str) -> Dict[str, Any]:
        """
        사용자 입력에 대한 챗봇의 최종 응답을 생성하는 메인 인터페이스 메서드입니다.
        Perceive-Decide-Act 사이클의 전체 과정을 조율합니다.
        Args:
            user_input (str): 사용자로부터 받은 텍스트 입력.
        Returns:
            Dict[str, Any]: 응답 성공 여부 ('success')와 최종 응답 메시지 ('response')를 포함하는 딕셔너리.
        """
        if not self.is_initialized:
            # 에이전트가 초기화되지 않았다면 오류 메시지 반환
            return {"success": False, "response": "에이전트가 초기화되지 않았습니다."}
        
        try:
            # 1. Perceive: 사용자 입력과 대화 이력을 바탕으로 현재 상태를 인지
            self.perceive(user_input)
            
            # 2. Decide: 인지된 상태를 기반으로 실행할 계획(도구 목록)을 결정
            plan = self.decide()
            
            # 3. Act: 결정된 계획에 따라 도구들을 순차적으로 실행하여 결과 도출
            results = self.act(plan)
            
            # 4. 최종 응답 추출 및 대화 이력 저장
            # 'response' 키에 최종 응답이 없으면 'clarify' 키의 메시지를 사용하거나, 최종 기본 오류 메시지 사용
            response = results.get('response', results.get('clarify', "죄송합니다. 응답을 생성할 수 없습니다."))
            
            # 사용자 입력과 에이전트 응답을 대화 이력에 추가
            self.conversation_manager.add_to_conversation(self.user_id, 'user', user_input)
            self.conversation_manager.add_to_conversation(self.user_id, 'assistant', response)
            
            return {"success": True, "response": response} # 성공 응답 반환
            
        except Exception as e:
            logger.error(f"❌ MainAgent 응답 생성 실패: {e}", exc_info=True) # 전체 프로세스 실패 시 에러 로그
            return {"success": False, "response": "죄송합니다. 답변을 생성하는 동안 오류가 발생했습니다."}
    
    def end_conversation(self) -> Dict[str, Any]:
        """
        현재 대화를 종료하고 대화 요약을 생성합니다.
        대화 이력을 LLM에 전달하여 요약을 요청한 후, 대화 이력을 초기화합니다.
        Returns:
            Dict[str, Any]: 성공 여부와 대화 요약 메시지를 포함하는 딕셔너리.
        """
        if not self.is_initialized:
            return {"success": False, "response": "에이전트가 초기화되지 않았습니다."}
        
        try:
            # 전체 대화 이력 가져오기
            conversation_history = self.conversation_manager.get_recent_conversation(
                self.user_id, count=self.conversation_manager.max_history_length
            )
            
            if not conversation_history: # 대화 이력이 없으면 기본 종료 메시지 반환
                return {"success": True, "response": "나중에 또 만나요! 언제든지 다시 찾아주세요."}
            
            # 대화 이력을 역순으로 정렬하여 프롬프트에 적합하게 포맷팅
            history_str = "\n".join([f"{c['role']}: {c['content']}" for c in reversed(conversation_history)])
            prompt = load_prompt("conversation_summary").format(conversation_history=history_str)
            summary_response = self.llm_service.get_response(prompt) # LLM에 요약 요청
            
            self.conversation_manager.clear_conversation_history(self.user_id) # 대화 이력 초기화
            
            return {"success": True, "response": summary_response} # 요약된 응답 반환
            
        except Exception as e:
            logger.error(f"❌ 대화 종료 처리 실패: {e}", exc_info=True) # 대화 종료 중 오류 발생 시 에러 로그
            return {"success": False, "response": "대화를 마무리하는 중 오류가 발생했습니다."}