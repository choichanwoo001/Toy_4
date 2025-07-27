from typing import List, Dict, Any, Optional, Tuple
import logging
from datetime import datetime, timedelta
import re

from ..models.diary import DiarySearchQuery, SearchResult, RAGResponse
from ..db.chroma_client import ChromaClient
from .embedding import EmbeddingService

logger = logging.getLogger(__name__)

class RAGAgent:
    def __init__(self):
        """RAG 에이전트 초기화"""
        self.chroma_client = ChromaClient()
        self.embedding_service = EmbeddingService()
        
        # 감정 키워드 매핑
        self.emotion_keywords = {
            "우울": ["우울", "슬픔", "절망", "무기력", "우울함"],
            "기쁨": ["기쁨", "행복", "즐거움", "신남", "기쁨"],
            "화남": ["화남", "분노", "짜증", "열받음", "화남"],
            "불안": ["불안", "걱정", "긴장", "스트레스", "불안함"],
            "평온": ["평온", "차분", "안정", "평화", "평온함"]
        }
        
        # 시간 컨텍스트 매핑
        self.time_patterns = {
            "오늘": 1,
            "어제": 2,
            "이번_주": 7,
            "지난_주": 14,
            "이번_달": 30
        }
    
    def analyze_user_input(self, user_input: str) -> DiarySearchQuery:
        """사용자 입력 분석"""
        try:
            # 감정 추출
            inferred_emotion = self._extract_emotion(user_input)
            
            # 상황 추출
            inferred_situation = self._extract_situation(user_input)
            
            # 시간 컨텍스트 추출
            time_context = self._extract_time_context(user_input)
            
            return DiarySearchQuery(
                user_utterance=user_input,
                inferred_emotion=inferred_emotion,
                inferred_situation=inferred_situation,
                time_context=time_context
            )
        except Exception as e:
            logger.error(f"사용자 입력 분석 중 오류: {e}")
            raise
    
    def _extract_emotion(self, text: str) -> Optional[str]:
        """감정 키워드 추출"""
        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    return emotion
        return None
    
    def _extract_situation(self, text: str) -> Optional[str]:
        """상황 키워드 추출"""
        situation_keywords = {
            "업무": ["회사", "업무", "직장", "회의", "프로젝트"],
            "가족": ["가족", "부모", "자식", "배우자"],
            "친구": ["친구", "동료", "사람"],
            "건강": ["건강", "병", "아픔", "피곤"]
        }
        
        for situation, keywords in situation_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    return situation
        return None
    
    def _extract_time_context(self, text: str) -> Optional[str]:
        """시간 컨텍스트 추출"""
        for pattern in self.time_patterns.keys():
            if pattern in text:
                return pattern
        return None
    
    def generate_search_query(self, parsed_query: DiarySearchQuery) -> Tuple[List[str], Dict[str, Any]]:
        """검색 쿼리 생성"""
        try:
            # 감정 기반 쿼리 키워드 생성
            query_keywords = []
            if parsed_query.inferred_emotion:
                query_keywords.extend(self.emotion_keywords.get(parsed_query.inferred_emotion, []))
            
            # 사용자 발화에서 키워드 추출
            words = parsed_query.user_utterance.split()
            query_keywords.extend([word for word in words if len(word) > 1])
            
            # 중복 제거
            query_keywords = list(set(query_keywords))
            
            # 필터 조건 생성
            where_filter = {}
            if parsed_query.inferred_situation:
                where_filter["context"] = parsed_query.inferred_situation
            
            # 시간 필터 추가
            if parsed_query.time_context:
                days_back = self.time_patterns.get(parsed_query.time_context, 7)
                end_date = datetime.now().strftime("%Y-%m-%d")
                start_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
                where_filter["date"] = {"$gte": start_date, "$lte": end_date}
            
            return query_keywords, where_filter
        except Exception as e:
            logger.error(f"검색 쿼리 생성 중 오류: {e}")
            raise
    
    def search_diary_entries(self, query_keywords: List[str], where_filter: Dict[str, Any], 
                           n_results: int = 15) -> List[SearchResult]:
        """일기 엔트리 검색"""
        try:
            # 쿼리 임베딩 생성
            query_text = " ".join(query_keywords)
            query_embedding = self.embedding_service.encode(query_text)
            
            # ChromaDB 검색
            search_results = self.chroma_client.search(
                query_embeddings=[query_embedding],
                n_results=n_results,
                where_filter=where_filter if where_filter else None
            )
            
            # 결과가 없으면 필터 없이 재검색
            if not search_results["documents"][0]:
                logger.info("필터된 검색 결과 없음, 전체 검색 시도")
                search_results = self.chroma_client.search(
                    query_embeddings=[query_embedding],
                    n_results=n_results
                )
            
            # 유사도 점수 계산 및 정렬
            scored_results = []
            for i, (doc, emb, meta) in enumerate(zip(
                search_results["documents"][0],
                search_results["embeddings"][0],
                search_results["metadatas"][0]
            )):
                similarity = self.embedding_service.cosine_similarity(query_embedding, emb)
                scored_results.append(SearchResult(
                    content=doc,
                    similarity_score=similarity,
                    metadata=meta
                ))
            
            # 유사도 순으로 정렬
            scored_results.sort(key=lambda x: x.similarity_score, reverse=True)
            
            return scored_results[:5]  # 상위 5개 반환
        except Exception as e:
            logger.error(f"일기 검색 중 오류: {e}")
            raise
    
    def generate_response(self, user_input: str, related_entries: List[SearchResult]) -> RAGResponse:
        """RAG 응답 생성"""
        try:
            # 관련 엔트리 요약
            context_summary = ""
            if related_entries:
                context_summary = "\n".join([
                    f"{entry.metadata.get('date', 'N/A')}: {entry.content} (감정: {entry.metadata.get('emotion', 'N/A')})"
                    for entry in related_entries
                ])
            
            # 분석 텍스트 생성 (실제로는 LLM을 사용해야 함)
            analysis = self._generate_analysis_text(user_input, context_summary, related_entries)
            
            # 신뢰도 점수 계산
            confidence_score = self._calculate_confidence(related_entries)
            
            return RAGResponse(
                analysis=analysis,
                related_entries=related_entries,
                confidence_score=confidence_score
            )
        except Exception as e:
            logger.error(f"응답 생성 중 오류: {e}")
            raise
    
    def _generate_analysis_text(self, user_input: str, context_summary: str, 
                              related_entries: List[SearchResult]) -> str:
        """분석 텍스트 생성 (간단한 버전)"""
        if not related_entries:
            return "관련된 일기 기록을 찾을 수 없어서 구체적인 분석을 제공하기 어렵습니다."
        
        # 평균 유사도 계산
        avg_similarity = sum(entry.similarity_score for entry in related_entries) / len(related_entries)
        
        # 감정 패턴 분석
        emotions = [entry.metadata.get('emotion', '') for entry in related_entries]
        emotion_counts = {}
        for emotion in emotions:
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        
        most_common_emotion = max(emotion_counts.items(), key=lambda x: x[1])[0] if emotion_counts else "알 수 없음"
        
        analysis = f"""
사용자 발화: "{user_input}"

분석 결과:
- 관련 일기 {len(related_entries)}개 발견
- 평균 유사도: {avg_similarity:.3f}
- 주요 감정 패턴: {most_common_emotion}

관련 일기 기록:
{context_summary}

이러한 패턴을 보면 {most_common_emotion}한 감정이 반복적으로 나타나고 있습니다.
"""
        return analysis.strip()
    
    def _calculate_confidence(self, related_entries: List[SearchResult]) -> float:
        """신뢰도 점수 계산"""
        if not related_entries:
            return 0.0
        
        # 평균 유사도와 결과 개수를 기반으로 신뢰도 계산
        avg_similarity = sum(entry.similarity_score for entry in related_entries) / len(related_entries)
        result_count_factor = min(len(related_entries) / 5.0, 1.0)  # 최대 5개 기준
        
        confidence = (avg_similarity * 0.7) + (result_count_factor * 0.3)
        return min(confidence, 1.0)
    
    def process_query(self, user_input: str) -> RAGResponse:
        """전체 RAG 처리 파이프라인"""
        try:
            # 1. 사용자 입력 분석
            parsed_query = self.analyze_user_input(user_input)
            logger.info(f"분석된 쿼리: {parsed_query}")
            
            # 2. 검색 쿼리 생성
            query_keywords, where_filter = self.generate_search_query(parsed_query)
            logger.info(f"검색 키워드: {query_keywords}, 필터: {where_filter}")
            
            # 3. 일기 검색
            related_entries = self.search_diary_entries(query_keywords, where_filter)
            logger.info(f"검색된 엔트리 수: {len(related_entries)}")
            
            # 4. 응답 생성
            response = self.generate_response(user_input, related_entries)
            logger.info(f"응답 생성 완료, 신뢰도: {response.confidence_score}")
            
            return response
        except Exception as e:
            logger.error(f"RAG 처리 중 오류: {e}")
            raise 