"""
챗봇 커맨드 라인 인터페이스 (CLI)
이 스크립트를 실행하여 터미널에서 직접 챗봇과 대화할 수 있습니다.
"""
import sys
import os
import logging

# 프로젝트 루트 경로를 추가하여 다른 모듈(core, config 등)을 불러올 수 있도록 설정
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot.chatbot_service import ChatbotService

# 기본 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """
    챗봇 CLI의 메인 실행 함수입니다.
    사용자와의 대화형 세션을 시작하고 관리합니다.
    """
    print("🌟 챗봇 상담 시스템에 오신 것을 환영합니다! 🌟\n")

    # 사용자 ID를 고정값으로 설정합니다. CLI 환경에서는 사용자를 구분할 필요가 적습니다.
    # 웹 애플리케이션 등에서는 로그인된 사용자의 ID를 동적으로 할당해야 합니다.
    user_id = "cli_user_01"

    try:
        # 1. 챗봇 서비스 초기화
        logger.info(f"사용자 ID '{user_id}'에 대한 챗봇 서비스를 초기화합니다.")
        chatbot_service = ChatbotService(user_id=user_id)
        chatbot_service.initialize()
        logger.info("챗봇 서비스가 성공적으로 초기화되었습니다.")
        
        print("\n💡 안녕하세요! 어떤 이야기를 나누고 싶으신가요?")
        print("   대화를 종료하려면 '종료' 또는 'quit'을 입력하세요.\n")

        # 2. 메인 대화 루프
        while True:
            print("-" * 50)
            user_input = input("나: ").strip()

            # 3. 종료 명령어 처리
            if user_input.lower() in ['종료', 'quit', 'exit', 'q']:
                print("\n🤖 대화를 종료합니다. 오늘 나눈 대화를 요약해드릴게요.")
                summary_result = chatbot_service.end_conversation()
                
                if summary_result["success"]:
                    print("\n--- 대화 요약 ---")
                    print(summary_result["response"])
                    print("------------------\n")
                else:
                    print(f"오류: 요약 생성에 실패했습니다. ({summary_result['response']})")
                
                print("이용해주셔서 감사합니다! 언제든 다시 찾아주세요. 👋")
                break

            # 4. 빈 입력 처리
            if not user_input:
                print("🤖 메시지를 입력해주세요.")
                continue

            # 5. 챗봇 응답 요청 및 출력
            print("🤖 잠시만요, 답변을 생각하고 있어요...")
            response_data = chatbot_service.get_response(user_input)

            if response_data["success"]:
                print(f"\n챗봇: {response_data['response']}")
            else:
                print(f"\n❌ 오류: 답변을 가져오는 데 실패했습니다. ({response_data['response']})")

    except Exception as e:
        logger.error(f"❌ 시스템에 심각한 오류가 발생했습니다: {e}", exc_info=True)
        print(f"\n죄송합니다. 시스템 오류가 발생하여 챗봇을 실행할 수 없습니다. 로그를 확인해주세요.")


if __name__ == "__main__":
    main() 