from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Union
import logging

logger = logging.getLogger(__name__)

class EmbeddingService:
    def __init__(self, model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
        """임베딩 모델 초기화"""
        try:
            self.model = SentenceTransformer(model_name)
            logger.info(f"임베딩 모델 '{model_name}' 로드됨")
        except Exception as e:
            logger.error(f"임베딩 모델 로드 실패: {e}")
            raise
    
    def encode(self, texts: Union[str, List[str]]) -> Union[List[float], List[List[float]]]:
        """텍스트를 벡터로 인코딩"""
        try:
            embeddings = self.model.encode(texts)
            if isinstance(texts, str):
                return embeddings.tolist()
            else:
                return embeddings.tolist()
        except Exception as e:
            logger.error(f"임베딩 생성 중 오류: {e}")
            raise
    
    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """코사인 유사도 계산"""
        try:
            vec1 = np.array(vec1)
            vec2 = np.array(vec2)
            dot_product = np.dot(vec1, vec2)
            norm1 = np.linalg.norm(vec1)
            norm2 = np.linalg.norm(vec2)
            
            if norm1 == 0 or norm2 == 0:
                return 0.0
                
            return float(dot_product / (norm1 * norm2))
        except Exception as e:
            logger.error(f"유사도 계산 중 오류: {e}")
            return 0.0
    
    def batch_encode(self, texts: List[str], batch_size: int = 32) -> List[List[float]]:
        """배치 단위로 임베딩 생성"""
        try:
            all_embeddings = []
            for i in range(0, len(texts), batch_size):
                batch = texts[i:i + batch_size]
                batch_embeddings = self.model.encode(batch)
                all_embeddings.extend(batch_embeddings.tolist())
            return all_embeddings
        except Exception as e:
            logger.error(f"배치 임베딩 생성 중 오류: {e}")
            raise 