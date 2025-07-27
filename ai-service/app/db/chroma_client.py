import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any
import logging
import os

logger = logging.getLogger(__name__)

class ChromaClient:
    def __init__(self, collection_name: str = "diary_entries"):
        # 최신 ChromaDB 설정
        persist_directory = "./chroma_db"
        
        # 디렉토리가 없으면 생성
        os.makedirs(persist_directory, exist_ok=True)
        
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection_name = collection_name
        self.collection = None
        self._init_collection()
    
    def _init_collection(self):
        """컬렉션 초기화"""
        try:
            self.collection = self.client.get_collection(name=self.collection_name)
            logger.info(f"기존 컬렉션 '{self.collection_name}' 로드됨")
        except:
            self.collection = self.client.create_collection(name=self.collection_name)
            logger.info(f"새 컬렉션 '{self.collection_name}' 생성됨")
    
    def add_documents(self, documents: List[str], embeddings: List[List[float]], 
                     metadatas: List[Dict[str, Any]], ids: List[str]):
        """문서들을 컬렉션에 추가"""
        try:
            self.collection.add(
                documents=documents,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )
            logger.info(f"{len(documents)}개 문서 추가됨")
        except Exception as e:
            logger.error(f"문서 추가 중 오류: {e}")
            raise
    
    def search(self, query_embeddings: List[List[float]], n_results: int = 10, 
               where_filter: Dict[str, Any] = None):
        """벡터 검색 수행"""
        try:
            results = self.collection.query(
                query_embeddings=query_embeddings,
                n_results=n_results,
                where=where_filter
            )
            return results
        except Exception as e:
            logger.error(f"검색 중 오류: {e}")
            raise
    
    def get_collection_info(self) -> Dict[str, Any]:
        """컬렉션 정보 반환"""
        return {
            "name": self.collection_name,
            "count": self.collection.count()
        } 