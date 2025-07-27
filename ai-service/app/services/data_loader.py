from typing import List, Dict, Any
import logging
from datetime import datetime, timedelta
import random

from ..models.diary import DiaryEntry
from ..db.chroma_client import ChromaClient
from .embedding import EmbeddingService

logger = logging.getLogger(__name__)

class DataLoader:
    def __init__(self):
        """데이터 로더 초기화"""
        self.chroma_client = ChromaClient()
        self.embedding_service = EmbeddingService()
    
    def generate_sample_diary_data(self, num_entries: int = 50) -> List[DiaryEntry]:
        """샘플 일기 데이터 생성"""
        sample_entries = [
            # 우울한 감정 관련
            "오늘 회의에서 내 의견이 무시당한 것 같아서 속상했다.",
            "요즘 계속 우울한 기분이 들고 아무것도 하고 싶지 않다.",
            "친구들과 만나기로 했는데 갑자기 기분이 안 좋아져서 취소했다.",
            "시험 결과가 생각보다 안 좋아서 많이 실망했다.",
            "부모님과 다퉈서 마음이 무겁다.",
            
            # 기쁜 감정 관련
            "오늘 프로젝트가 성공적으로 완료되어서 정말 기뻤다.",
            "친구가 생일 선물로 정말 예쁜 것을 줘서 감동받았다.",
            "새로운 취미를 시작했는데 생각보다 재미있다.",
            "가족들과 맛있는 저녁을 먹고 행복한 시간을 보냈다.",
            "운동을 시작했는데 몸이 가벼워지는 느낌이 좋다.",
            
            # 화난 감정 관련
            "동료가 내 일을 방해해서 정말 화가 났다.",
            "버스에서 누군가 내 자리를 뺏어서 짜증이 났다.",
            "인터넷이 계속 끊겨서 작업을 못 하고 있다.",
            "식당에서 음식이 너무 늦게 나와서 화가 났다.",
            "누군가 내 물건을 함부로 만져서 기분이 나빴다.",
            
            # 불안한 감정 관련
            "내일 중요한 발표가 있어서 긴장된다.",
            "건강검진 결과가 나오기 전까지 불안하다.",
            "새로운 직장에 적응할 수 있을지 걱정된다.",
            "시험 준비가 부족해서 불안하다.",
            "가족의 건강이 걱정된다.",
            
            # 평온한 감정 관련
            "오늘은 날씨가 좋아서 산책을 다녀왔다.",
            "커피 한 잔 마시면서 책을 읽는 시간이 평화로웠다.",
            "요가 수업을 들었는데 마음이 차분해졌다.",
            "가족들과 함께 TV를 보면서 편안한 시간을 보냈다.",
            "새벽에 일어나서 조용히 명상을 했다."
        ]
        
        emotions = ["우울", "기쁨", "화남", "불안", "평온"]
        contexts = ["업무", "가족", "친구", "건강", "취미"]
        
        entries = []
        base_date = datetime.now() - timedelta(days=num_entries)
        
        for i in range(num_entries):
            content = random.choice(sample_entries)
            emotion = random.choice(emotions)
            context = random.choice(contexts)
            date = (base_date + timedelta(days=i)).strftime("%Y-%m-%d")
            
            entries.append(DiaryEntry(
                content=content,
                date=date,
                emotion=emotion,
                context=context
            ))
        
        return entries
    
    def load_data_to_chroma(self, entries: List[DiaryEntry]) -> bool:
        """일기 데이터를 ChromaDB에 로드"""
        try:
            # 문서, 메타데이터, ID 준비
            documents = [entry.content for entry in entries]
            metadatas = [
                {
                    "date": entry.date,
                    "emotion": entry.emotion,
                    "context": entry.context
                }
                for entry in entries
            ]
            ids = [f"diary_{i}_{entry.date}" for i, entry in enumerate(entries)]
            
            # 임베딩 생성
            logger.info("임베딩 생성 중...")
            embeddings = self.embedding_service.batch_encode(documents)
            
            # ChromaDB에 저장
            logger.info("ChromaDB에 데이터 저장 중...")
            self.chroma_client.add_documents(documents, embeddings, metadatas, ids)
            
            logger.info(f"{len(entries)}개 일기 엔트리가 성공적으로 저장되었습니다.")
            return True
            
        except Exception as e:
            logger.error(f"데이터 로드 중 오류: {e}")
            return False
    
    def get_collection_info(self) -> Dict[str, Any]:
        """컬렉션 정보 반환"""
        return self.chroma_client.get_collection_info()
    
    def clear_collection(self):
        """컬렉션 초기화 (테스트용)"""
        try:
            # 새로운 클라이언트로 컬렉션 재생성
            self.chroma_client = ChromaClient()
            logger.info("컬렉션이 초기화되었습니다.")
        except Exception as e:
            logger.error(f"컬렉션 초기화 중 오류: {e}")
            raise 