"""
일기 기반 조언 시스템 메인 애플리케이션
벡터DB 검색과 GPT를 결합한 개인화된 조언 제공

이 모듈은 사용자의 일기 내용을 받아서 다음과 같은 방식으로 조언을 생성합니다:
1. RAG 방식: 벡터 검색으로 유사한 조언을 찾고, GPT로 개인화된 조언 생성
2. 프롬프트 방식: GPT만으로 직접 조언 생성
3. 비교 방식: 두 방식을 모두 사용하여 결과 비교

주요 구성 요소:
- DiaryAdvisorSystem: 전체 시스템을 관리하는 메인 클래스
- VectorDatabase: 벡터 검색을 담당
- GPTAdvisor: GPT 기반 조언 생성
- PromptAdvisor: 프롬프트 기반 조언 생성 및 감정/상황 분석
"""

# 필요한 라이브러리 임포트
import logging  # 로그 출력을 위한 모듈
from typing import Dict, Any  # 타입 힌트를 위한 타입 정의
import sys  # 시스템 경로 조작
import os  # 파일 시스템 접근
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 상위 디렉토리를 Python 경로에 추가

# 프로젝트 내부 모듈들 임포트
from core.vector_db import VectorDatabase  # 벡터 데이터베이스 관리
from core.gpt_advisor import GPTAdvisor  # GPT 기반 조언 생성
from core.prompt_advisor import PromptAdvisor  # 프롬프트 기반 조언 생성
from config.config import Config  # 시스템 설정

# 로깅 설정 - INFO 레벨 이상의 로그를 출력
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # 현재 모듈의 로거 생성

