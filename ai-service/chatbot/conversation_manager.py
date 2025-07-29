"""
Redis를 사용하여 챗봇의 대화 기록을 관리하는 모듈입니다.

이 모듈은 사용자별로 대화 내용을 Redis에 저장, 조회, 삭제하는 기능을 제공하여
챗봇이 이전 대화의 맥락을 기억하고 일관성 있는 대화를 이어갈 수 있도록 돕습니다.

개발/테스트 환경에서는 fakeredis를 사용하여 별도의 Redis 서버 없이도 동작합니다.
"""
import redis
import fakeredis
import logging
from typing import List, Dict, Union

logger = logging.getLogger(__name__)

class ConversationManager:
    """
    Redis를 사용하여 사용자와의 대화 기록을 관리하는 클래스입니다.

    Redis의 List 데이터 구조를 활용하여 각 사용자의 대화 턴을 순서대로 저장합니다.
    최신 대화가 리스트의 맨 앞에 오도록(lpush) 관리하여 최근 대화 조회 성능을 최적화합니다.
    
    Attributes:
        redis_client (redis.Redis): Redis 데이터베이스와의 연결을 관리하는 클라이언트 객체입니다.
        history_key_prefix (str): Redis 키를 생성할 때 사용할 접두사입니다. 
                                  'conversation_history:user123'와 같은 형태로 키를 만듭니다.
        max_history_length (int): 각 사용자에 대해 저장할 최대 대화 턴의 수입니다.
                                  이 개수를 초과하면 가장 오래된 기록부터 자동으로 삭제됩니다.
    """
    
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0, max_history_length: int = 10):
        """
        ConversationManager 인스턴스를 생성하고 fakeredis(메모리 기반 Redis)에 연결합니다.
        
        Args:
            host (str): 호환성을 위해 유지하지만 사용되지 않습니다.
            port (int): 호환성을 위해 유지하지만 사용되지 않습니다.
            db (int): 호환성을 위해 유지하지만 사용되지 않습니다.
            max_history_length (int): 유지할 최대 대화 기록의 길이입니다.
        """
        # fakeredis 클라이언트 생성 (메모리에서만 동작하는 Redis 모형)
        # decode_responses=True로 설정하면, Redis에서 받은 응답(바이트)을 자동으로 UTF-8로 디코딩해줍니다.
        self.redis_client = fakeredis.FakeRedis(decode_responses=True)
        logger.info("✅ fakeredis 연결 성공 (메모리 기반 Redis 사용)")
            
        self.history_key_prefix = "conversation_history:"
        self.max_history_length = max_history_length

    def _get_history_key(self, user_id: str) -> str:
        """
        주어진 사용자 ID에 대한 고유한 Redis 키를 생성합니다.
        
        Example:
            _get_history_key("user123") -> "conversation_history:user123"
        """
        return f"{self.history_key_prefix}{user_id}"

    def get_recent_conversation(self, user_id: str, count: int = 10) -> List[Dict[str, str]]:
        """
        지정된 사용자의 최근 대화 기록을 Redis에서 가져옵니다.
        
        Args:
            user_id (str): 대화 기록을 조회할 사용자의 ID입니다.
            count (int): 가져올 최근 대화의 최대 개수입니다.
            
        Returns:
            List[Dict[str, str]]: 'role'과 'content'를 키로 갖는 딕셔너리들의 리스트입니다.
                                 최신 대화가 리스트의 맨 앞에 위치합니다.
                                 오류 발생 시 빈 리스트를 반환합니다.
        """
        history_key = self._get_history_key(user_id)
        try:
            # lrange(key, start, end)는 리스트의 특정 범위의 요소들을 가져옵니다.
            # 0부터 count-1까지 가져와 최근 count개의 대화 기록을 조회합니다.
            recent_chats_str = self.redis_client.lrange(history_key, 0, count - 1)
            
            # Redis에 저장된 값은 문자열 형태이므로, 다시 파이썬 딕셔너리로 변환합니다.
            # '{"role": "user", "content": "안녕"}' -> {"role": "user", "content": "안녕"}
            # eval()은 보안에 취약할 수 있으므로, 실제 프로덕션 환경에서는 json.loads()를 사용하는 것이 더 안전합니다.
            # 여기서는 편의상 eval()을 사용합니다.
            return [eval(chat) for chat in recent_chats_str]
        except Exception as e:
            logger.error(f"대화 기록 조회 실패 (사용자 ID: {user_id}): {e}", exc_info=True)
            return []

    def add_to_conversation(self, user_id: str, role: str, content: str) -> None:
        """
        새로운 대화(발화)를 사용자의 대화 기록에 추가합니다.
        
        Args:
            user_id (str): 대화 기록을 추가할 사용자의 ID입니다.
            role (str): 발화의 주체입니다. (예: 'user', 'assistant')
            content (str): 발화의 실제 내용입니다.
        """
        history_key = self._get_history_key(user_id)
        # 딕셔너리를 문자열로 변환하여 Redis에 저장합니다.
        new_entry = str({"role": role, "content": content})
        
        try:
            # lpush(key, value)는 리스트의 맨 왼쪽에(가장 앞에) 새로운 요소를 추가합니다.
            # 이렇게 하면 항상 최신 대화가 0번 인덱스에 위치하게 됩니다.
            self.redis_client.lpush(history_key, new_entry)
            
            # ltrim(key, start, end)은 리스트를 지정된 범위만 남기고 나머지는 삭제합니다.
            # 0부터 max_history_length-1까지만 남겨서, 리스트의 길이가 최대치를 넘지 않도록 관리합니다.
            self.redis_client.ltrim(history_key, 0, self.max_history_length - 1)
        except Exception as e:
            logger.error(f"대화 기록 추가 실패 (사용자 ID: {user_id}): {e}", exc_info=True)

    def clear_conversation_history(self, user_id: str) -> None:
        """
        지정된 사용자의 모든 대화 기록을 Redis에서 삭제합니다.
        대화가 종료되거나 사용자가 기록 삭제를 요청할 때 사용됩니다.
        
        Args:
            user_id (str): 대화 기록을 삭제할 사용자의 ID입니다.
        """
        history_key = self._get_history_key(user_id)
        try:
            # 해당 키를 Redis에서 삭제하여 모든 대화 기록을 한번에 지웁니다.
            self.redis_client.delete(history_key)
            logger.info(f"사용자 ID '{user_id}'의 대화 기록이 삭제되었습니다.")
        except Exception as e:
            logger.error(f"대화 기록 삭제 실패 (사용자 ID: {user_id}): {e}", exc_info=True) 