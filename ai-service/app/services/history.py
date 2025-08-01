from __future__ import annotations
from typing import List, Optional
import json
import fakeredis
from app.models.agent import RecentMessage

class RedisHistory:
    """
    Redis 기반 대화 히스토리 관리 클래스
    
    특징:
    - 사용자별 대화 히스토리 저장
    - 최신 메시지 우선 정렬
    - Redis 기반 (영구 저장)
    - 개발용 fakeredis 사용
    """
    
    def __init__(self, maxlen: int = 1000):
        """
        Args:
            maxlen: 사용자별 최대 저장 메시지 수
        """
        # fakeredis 클라이언트 생성 (개발용)
        self.redis_client = fakeredis.FakeRedis()
        self.maxlen = maxlen

    def _get_user_key(self, user_id: int) -> str:
        """사용자별 Redis 키 생성"""
        return f"chat_history:user:{user_id}"

    async def add(self, user_id: int, speaker: str, message: str) -> None:
        """
        대화 메시지 추가
        
        Args:
            user_id: 사용자 ID
            speaker: 화자 ("user" 또는 "ai")
            message: 메시지 내용
        """
        user_key = self._get_user_key(user_id)
        
        # 메시지 객체 생성
        msg_obj = RecentMessage(speaker=speaker, message=message)
        msg_json = msg_obj.model_dump_json()
        
        # Redis List에 메시지 추가 (최신이 오른쪽에)
        self.redis_client.rpush(user_key, msg_json)
        
        # 최대 길이 제한 (오래된 메시지 제거)
        if self.redis_client.llen(user_key) > self.maxlen:
            self.redis_client.lpop(user_key)

    async def load(self, user_id: int, limit: int = 5) -> List[RecentMessage]:
        """
        최근 대화 히스토리 로드
        
        Args:
            user_id: 사용자 ID
            limit: 로드할 메시지 수
            
        Returns:
            최신 메시지가 앞쪽에 오는 정렬된 리스트
        """
        user_key = self._get_user_key(user_id)
        
        # Redis에서 최신 메시지들 가져오기 (오른쪽에서 limit개)
        msg_jsons = self.redis_client.lrange(user_key, -limit, -1)
        
        # JSON을 객체로 변환하고 순서 뒤집기 (최신이 앞쪽에)
        messages = []
        for msg_json in reversed(msg_jsons):
            try:
                msg_data = json.loads(msg_json.decode('utf-8'))
                messages.append(RecentMessage.model_validate(msg_data))
            except (json.JSONDecodeError, KeyError) as e:
                print(f"메시지 파싱 오류: {e}")
                continue
        
        return messages

    async def clear(self, user_id: int) -> None:
        """
        사용자의 대화 히스토리 삭제
        
        Args:
            user_id: 사용자 ID
        """
        user_key = self._get_user_key(user_id)
        self.redis_client.delete(user_key)

    async def get_user_count(self, user_id: int) -> int:
        """
        사용자의 메시지 개수 반환
        
        Args:
            user_id: 사용자 ID
            
        Returns:
            int: 메시지 개수
        """
        user_key = self._get_user_key(user_id)
        return self.redis_client.llen(user_key)

# 기존 InMemoryHistory는 개발용으로 유지 (호환성)
class InMemoryHistory(RedisHistory):
    """
    기존 InMemoryHistory와의 호환성을 위한 래퍼 클래스
    실제로는 Redis 기반으로 동작
    """
    pass 