class DiaryAdvisorSystem:
    """
    일기 조언 시스템의 메인 클래스
    
    이 클래스는 사용자의 일기 내용을 받아서 다양한 방식으로 조언을 생성합니다.
    RAG(Retrieval-Augmented Generation)와 프롬프트 기반 방식을 모두 지원하며,
    벡터 데이터베이스에서 유사한 조언을 검색하고 GPT로 개인화된 조언을 생성합니다.
    
    Attributes:
        config (Config): 시스템 설정 객체
        vector_db (VectorDatabase): 벡터 데이터베이스 객체
        gpt_advisor (GPTAdvisor): GPT 기반 조언 생성 객체
        prompt_advisor (PromptAdvisor): 프롬프트 기반 조언 생성 객체
        is_initialized (bool): 시스템 초기화 완료 여부
    """
    
    def __init__(self):
        """
        일기 조언 시스템 초기화
        
        시스템의 각 구성 요소들을 None으로 초기화합니다.
        실제 초기화는 initialize() 메서드에서 진행됩니다.
        """
        self.config = Config()  # 설정 파일에서 설정값 로드
        self.vector_db = None  # 벡터 데이터베이스 객체 (초기에는 None)
        self.gpt_advisor = None  # GPT 조언자 객체 (초기에는 None)
        self.prompt_advisor = None  # 프롬프트 조언자 객체 (초기에는 None)
        self.is_initialized = False  # 초기화 완료 여부 플래그
    
    def initialize(self):
        """
        전체 시스템 초기화
        
        이 메서드는 시스템의 모든 구성 요소를 초기화합니다:
        1. 벡터 데이터베이스 초기화 (ChromaDB 연결 및 모델 로딩)
        2. GPT 조언자 초기화 (OpenAI API 연결)
        3. 프롬프트 조언자 초기화 (감정/상황 분석용)
        
        Raises:
            Exception: 초기화 중 오류가 발생한 경우
        """
        try:
            logger.info("일기 조언 시스템 초기화 시작...")
            
            # 1. 벡터 데이터베이스 초기화
            logger.info("1. 벡터 데이터베이스 초기화 중...")
            self.vector_db = VectorDatabase()  # 벡터 데이터베이스 객체 생성
            self.vector_db.initialize()  # ChromaDB 연결 및 임베딩 모델 로딩
            
            # 기존 데이터베이스 정보 확인
            db_info = self.vector_db.get_collection_info()
            logger.info(f"기존 데이터베이스에서 {db_info['count']}개의 조언을 로드했습니다.")
            
            # 2. GPT 조언자 초기화
            logger.info("2. GPT 조언자 초기화 중...")
            self.gpt_advisor = GPTAdvisor()  # GPT 조언자 객체 생성
            
            # 3. 프롬프트 조언자 초기화
            logger.info("3. 프롬프트 조언자 초기화 중...")
            self.prompt_advisor = PromptAdvisor()  # 프롬프트 조언자 객체 생성
            
            self.is_initialized = True  # 초기화 완료 플래그 설정
            logger.info("✅ 일기 조언 시스템 초기화 완료!")
            
            # 시스템 정보 출력
            db_info = self.vector_db.get_collection_info()
            logger.info(f"📊 데이터베이스 정보: {db_info}")
            
        except Exception as e:
            logger.error(f"❌ 시스템 초기화 실패: {e}")
            self.is_initialized = False
            raise  # 오류를 다시 발생시켜 상위에서 처리할 수 있도록 함
    
    def get_advice_rag(self, user_diary: str) -> Dict[str, Any]:
        """
        RAG 기반 사용자 일기에 대한 조언 생성
        
        RAG(Retrieval-Augmented Generation) 방식으로 조언을 생성합니다:
        1. 일기 내용에서 감정과 상황을 자동 분석
        2. 분석된 감정/상황으로 벡터 데이터베이스에서 유사한 조언 검색
        3. 검색된 조언들을 바탕으로 GPT가 개인화된 조언 생성
        
        Args:
            user_diary (str): 사용자가 작성한 일기 내용
            
        Returns:
            Dict[str, Any]: 조언 생성 결과
                - success (bool): 성공 여부
                - advice (str): 생성된 조언 (성공 시)
                - similar_advice (list): 검색된 유사 조언들 (성공 시)
                - emotion (str): 분석된 감정 카테고리 (성공 시)
                - situation (str): 분석된 상황 카테고리 (성공 시)
                - error (str): 오류 메시지 (실패 시)
        """
        # 시스템 초기화 확인
        if not self.is_initialized:
            return {
                "success": False,
                "error": "시스템이 초기화되지 않았습니다.",
                "advice": None,
                "similar_advice": None
            }
        
        try:
            logger.info("조언 생성 프로세스 시작...")
            
            # 1. 일기 내용에서 감정과 상황 분석
            logger.info("1. 감정과 상황 분석 중...")
            analysis_result = self.prompt_advisor.analyze_emotion_and_situation(user_diary)
            
            # 분석 결과에 따른 필터 설정
            emotion_filter = None
            situation_filter = None
            
            if analysis_result["success"]:
                emotion_filter = [analysis_result["emotion"]]  # 감정 필터 설정
                situation_filter = analysis_result["situation"]  # 상황 필터 설정
                logger.info(f"분석된 감정: {analysis_result['emotion']}, 상황: {analysis_result['situation']}")
            else:
                logger.warning(f"감정/상황 분석 실패: {analysis_result.get('error', 'Unknown error')}")
            
            # 필터링 결과가 없을 경우를 대비해 감정만으로도 검색해보기 위한 fallback 설정
            fallback_emotion_filter = emotion_filter
            fallback_situation_filter = None
            
            # 2. 일기 내용 벡터화 및 유사 조언 검색 (필터링 적용)
            logger.info("2. 유사한 조언 검색 중...")
            
            # 먼저 필터링 없이 검색해서 데이터가 있는지 확인
            logger.info("2-1. 필터링 없이 전체 검색 중...")
            all_search_results = self.vector_db.search_similar_advice(user_diary)
            logger.info(f"전체 검색 결과: {len(all_search_results['documents'][0])}개")
            
            # 필터링 적용하여 검색
            logger.info("2-2. 필터링 적용하여 검색 중...")
            search_results = self.vector_db.search_similar_advice(
                user_diary, 
                emotion_filter=emotion_filter, 
                situation_filter=situation_filter
            )
            logger.info(f"필터링 검색 결과: {len(search_results['documents'][0])}개")
            
            # 필터링 결과가 없으면 감정만으로 재검색 (단계별 fallback 전략)
            if not search_results["documents"][0] and fallback_emotion_filter:
                logger.info("감정과 상황 모두 필터링 결과가 없어서 감정만으로 재검색합니다.")
                search_results = self.vector_db.search_similar_advice(
                    user_diary, 
                    emotion_filter=fallback_emotion_filter, 
                    situation_filter=fallback_situation_filter
                )
                logger.info(f"감정만 필터링 검색 결과: {len(search_results['documents'][0])}개")
            
            # 그래도 결과가 없으면 전체 검색 결과 사용 (최종 fallback)
            if not search_results["documents"][0] and all_search_results["documents"][0]:
                logger.info("모든 필터링 결과가 없어서 전체 검색 결과를 사용합니다.")
                search_results = all_search_results
            
            # 3. 검색 결과 확인 (유사도 점수 포함)
            similar_advice = []
            if search_results["documents"][0]:
                for i, (doc, meta, distance) in enumerate(zip(
                    search_results["documents"][0], 
                    search_results["metadatas"][0],
                    search_results["distances"][0]
                )):
                    # 거리를 유사도 점수로 변환 (0~1 범위, 1에 가까울수록 유사)
                    similarity_score = 1 - distance
                    similar_advice.append({
                        "content": doc,  # 조언 내용
                        "metadata": meta,  # 메타데이터 (감정, 상황 등)
                        "similarity_rank": i + 1,  # 유사도 순위
                        "similarity_score": similarity_score,  # 유사도 점수
                        "distance": distance  # 원본 거리 값
                    })
                logger.info(f"검색된 유사 조언: {len(similar_advice)}개")
            else:
                logger.info("유사한 조언을 찾지 못했습니다.")
            
            # 4. GPT를 사용한 개인화된 조언 생성
            logger.info("4. 개인화된 조언 생성 중...")
            
            if similar_advice:
                # 유사한 조언이 있으면 그것을 참고하여 개인화된 조언 생성
                advice = self.gpt_advisor.generate_advice(user_diary, search_results)
            else:
                # 검색 결과가 없을 때는 단순 조언 생성
                advice = self.gpt_advisor.generate_simple_advice(user_diary)
            
            logger.info("✅ 조언 생성 완료!")
            
            # 성공 결과 반환
            return {
                "success": True,
                "advice": advice,  # 생성된 조언
                "similar_advice": similar_advice,  # 검색된 유사 조언들
                "emotion": analysis_result.get("emotion") if analysis_result["success"] else None,  # 분석된 감정
                "situation": analysis_result.get("situation") if analysis_result["success"] else None,  # 분석된 상황
                "error": None
            }
            
        except Exception as e:
            # 오류 발생 시 로그 기록 및 오류 결과 반환
            logger.error(f"❌ 조언 생성 실패: {e}")
            return {
                "success": False,
                "error": str(e),  # 오류 메시지
                "advice": None,
                "similar_advice": None
            }
    
    def add_new_advice(self, content: str, metadata: Dict[str, str]) -> bool:
        """
        새로운 조언을 데이터베이스에 추가
        
        사용자가 새로운 조언을 추가할 때 사용합니다.
        조언 내용과 메타데이터를 받아서 벡터 데이터베이스에 저장합니다.
        
        Args:
            content (str): 추가할 조언 내용
            metadata (Dict[str, str]): 조언의 메타데이터 (감정, 상황 등)
            
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        if not self.is_initialized:
            logger.error("시스템이 초기화되지 않았습니다.")
            return False
        
        try:
            import uuid  # 고유 ID 생성을 위한 모듈
            advice_data = {
                "id": f"advice_{uuid.uuid4().hex[:8]}",  # 고유 ID 생성
                "content": content,  # 조언 내용
                "metadata": metadata  # 메타데이터
            }
            
            return self.vector_db.add_advice(advice_data)  # 벡터 데이터베이스에 추가
            
        except Exception as e:
            logger.error(f"조언 추가 실패: {e}")
            return False
    
    def get_system_info(self) -> Dict[str, Any]:
        """
        시스템 정보 반환
        
        현재 시스템의 상태와 설정 정보를 반환합니다.
        
        Returns:
            Dict[str, Any]: 시스템 정보
                - initialized (bool): 초기화 완료 여부
                - database (dict): 데이터베이스 정보
                - embedding_model (str): 사용중인 임베딩 모델
                - gpt_model (str): 사용중인 GPT 모델
        """
        if not self.is_initialized:
            return {"initialized": False}
        
        try:
            db_info = self.vector_db.get_collection_info()  # 데이터베이스 정보 조회
            return {
                "initialized": True,
                "database": db_info,  # 데이터베이스 정보
                "embedding_model": self.config.EMBEDDING_MODEL,  # 임베딩 모델명
                "gpt_model": self.config.GPT_MODEL  # GPT 모델명
            }
        except Exception as e:
            logger.error(f"시스템 정보 조회 실패: {e}")
            return {"initialized": True, "error": str(e)}
    
    def get_advice_prompt(self, user_diary: str) -> Dict[str, Any]:
        """
        프롬프트 기반 사용자 일기에 대한 조언 생성
        
        RAG 없이 순수하게 GPT만을 사용하여 조언을 생성합니다.
        벡터 검색 없이 직접 일기 내용을 GPT에 전달하여 조언을 받습니다.
        
        Args:
            user_diary (str): 사용자가 작성한 일기 내용
            
        Returns:
            Dict[str, Any]: 조언 생성 결과
                - success (bool): 성공 여부
                - advice (str): 생성된 조언 (성공 시)
                - method (str): 사용된 방법 ("prompt_only")
                - tokens_used (int): 사용된 토큰 수 (성공 시)
                - error (str): 오류 메시지 (실패 시)
        """
        if not self.is_initialized:
            return {
                "success": False,
                "error": "시스템이 초기화되지 않았습니다.",
                "advice": None,
                "method": "prompt_only"
            }
        
        try:
            logger.info("프롬프트 기반 조언 생성 프로세스 시작...")
            
            # 프롬프트 기반 조언 생성
            result = self.prompt_advisor.generate_advice(user_diary)
            
            logger.info("✅ 프롬프트 기반 조언 생성 완료!")
            return result
            
        except Exception as e:
            logger.error(f"❌ 프롬프트 기반 조언 생성 실패: {e}")
            return {
                "success": False,
                "error": str(e),
                "advice": None,
                "method": "prompt_only"
            }
    
    def get_advice_comparison(self, user_diary: str) -> Dict[str, Any]:
        """
        RAG와 프롬프트 방식 비교 조언 생성
        
        같은 일기 내용에 대해 RAG 방식과 프롬프트 방식을 모두 사용하여
        결과를 비교할 수 있도록 합니다.
        
        Args:
            user_diary (str): 사용자가 작성한 일기 내용
            
        Returns:
            Dict[str, Any]: 비교 조언 생성 결과
                - success (bool): 성공 여부
                - rag_result (dict): RAG 방식 결과
                - prompt_result (dict): 프롬프트 방식 결과
                - comparison (dict): 비교 정보
                - error (str): 오류 메시지 (실패 시)
        """
        if not self.is_initialized:
            return {
                "success": False,
                "error": "시스템이 초기화되지 않았습니다."
            }
        
        try:
            logger.info("두 방식 비교 조언 생성 시작...")
            
            # RAG 기반 조언 생성
            rag_result = self.get_advice_rag(user_diary)
            
            # 프롬프트 기반 조언 생성
            prompt_result = self.get_advice_prompt(user_diary)
            
            logger.info("✅ 비교 조언 생성 완료!")
            
            return {
                "success": True,
                "rag_result": rag_result,  # RAG 방식 결과
                "prompt_result": prompt_result,  # 프롬프트 방식 결과
                "comparison": {
                    "rag_success": rag_result["success"],  # RAG 성공 여부
                    "prompt_success": prompt_result["success"],  # 프롬프트 성공 여부
                    "similar_advice_found": len(rag_result.get("similar_advice", [])) if rag_result["success"] else 0  # 찾은 유사 조언 수
                }
            }
            
        except Exception as e:
            logger.error(f"❌ 비교 조언 생성 실패: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_advice(self, user_diary: str, method: str = "rag") -> Dict[str, Any]:
        """
        사용자 일기에 대한 조언 생성 (디폴트는 RAG 방식)
        
        사용자가 선택한 방식에 따라 조언을 생성합니다.
        
        Args:
            user_diary (str): 사용자가 작성한 일기 내용
            method (str): 조언 생성 방식 ("rag", "prompt", "comparison")
            
        Returns:
            Dict[str, Any]: 조언 생성 결과
        """
        if method == "prompt":
            return self.get_advice_prompt(user_diary)  # 프롬프트 방식
        elif method == "comparison":
            return self.get_advice_comparison(user_diary)  # 비교 방식
        else:  # method == "rag" or default
            return self.get_advice_rag(user_diary)  # RAG 방식 (기본값)


def main():
    """
    메인 실행 함수 - 커맨드라인 인터페이스
    
    이 함수는 사용자와의 대화형 인터페이스를 제공합니다.
    사용자가 일기를 입력하면 다양한 방식으로 조언을 생성하고 결과를 표시합니다.
    """
    print("🌟 일기 기반 조언 시스템에 오신 것을 환영합니다! 🌟\n")
    
    try:
        # 시스템 초기화
        advisor_system = DiaryAdvisorSystem()  # 시스템 객체 생성
        advisor_system.initialize()  # 시스템 초기화
        
        # 시스템 정보 출력
        info = advisor_system.get_system_info()  # 시스템 정보 조회
        print(f"📊 시스템 정보:")
        print(f"   - 데이터베이스: {info['database']['count']}개 조언 보유")
        print(f"   - 임베딩 모델: {info['embedding_model']}")
        print(f"   - GPT 모델: {info['gpt_model']}\n")
        
        print("💡 사용법: 일기를 입력하시면 개인화된 조언을 제공합니다.")
        print("종료하려면 '종료' 또는 'quit'을 입력하세요.\n")
        
        # 메인 루프 - 사용자 입력을 계속 받음
        while True:
            # 사용자 입력 받기
            print("-" * 70)  # 구분선 출력
            user_input = input("📝 오늘의 일기를 들려주세요: ").strip()  # 사용자 입력 받기
            
            # 종료 조건 확인
            if user_input.lower() in ['종료', 'quit', 'exit', 'q']:
                print("👋 이용해주셔서 감사합니다!")
                break
            
            # 빈 입력 확인
            if not user_input:
                print("❗ 일기 내용을 입력해주세요.")
                continue
            
            # 조언 방식 선택
            print("\n🔧 조언 방식을 선택해주세요:")
            print("1. 🔍 RAG 방식 (유사 조언 검색 + GPT)")
            print("2. 💭 프롬프트 방식 (순수 GPT)")
            print("3. ⚖️ 두 방식 비교")
            
            method_choice = input("선택하세요 (1/2/3): ").strip()  # 사용자 선택 받기
            
            # 선택에 따른 방식 설정
            if method_choice == "1":
                method = "rag"
                print("\n🔍 유사 상황을 검색하고 분석 중...")
            elif method_choice == "2":
                method = "prompt"
                print("\n💭 당신의 마음을 분석 중...")
            elif method_choice == "3":
                method = "comparison"
                print("\n⚖️ 두 방식으로 조언을 생성 중...")
            else:
                print("❗ 잘못된 선택입니다. 기본값(RAG)을 사용합니다.")
                method = "rag"
                print("\n🔍 유사 상황을 검색하고 분석 중...")
            
            # 조언 생성
            result = advisor_system.get_advice(user_input, method=method)
            
            # 결과 처리 및 표시
            if result["success"]:
                if method == "comparison":
                    # 비교 모드 결과 표시
                    print("\n" + "="*70)
                    print("⚖️ 두 방식 비교 결과")
                    print("="*70)
                    
                    rag_result = result.get("rag_result", {})  # RAG 결과
                    prompt_result = result.get("prompt_result", {})  # 프롬프트 결과
                    
                    # RAG 결과 표시
                    print("\n🔍 RAG 방식 조언:")
                    print("-" * 35)
                    if rag_result.get("success"):
                        print(f"{rag_result['advice']}\n")
                        
                        # 유사도는 로그에서 확인하므로 참고 조언들 표시 제거
                        # if rag_result.get("similar_advice"):
                        #     print("📚 참고한 유사 조언들:")
                        #     for advice in rag_result["similar_advice"]:
                        #         meta = advice["metadata"]
                        #         similarity_score = advice.get("similarity_score", 0)
                        #         print(f"   {advice['similarity_rank']}. [{meta.get('category', '일반')}] 유사도: {similarity_score:.3f} - {advice['content'][:80]}...")
                    else:
                        print(f"❌ 실패: {rag_result.get('error', 'Unknown error')}")
                    
                    # 프롬프트 결과 표시
                    print(f"\n💭 프롬프트 방식 조언:")
                    print("-" * 35)
                    if prompt_result.get("success"):
                        print(f"{prompt_result['advice']}")
                        if prompt_result.get("tokens_used"):
                            print(f"\n📊 사용된 토큰: {prompt_result['tokens_used']}")
                    else:
                        print(f"❌ 실패: {prompt_result.get('error', 'Unknown error')}")
                    
                    print("\n" + "="*70)
                    
                else:
                    # 단일 방식 결과 표시
                    method_name = "🔍 RAG 방식" if method == "rag" else "💭 프롬프트 방식"
                    print(f"\n💝 {method_name} 조언:")
                    print(f"{result['advice']}\n")
                    
                    # RAG 방식인 경우 분석 결과와 유사 조언들 표시
                    if method == "rag":
                        # 감정/상황 분석 결과 표시
                        if result.get("emotion") and result.get("situation"):
                            print(f"📊 분석된 감정: {result['emotion']}")
                            print(f"📊 분석된 상황: {result['situation']}\n")
                        
                        # 유사도는 로그에서 확인하므로 참고 조언들 표시 제거
                        # if result.get("similar_advice"):
                        #     print("\n📚 참고 조언들:")
                        #     for advice in result["similar_advice"]:
                        #         meta = advice["metadata"]
                        #         similarity_score = advice.get("similarity_score", 0)
                        #         print(f"   {advice['similarity_rank']}. [{meta.get('category', '일반')}] 유사도: {similarity_score:.3f} - {advice['content'][:100]}...")
                        #     print()
                    
                    # 프롬프트 방식인 경우 토큰 사용량 표시
                    if method == "prompt" and result.get("tokens_used"):
                        print(f"📊 사용된 토큰: {result['tokens_used']}")
            else:
                # 오류 발생 시 오류 메시지 표시
                print(f"\n❌ 조언 생성 중 오류가 발생했습니다: {result['error']}")
    
    except KeyboardInterrupt:
        # Ctrl+C로 프로그램 중단 시
        print("\n\n👋 프로그램을 종료합니다.")
    except Exception as e:
        # 기타 예외 발생 시
        print(f"\n❌ 시스템 오류: {e}")
        print("설정을 확인하고 다시 시도해주세요.")


# 스크립트가 직접 실행될 때만 main() 함수 호출
if __name__ == "__main__":
    main() 