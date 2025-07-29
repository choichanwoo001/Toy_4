"""
프롬프트 기반 조언 생성 모듈
RAG(Retrieval-Augmented Generation) 없이 순수 프롬프트만으로 조언을 생성하는 클래스

이 모듈은 사용자의 일기 내용을 받아서 OpenAI GPT 모델을 사용하여 
심리상담사 관점에서 따뜻하고 공감적인 조언을 생성합니다.

주요 특징:
- RAG 없이 순수 프롬프트 기반 조언 생성
- 감정 공감, 현실적 조언, 위로와 격려, 성장 관점을 포함한 종합적 조언
- 한국어 자연스러운 말투로 조언 생성
- OpenAI API 연결 및 에러 처리
"""

# 필요한 라이브러리 임포트
from openai import OpenAI  # OpenAI API 클라이언트
from typing import Dict, Any  # 타입 힌트를 위한 타입 정의
import logging  # 로깅을 위한 모듈
from config.config import Config  # 설정 파일에서 설정값 가져오기

# 로깅 설정 - INFO 레벨 이상의 로그를 출력
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # 현재 모듈의 로거 생성

class PromptAdvisor:
    """
    프롬프트 기반 조언 생성 클래스
    
    이 클래스는 사용자의 일기 내용을 받아서 OpenAI GPT 모델을 사용하여
    심리상담사 관점에서 따뜻하고 공감적인 조언을 생성합니다.
    
    Attributes:
        config (Config): 설정 객체 (API 키, 모델명 등)
        client (OpenAI): OpenAI API 클라이언트 객체
    """
    
    def __init__(self):
        """
        프롬프트 조언자 초기화
        
        초기화 과정:
        1. 설정 객체 생성
        2. OpenAI 클라이언트 초기화
        """
        self.config = Config()  # 설정 파일에서 설정값 로드
        self.client = None  # OpenAI 클라이언트 객체 (초기에는 None)
        self.initialize()  # OpenAI 클라이언트 초기화 실행
    
    def initialize(self):
        """
        OpenAI 클라이언트 초기화
        
        이 메서드는 OpenAI API 클라이언트를 초기화합니다.
        API 키가 설정되어 있는지 확인하고, 클라이언트 객체를 생성합니다.
        
        Raises:
            ValueError: API 키가 설정되지 않은 경우
            Exception: 기타 초기화 오류
        """
        try:
            # API 키가 설정되어 있는지 확인
            if not self.config.OPENAI_API_KEY:
                raise ValueError("OpenAI API 키가 설정되지 않았습니다. .env 파일을 확인해주세요.")
            
            # OpenAI 클라이언트 객체 생성
            self.client = OpenAI(
                api_key=self.config.OPENAI_API_KEY  # 설정에서 가져온 API 키 사용
            )
            logger.info("PromptAdvisor - OpenAI 클라이언트 초기화 완료")
            
        except Exception as e:
            logger.error(f"PromptAdvisor - OpenAI 클라이언트 초기화 실패: {e}")
            raise  # 오류를 다시 발생시켜 상위에서 처리할 수 있도록 함
    
    def analyze_emotion_and_situation(self, diary_content: str) -> Dict[str, Any]:
        """
        일기 내용에서 감정과 상황을 분석하는 메서드
        
        사용자의 일기 내용을 분석하여 가장 적합한 감정과 상황 카테고리를 추출합니다.
        
        Args:
            diary_content (str): 분석할 일기 내용
            
        Returns:
            Dict[str, Any]: 분석 결과
                - success (bool): 성공 여부
                - emotion (str): 분석된 감정 카테고리
                - situation (str): 분석된 상황 카테고리
                - error (str): 오류 메시지 (실패 시)
        """
        try:
            # 감정과 상황 분석을 위한 프롬프트
            analysis_prompt = """당신은 일기 내용을 분석하여 감정과 상황을 분류하는 전문가입니다.

다음 카테고리 중에서 일기 내용과 가장 적합한 감정과 상황을 각각 하나씩 선택해주세요:

**감정 카테고리:**
- 긍정적 감정 (기쁨, 만족, 희망, 자신감 등)
- 부정적 감정 (슬픔, 분노, 실망, 좌절 등)
- 두려움과 공포 (무서움, 불안, 걱정 등)
- 불안과 긴장 (스트레스, 압박감, 긴장 등)
- 수치와 자책 (후회, 죄책감, 자책 등)
- 소외와 상실 (외로움, 상실감, 고립감 등)
- 그리움과 아쉬움 (그리움, 아쉬움, 미련 등)
- 동기와 욕구 (열망, 욕구, 동기부여 등)
- 사회적 관계 감정 (사랑, 친밀감, 소속감 등)
- 이완과 침체 (무기력, 지루함, 침체 등)
- 혼란과 의심 (혼란, 의심, 불확실성 등)
- 경이와 압도 (놀라움, 감탄, 압도감 등)

**상황 카테고리:**
- 일상 및 여가 (일상생활, 취미, 휴식 등)
- 업무 및 학습 (직장, 공부, 프로젝트 등)
- 인간관계 (가족, 친구, 연인, 동료 관계 등)
- 건강 및 의료 (신체적, 정신적 건강 문제 등)
- 경제 및 소비생활 (돈, 구매, 경제적 문제 등)
- 특별한 날과 사건 (생일, 기념일, 특별한 사건 등)
- 디지털 및 온라인 활동 (SNS, 게임, 온라인 활동 등)
- 내면 활동 및 감정 (자기성찰, 내면의 변화 등)
- 창작과 성장 (새로운 도전, 성장, 발전 등)

분석 결과는 다음 형식으로 응답해주세요:
감정: [선택한 감정 카테고리]
상황: [선택한 상황 카테고리]

예시:
감정: 긍정적 감정
상황: 일상 및 여가"""

            # GPT API 호출하여 감정/상황 분석
            response = self.client.chat.completions.create(
                model=self.config.GPT_MODEL,
                messages=[
                    {"role": "system", "content": "당신은 일기 내용을 분석하여 감정과 상황을 분류하는 전문가입니다."},
                    {"role": "user", "content": f"다음 일기 내용을 분석해주세요:\n\n{diary_content}\n\n{analysis_prompt}"}
                ],
                max_tokens=100,
                temperature=0.3
            )
            
            # 응답 파싱
            analysis_result = response.choices[0].message.content.strip()
            
            # 결과에서 감정과 상황 추출
            emotion = None
            situation = None
            
            for line in analysis_result.split('\n'):
                if line.startswith('감정:'):
                    emotion = line.replace('감정:', '').strip()
                elif line.startswith('상황:'):
                    situation = line.replace('상황:', '').strip()
            
            if not emotion or not situation:
                raise ValueError("감정 또는 상황을 추출할 수 없습니다.")
            
            logger.info(f"감정/상황 분석 완료: 감정={emotion}, 상황={situation}")
            
            return {
                "success": True,
                "emotion": emotion,
                "situation": situation
            }
            
        except Exception as e:
            logger.error(f"감정/상황 분석 실패: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    def generate_advice(self, diary_content: str) -> Dict[str, Any]:
        """
        프롬프트만으로 조언 생성
        
        사용자의 일기 내용을 받아서 GPT 모델을 사용하여 심리상담사 관점의
        따뜻하고 공감적인 조언을 생성합니다.
        
        Args:
            diary_content (str): 사용자가 작성한 일기 내용
            
        Returns:
            Dict[str, Any]: 조언 생성 결과
                - success (bool): 성공 여부
                - advice (str): 생성된 조언 (성공 시)
                - method (str): 사용된 방법 ("prompt_only")
                - tokens_used (int): 사용된 토큰 수 (성공 시)
                - error (str): 오류 메시지 (실패 시)
        """
        try:
            logger.info("프롬프트 기반 조언 생성 시작...")
            
            # 상세한 프롬프트 구성
            system_prompt = """당신은 따뜻하고 공감능력이 뛰어난 심리상담사입니다.
사용자의 일기를 읽고, 주어진 '조언 생성 원칙'에 따라 종합적인 조언을 제공해주세요.

[조언 생성 원칙]
1. 감정 공감: 사용자의 감정을 충분히 이해하고 공감해주세요.
2. 현실적 조언: 실현 가능하고 구체적인 해결 방안을 제시해주세요.
3. 위로와 격려: 따뜻한 위로와 희망적인 메시지를 포함해주세요.
4. 성장 관점: 이 경험을 통해 성장할 수 있는 방향을 제시해주세요.
5. 가독성: 문단과 문장을 나누어 가독성 좋게 작성해주세요.

**[분기별 지침]**
*   **만약 '참고 정보'가 제공되면 (RAG 방식):**
    *   **6. RAG 활용:** 제공된 '참고 정보'(유사 조언, 명언, 과거 일기)를 적극적으로 활용하여, "과거에도 비슷한 감정을 느끼셨군요" 또는 "이런 명언이 있듯이..." 와 같이 자연스럽게 내용을 연결하며 조언해주세요.
*   **만약 '참고 정보'가 없다면 (프롬프트 방식):**
    *   **6. 자율성:** 참고 정보 없이, 당신의 전문 지식과 분석력을 바탕으로 자율적으로 조언을 생성해주세요.
    *   **7. 명언 생성:** 일기 내용에 어울리는 명언을 직접 생성하거나 떠올려 조언에 포함시켜주세요.

[출력 형식]
- 조언은 한국어로 자연스럽고 따뜻한 말투로 작성해주세요.
- 전체 길이는 2~4개의 완결된 문장으로 간결하게 구성해주세요. 절대 중간에 끊기면 안 됩니다."""

            # 사용자 프롬프트
            user_prompt = f"""[사용자 일기]
{diary_content}"""

            # GPT API 호출하여 조언 생성
            response = self.client.chat.completions.create(
                model=self.config.GPT_MODEL,  # 설정에서 지정한 모델 사용 (예: gpt-3.5-turbo)
                messages=[
                    {"role": "system", "content": system_prompt},  # 시스템 역할 정의
                    {"role": "user", "content": user_prompt}       # 사용자 요청
                ],
                max_tokens=self.config.MAX_TOKENS,  # 최대 토큰 수 제한
                temperature=self.config.TEMPERATURE  # 창의성 조절 (0.0~1.0)
            )
            
            # 응답에서 조언 내용 추출
            advice = response.choices[0].message.content.strip()
            
            logger.info("프롬프트 기반 조언 생성 완료")
            
            # 성공 결과 반환
            return {
                "success": True,
                "advice": advice,  # 생성된 조언
                "method": "prompt_only",  # 사용된 방법 (RAG 없이 프롬프트만 사용)
                "tokens_used": response.usage.total_tokens if response.usage else 0  # 사용된 토큰 수
            }
            
        except Exception as e:
            # 오류 발생 시 로그 기록 및 오류 결과 반환
            logger.error(f"프롬프트 기반 조언 생성 실패: {e}")
            return {
                "success": False,
                "error": str(e),  # 오류 메시지
                "method": "prompt_only"  # 사용된 방법
            }
    

 