"""
벡터 데이터베이스 관리 모듈
ChromaDB를 사용하여 조언 데이터를 벡터화하여 저장하고 검색

벡터 데이터베이스란?
- 텍스트를 숫자 벡터로 변환해서 저장하는 데이터베이스
- 비슷한 의미의 텍스트들을 빠르게 찾을 수 있음
- 예: "슬프다"와 "우울하다"를 비슷한 벡터로 변환해서 관련 조언을 찾음
"""

# 필요한 라이브러리들 가져오기
import chromadb  # 벡터 데이터베이스 라이브러리
from chromadb.config import Settings  # ChromaDB 설정
from transformers import AutoTokenizer, AutoModel  # HuggingFace의 AI 모델들
import torch  # 딥러닝 라이브러리
import numpy as np  # 수치 계산 라이브러리
from typing import List, Dict, Any  # 타입 힌트용
import logging  # 로그 출력용
from config.config import Config  # 설정 파일


# 로그 설정 (프로그램 실행 과정을 출력하기 위함)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VectorDatabase:
    """
    벡터 데이터베이스 관리 클래스
    - 텍스트를 벡터로 변환
    - 벡터를 데이터베이스에 저장
    - 유사한 벡터 검색
    """
    
    def __init__(self):
        """
        클래스 초기화 - 필요한 변수들을 None으로 설정
        실제 초기화는 initialize() 메소드에서 진행
        """
        self.config = Config()  # 설정 파일에서 설정값 로드
        self.embedding_model = None  # 텍스트를 벡터로 변환하는 AI 모델
        self.tokenizer = None  # 텍스트를 토큰(단어 조각)으로 나누는 도구
        self.embedding_model_diary = None  # 일기 임베딩 모델
        self.tokenizer_diary = None  # 일기용 토크나이저
        self.client = None  # ChromaDB 클라이언트 (데이터베이스 연결 객체)
        self.collection = None  # 기본 조언 컬렉션
        self.quotes_collection = None  # 명언 컬렉션
        self.past_diaries_collection = None  # 과거 일기 컬렉션
        
    def initialize(self):
        """
        실제 초기화 작업
        1. AI 모델 로딩
        2. 데이터베이스 연결
        3. 컬렉션 생성
        """
        try:
            # 1. HuggingFace에서 AI 모델 다운로드 및 로딩
            logger.info("HuggingFace 임베딩 모델 로딩 중...")
            
            # 기본 모델 (조언, 명언용)
            # 토크나이저: 텍스트를 AI가 이해할 수 있는 토큰으로 변환
            # EMBEDDING_MODEL - sentence-transformers/all-MiniLM-L6-v2
            self.tokenizer = AutoTokenizer.from_pretrained(self.config.EMBEDDING_MODEL)
            # 임베딩 모델: 토큰을 벡터(숫자 배열)로 변환
            self.embedding_model = AutoModel.from_pretrained(self.config.EMBEDDING_MODEL)
            logger.info(f"기본 임베딩 모델 로딩 완료: {self.config.EMBEDDING_MODEL}")
            
            # 일기용 모델 (과거 일기용)
            # EMBEDDING_MODEL_DIARY - sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
            self.tokenizer_diary = AutoTokenizer.from_pretrained(self.config.EMBEDDING_MODEL_DIARY)
            self.embedding_model_diary = AutoModel.from_pretrained(self.config.EMBEDDING_MODEL_DIARY)
            logger.info(f"일기용 임베딩 모델 로딩 완료: {self.config.EMBEDDING_MODEL_DIARY}")
            
            logger.info("ChromaDB 클라이언트 초기화 중...")
            
            # 2. 기존 데이터베이스가 있는지 확인
            import os      # 파일 시스템 접근용
            db_exists = os.path.exists(self.config.CHROMA_PERSIST_DIRECTORY)
            
            # 3. ChromaDB 클라이언트 생성 (데이터베이스 연결)
            self.client = chromadb.PersistentClient(
                path=self.config.CHROMA_PERSIST_DIRECTORY,  # 데이터베이스 저장 경로
                settings=Settings(
                    anonymized_telemetry=False,  # 사용 통계 전송 안함
                    allow_reset=True             # 리셋 허용
                )
            )
            
            # 4. 각 컬렉션 생성 또는 기존 컬렉션 가져오기
            # 기본 조언 컬렉션
            try:
                self.collection = self.client.get_collection(name=self.config.COLLECTION_NAME)
                logger.info(f"기존 조언 컬렉션 로드: {self.config.COLLECTION_NAME}")
            except:
                self.collection = self.client.create_collection(
                    name=self.config.COLLECTION_NAME,
                    metadata={"description": "일기 조언 데이터베이스"}
                )
                logger.info(f"새 조언 컬렉션 생성: {self.config.COLLECTION_NAME}")
            
            # 명언 컬렉션
            try:
                self.quotes_collection = self.client.get_collection(name=self.config.QUOTES_COLLECTION_NAME)
                logger.info(f"기존 명언 컬렉션 로드: {self.config.QUOTES_COLLECTION_NAME}")
            except:
                self.quotes_collection = self.client.create_collection(
                    name=self.config.QUOTES_COLLECTION_NAME,
                    metadata={"description": "명언 데이터베이스"}
                )
                logger.info(f"새 명언 컬렉션 생성: {self.config.QUOTES_COLLECTION_NAME}")
            
            # 과거 일기 컬렉션
            try:
                self.past_diaries_collection = self.client.get_collection(name=self.config.PAST_DIARIES_COLLECTION_NAME)
                logger.info(f"기존 과거 일기 컬렉션 로드: {self.config.PAST_DIARIES_COLLECTION_NAME}")
            except:
                self.past_diaries_collection = self.client.create_collection(
                    name=self.config.PAST_DIARIES_COLLECTION_NAME,
                    metadata={"description": "과거 일기 데이터베이스"}
                )
                logger.info(f"새 과거 일기 컬렉션 생성: {self.config.PAST_DIARIES_COLLECTION_NAME}")
                
        except Exception as e:
            logger.error(f"데이터베이스 초기화 실패: {e}")
            raise  # 에러를 다시 발생시켜서 프로그램 중단
    
    def embed_text(self, text: str) -> List[float]:
        """
        텍스트를 벡터로 변환하는 핵심 함수 (기본 모델 사용)
        
        과정:
        1. 텍스트를 토큰으로 분할
        2. 토큰을 AI 모델에 입력
        3. AI 모델이 벡터 출력
        4. 벡터를 정규화해서 반환
        
        Args:
            text: 변환할 텍스트 (예: "오늘 기분이 안좋다")
            
        Returns:
            List[float]: 벡터 (예: [0.1, -0.5, 0.3, ...])
        """
        try:
            # 모델이 초기화되지 않았으면 초기화
            if self.embedding_model is None:
                logger.info("임베딩 모델이 초기화되지 않아 초기화를 진행합니다...")
                self.initialize()
            
            # 1. 텍스트를 토큰으로 변환
            # padding=True: 짧은 텍스트는 패딩으로 채움
            # truncation=True: 긴 텍스트는 잘라냄 (최대 256 토큰)
            # max_length=256: sentence-transformers 모델의 기본 최대 길이
            # return_tensors='pt': PyTorch 텐서로 반환
            encoded_input = self.tokenizer(text, padding=True, truncation=True, max_length=256, return_tensors='pt')
            
            # 2. AI 모델에 토큰 입력해서 벡터 생성
            # torch.no_grad(): 학습이 아니므로 그래디언트 계산 안함 (메모리 절약)
            with torch.no_grad():
                model_output = self.embedding_model(**encoded_input)
            
            # 3. CLS 토큰 사용으로 문장 전체의 벡터 생성
            # [CLS] 토큰의 임베딩을 사용하여 더 나은 문장 표현 생성
            sentence_embeddings = model_output.last_hidden_state[:, 0, :]
            
            # 4. 벡터 정규화 (크기를 1로 만듦)
            # 벡터의 방향만 중요하고 크기는 중요하지 않으므로
            sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
            
            # 5. PyTorch 텐서를 파이썬 리스트로 변환해서 반환
            return sentence_embeddings.squeeze().cpu().numpy().tolist()
            
        except Exception as e:
            logger.error(f"임베딩 생성 실패: {e}")
            raise
    
    def embed_text_diary(self, text: str) -> List[float]:
        """
        일기 텍스트를 벡터로 변환하는 함수 (일기용 모델 사용)
        
        과정:
        1. 텍스트를 토큰으로 분할 (일기용 토크나이저 사용)
        2. 토큰을 일기용 AI 모델에 입력
        3. AI 모델이 벡터 출력
        4. 벡터를 정규화해서 반환
        
        Args:
            text: 변환할 일기 텍스트 (예: "오늘 회사에서 힘든 일이 있었다")
            
        Returns:
            List[float]: 벡터 (예: [0.1, -0.5, 0.3, ...])
        """
        try:
            # 모델이 초기화되지 않았으면 초기화
            if self.embedding_model_diary is None:
                logger.info("일기용 임베딩 모델이 초기화되지 않아 초기화를 진행합니다...")
                self.initialize()
            
            # 1. 텍스트를 토큰으로 변환 (일기용 토크나이저 사용)
            encoded_input = self.tokenizer_diary(text, padding=True, truncation=True, max_length=512, return_tensors='pt')
            
            # 2. 일기용 AI 모델에 토큰 입력해서 벡터 생성
            with torch.no_grad():
                model_output = self.embedding_model_diary(**encoded_input)
            
            # 3. CLS 토큰 사용으로 문장 전체의 벡터 생성
            sentence_embeddings = model_output.last_hidden_state[:, 0, :]
            
            # 4. 벡터 정규화 (크기를 1로 만듦)
            sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
            
            # 5. PyTorch 텐서를 파이썬 리스트로 변환해서 반환
            return sentence_embeddings.squeeze().cpu().numpy().tolist()
            
        except Exception as e:
            logger.error(f"일기 임베딩 생성 실패: {e}")
            raise
    
    def _mean_pooling(self, model_output, attention_mask):
        """
        평균 풀링 함수 - 여러 토큰 벡터를 하나의 문장 벡터로 합치기
        
        예시:
        "안녕하세요" = ["안녕", "하", "세요"] 토큰들
        각 토큰마다 벡터가 있음: [v1, v2, v3]
        이를 평균내서 하나의 문장 벡터로 만듦: (v1 + v2 + v3) / 3
        
        Args:
            model_output: AI 모델의 출력 (모든 토큰의 벡터들)
            attention_mask: 어떤 토큰이 실제 단어이고 어떤 토큰이 패딩인지 표시
            
        Returns:
            torch.Tensor: 문장 벡터
        """
        # 첫 번째 요소가 모든 토큰의 임베딩
        token_embeddings = model_output[0]
        
        # attention_mask를 확장해서 토큰 임베딩과 같은 크기로 만듦
        # attention_mask: [1, 1, 1, 0, 0] (1=실제단어, 0=패딩)
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        
        # 실제 단어들의 벡터만 더하고, 패딩은 제외
        # 그리고 실제 단어 개수로 나누어서 평균 계산
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    
    def add_advice(self, advice_data: Dict[str, Any]) -> bool:
        """
        새로운 조언 데이터를 벡터 데이터베이스에 추가
        
        과정:
        1. 조언 텍스트를 벡터로 변환
        2. 메타데이터 전처리
        3. 데이터베이스에 저장
        
        Args:
            advice_data: 조언 데이터 딕셔너리
            {
                "content": "힘들 때는 친구와 대화해보세요",  # 조언 데이터용
                "document": "인생은 항상 공평하지 않을 수도 있어요",  # 명언 데이터용
                "metadata": {
                    "emotion": ["슬픔", "우울"],
                    "situation": "인간관계"
                },
                "id": "advice_1"
            }
            
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        try:
            # 1. 텍스트 내용 추출 (content 또는 document 필드)
            text_content = advice_data.get("content") or advice_data.get("document")
            if not text_content:
                logger.error("텍스트 내용을 찾을 수 없습니다. 'content' 또는 'document' 필드가 필요합니다.")
                return False
            
            # 2. 조언 내용을 벡터로 변환
            embedding = self.embed_text(text_content)
            
            # 3. 메타데이터 전처리 - ChromaDB는 리스트를 저장 못하므로 문자열로 변환
            processed_metadata = {}
            for key, value in advice_data["metadata"].items():
                if isinstance(value, list):
                    # 리스트를 쉼표로 구분된 문자열로 변환
                    # 예: ["슬픔", "우울"] → "슬픔,우울"
                    processed_metadata[key] = ",".join(str(item) for item in value)
                else:
                    # 리스트가 아니면 그대로 저장
                    processed_metadata[key] = value
            
            # 4. ID 생성 (없으면 자동으로 만듦)
            advice_id = advice_data.get("id", f"advice_{len(self.collection.get()['ids']) + 1}")
            
            # 5. 데이터베이스에 실제로 저장
            self.collection.add(
                documents=[text_content],              # 원본 텍스트
                metadatas=[processed_metadata],        # 메타데이터 (감정, 상황 등)
                ids=[advice_id],                       # 고유 ID
                embeddings=[embedding]                 # 벡터
            )
            
            logger.info(f"데이터 추가 완료: {advice_id}")
            return True
            
        except Exception as e:
            logger.error(f"데이터 추가 실패: {e}")
            return False
    
    def add_quote(self, quote_data: Dict[str, Any]) -> bool:
        """명언 데이터를 명언 컬렉션에 추가"""
        try:
            # 1. 텍스트 내용 추출
            text_content = quote_data.get("document")
            if not text_content:
                logger.error("명언 텍스트를 찾을 수 없습니다.")
                return False
            
            # 2. 명언 내용을 벡터로 변환
            embedding = self.embed_text(text_content)
            
            # 3. 메타데이터 처리
            processed_metadata = {}
            for key, value in quote_data["metadata"].items():
                if isinstance(value, list):
                    processed_metadata[key] = ",".join(str(item) for item in value)
                else:
                    processed_metadata[key] = value
            
            # 4. ID 생성
            quote_id = quote_data.get("id", f"quote_{len(self.quotes_collection.get()['ids']) + 1}")
            
            # 5. 명언 컬렉션에 저장
            self.quotes_collection.add(
                documents=[text_content],
                metadatas=[processed_metadata],
                ids=[quote_id],
                embeddings=[embedding]
            )
            
            logger.info(f"명언 추가 완료: {quote_id}")
            return True
            
        except Exception as e:
            logger.error(f"명언 추가 실패: {e}")
            return False
    
    def add_past_diary(self, diary_data: Dict[str, Any]) -> bool:
        """과거 일기 데이터를 과거 일기 컬렉션에 추가 (일기용 임베딩 모델 사용)"""
        try:
            # 1. 텍스트 내용 추출
            text_content = diary_data.get("document")
            if not text_content:
                logger.error("과거 일기 텍스트를 찾을 수 없습니다.")
                return False
            
            # 2. 과거 일기 내용을 일기용 벡터로 변환
            embedding = self.embed_text_diary(text_content)
            
            # 3. 메타데이터 처리
            processed_metadata = {}
            for key, value in diary_data["metadata"].items():
                if isinstance(value, list):
                    processed_metadata[key] = ",".join(str(item) for item in value)
                else:
                    processed_metadata[key] = value
            
            # 4. ID 생성
            diary_id = diary_data.get("id", f"diary_{len(self.past_diaries_collection.get()['ids']) + 1}")
            
            # 5. 과거 일기 컬렉션에 저장
            self.past_diaries_collection.add(
                documents=[text_content],
                metadatas=[processed_metadata],
                ids=[diary_id],
                embeddings=[embedding]
            )
            
            logger.info(f"과거 일기 추가 완료: {diary_id}")
            return True
            
        except Exception as e:
            logger.error(f"과거 일기 추가 실패: {e}")
            return False
    
    def search_similar_advice(self, query_text: str, n_results: int = None, 
                            emotion_filter: List[str] = None, 
                            situation_filter: str = None) -> Dict[str, Any]:
        """
        유사한 조언을 검색하는 핵심 함수
        
        과정:
        1. 검색어를 벡터로 변환
        2. 필터 조건 설정 (감정, 상황)
        3. 벡터 유사도로 검색
        4. 결과 반환
        
        Args:
            query_text: 검색할 텍스트 (예: "요즘 우울해서 힘들어")
            n_results: 반환할 결과 개수 (None이면 설정 파일의 기본값)
            emotion_filter: 감정 필터 (예: ["부정적 감정"])
            situation_filter: 상황 필터 (예: "업무 및 학습")
            
        Returns:
            Dict: 검색 결과
            {
                "documents": [["조언1", "조언2", ...]],
                "metadatas": [[메타데이터1, 메타데이터2, ...]],
                "distances": [[거리1, 거리2, ...]]  # 거리가 작을수록 유사
            }
        """
        # 결과 개수가 지정되지 않으면 설정 파일의 기본값 사용
        if n_results is None:
            n_results = self.config.TOP_K_RESULTS
            
        try:
            # 1. 검색어를 벡터로 변환
            query_embedding = self.embed_text(query_text)
            
            # 2. 필터 조건 구성 - 단순화된 접근법 사용
            where_conditions = None
            
            if emotion_filter and len(emotion_filter) > 0:
                emotion = emotion_filter[0]  # 첫 번째 감정만 사용
                where_conditions = {"emotion": emotion}
                logger.info(f"감정 필터 적용: {emotion}")
                
            if situation_filter:
                if where_conditions:
                    # 감정과 상황 필터 모두 적용
                    where_conditions = {
                        "$and": [
                            {"emotion": emotion_filter[0]},
                            {"situation": situation_filter}
                        ]
                    }
                else:
                    where_conditions = {"situation": situation_filter}
                logger.info(f"상황 필터 적용: {situation_filter}")
            
            # 3. 벡터 유사도 검색 실행
            if where_conditions:
                logger.info(f"필터 조건으로 검색: {where_conditions}")
                results = self.collection.query(
                    query_embeddings=[query_embedding],  # 검색할 벡터
                    n_results=n_results,                  # 결과 개수
                    where=where_conditions                # 필터 조건
                )
            else:
                # 필터 조건이 없는 경우 (전체 검색)
                logger.info("필터 없이 전체 검색")
                results = self.collection.query(
                    query_embeddings=[query_embedding],
                    n_results=n_results
                )
            
            logger.info(f"검색 완료: {len(results['documents'][0])}개 결과 (필터: 감정={emotion_filter}, 상황={situation_filter})")
            
            # 유사도가 너무 낮거나 결과가 없는 경우 필터 없이 재검색
            if len(results['documents'][0]) == 0 and where_conditions:
                logger.info("필터링 결과가 없어서 전체 검색으로 재시도...")
                results = self.collection.query(
                    query_embeddings=[query_embedding],
                    n_results=n_results
                )
                logger.info(f"전체 검색 결과: {len(results['documents'][0])}개")
            
            return results
            
        except Exception as e:
            logger.error(f"검색 실패: {e}")
            # 에러 발생 시 빈 결과 반환
            return {"documents": [[]], "metadatas": [[]], "distances": [[]]}

    def search_similar_quotes(self, query: str, n_results: int = 3) -> dict:
        """유사한 명언 검색 (명언 컬렉션에서)"""
        try:
            # 모델이 초기화되지 않았으면 초기화
            if self.embedding_model is None:
                logger.info("임베딩 모델이 초기화되지 않아 초기화를 진행합니다...")
                self.initialize()
            
            logger.info(f"명언 검색 시작: 쿼리='{query[:50]}...', n_results={n_results}")
            
            # 1. 쿼리 텍스트를 벡터로 변환
            query_embedding = self.embed_text(query)
            logger.info("쿼리 임베딩 생성 완료")
            
            # 2. 명언 컬렉션에서 검색
            results = self.quotes_collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )
            
            logger.info(f"명언 검색 완료: {len(results['documents'][0])}개 결과")
            return results
            
        except Exception as e:
            logger.error(f"명언 검색 중 오류 발생: {e}")
            return {"documents": [[]], "metadatas": [[]], "distances": [[]]}
    
    def search_similar_past_diaries(self, query: str, n_results: int = 3) -> dict:
        """유사한 과거 일기 검색 (과거 일기 컬렉션에서, 일기용 임베딩 모델 사용)"""
        try:
            # 모델이 초기화되지 않았으면 초기화
            if self.embedding_model_diary is None:
                logger.info("일기용 임베딩 모델이 초기화되지 않아 초기화를 진행합니다...")
                self.initialize()
            
            logger.info(f"과거 일기 검색 시작: 쿼리='{query[:50]}...', n_results={n_results}")
            
            # 1. 쿼리 텍스트를 일기용 벡터로 변환
            query_embedding = self.embed_text_diary(query)
            logger.info("일기용 쿼리 임베딩 생성 완료")
            
            # 2. 과거 일기 컬렉션에서 검색
            results = self.past_diaries_collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )
            
            logger.info(f"과거 일기 검색 완료: {len(results['documents'][0])}개 결과")
            return results
            
        except Exception as e:
            logger.error(f"과거 일기 검색 중 오류 발생: {e}")
            return {"documents": [[]], "metadatas": [[]], "distances": [[]]}
    
    def get_collection_info(self) -> Dict[str, Any]:
        """
        현재 데이터베이스의 정보를 반환
        
        Returns:
            Dict: 데이터베이스 정보
            {
                "name": "컬렉션 이름",
                "count": 저장된 데이터 개수,
                "embedding_model": "사용중인 AI 모델 이름"
            }
        """
        try:
            count = self.collection.count()  # 저장된 데이터 개수 조회
            return {
                "name": self.config.COLLECTION_NAME,
                "count": count,
                "embedding_model": self.config.EMBEDDING_MODEL
            }
        except Exception as e:
            logger.error(f"컬렉션 정보 조회 실패: {e}")
            return {}
    
    def reset_database(self) -> bool:
        """
        데이터베이스를 완전히 초기화 (모든 데이터 삭제)
        
        과정:
        1. 기존 컬렉션 삭제
        2. 새 컬렉션 생성
        
        Returns:
            bool: 성공하면 True, 실패하면 False
        """
        try:
            # 기존 컬렉션 삭제
            self.client.delete_collection(self.config.COLLECTION_NAME)
            self.client.delete_collection(self.config.QUOTES_COLLECTION_NAME)
            self.client.delete_collection(self.config.PAST_DIARIES_COLLECTION_NAME)
            
            # 새 컬렉션 생성
            self.collection = self.client.create_collection(
                name=self.config.COLLECTION_NAME,
                metadata={"description": "일기 조언 데이터베이스"}
            )
            
            self.quotes_collection = self.client.create_collection(
                name=self.config.QUOTES_COLLECTION_NAME,
                metadata={"description": "명언 데이터베이스"}
            )
            
            self.past_diaries_collection = self.client.create_collection(
                name=self.config.PAST_DIARIES_COLLECTION_NAME,
                metadata={"description": "과거 일기 데이터베이스"}
            )
            
            logger.info("데이터베이스 리셋 완료")
            return True
            
        except Exception as e:
            logger.error(f"데이터베이스 리셋 실패: {e}")
            return False
    
    def reset_advice_collection(self) -> bool:
        """조언 컬렉션만 리셋"""
        try:
            self.client.delete_collection(self.config.COLLECTION_NAME)
            self.collection = self.client.create_collection(
                name=self.config.COLLECTION_NAME,
                metadata={"description": "일기 조언 데이터베이스"}
            )
            logger.info("조언 컬렉션 리셋 완료")
            return True
        except Exception as e:
            logger.error(f"조언 컬렉션 리셋 실패: {e}")
            return False
    
    def reset_quotes_collection(self) -> bool:
        """명언 컬렉션만 리셋"""
        try:
            self.client.delete_collection(self.config.QUOTES_COLLECTION_NAME)
            self.quotes_collection = self.client.create_collection(
                name=self.config.QUOTES_COLLECTION_NAME,
                metadata={"description": "명언 데이터베이스"}
            )
            logger.info("명언 컬렉션 리셋 완료")
            return True
        except Exception as e:
            logger.error(f"명언 컬렉션 리셋 실패: {e}")
            return False
    
    def reset_past_diaries_collection(self) -> bool:
        """과거 일기 컬렉션만 리셋"""
        try:
            self.client.delete_collection(self.config.PAST_DIARIES_COLLECTION_NAME)
            self.past_diaries_collection = self.client.create_collection(
                name=self.config.PAST_DIARIES_COLLECTION_NAME,
                metadata={"description": "과거 일기 데이터베이스"}
            )
            logger.info("과거 일기 컬렉션 리셋 완료")
            return True
        except Exception as e:
            logger.error(f"과거 일기 컬렉션 리셋 실패: {e}")
            return False