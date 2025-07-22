const chatInput = document.getElementById('chat-input');
const sendButton = document.getElementById('send-button');
const chatContainer = document.getElementById('chat-container');
const typingIndicator = document.getElementById('typing-indicator');
const backButton = document.getElementById('back-button');
const popupOverlay = document.getElementById('popup-overlay');
const cancelButton = document.getElementById('cancel-button');
const confirmButton = document.getElementById('confirm-button');

// 뒤로가기 버튼 클릭 이벤트
backButton.addEventListener('click', function() {
    // 대화 내용이 있다면 확인 팝업 표시, 없다면 바로 이동
    const messages = chatContainer.querySelectorAll('.message-bubble');
    if (messages.length > 3) { // 초기 메시지 3개보다 많으면
        popupOverlay.style.display = 'flex';
    } else {
        // 바로 이전 페이지로 이동
        window.history.back();
    }
});

// 팝업 닫기 (아니오 버튼)
cancelButton.addEventListener('click', function() {
    popupOverlay.style.display = 'none';
});

// 팝업 확인 (예 버튼) - 이전 페이지로 이동
confirmButton.addEventListener('click', function() {
    // 팝업 닫기
    popupOverlay.style.display = 'none';
    
    // 이전 페이지로 이동
    window.history.back();
});

// 팝업 외부 클릭 시 닫기
popupOverlay.addEventListener('click', function(e) {
    if (e.target === popupOverlay) {
        popupOverlay.style.display = 'none';
    }
});

// 채팅에 메시지 추가하는 함수
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message-bubble');
    if (sender === 'user') {
        messageDiv.classList.add('user-bubble');
    } else {
        messageDiv.classList.add('ai-bubble');
    }
    messageDiv.innerHTML = `<p>${text}</p>`;
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight; // 맨 아래로 스크롤
}

// AI 응답 시뮬레이션 (실제 앱에서는 Gemini API 호출)
async function getAIResponse(userMessage) {
    typingIndicator.style.display = 'block'; // 타이핑 표시기 보이기
    chatContainer.scrollTop = chatContainer.scrollHeight;

    // API 호출 지연 시뮬레이션
    await new Promise(resolve => setTimeout(resolve, 1000)); 

    typingIndicator.style.display = 'none'; // 타이핑 표시기 숨기기
    // 사용자 입력에 따른 AI 응답 예시
    let aiResponse = "선생님은 제자님의 말씀을 잘 들었어요. 더 자세히 이야기해줄 수 있을까요?";
    if (userMessage.includes("힘들") || userMessage.includes("지쳐")) {
        aiResponse = "힘든 마음이 드셨군요. 선생님은 제자님의 그런 감정을 이해한답니다. 무엇이 제자님을 힘들게 했는지 좀 더 이야기해줄 수 있을까요?";
    } else if (userMessage.includes("기분 좋") || userMessage.includes("행복")) {
        aiResponse = "기분 좋은 일이 있으셨다니 선생님도 기쁘네요! 어떤 일이었는지 더 자세히 들려주세요!";
    }
    addMessage(aiResponse, 'ai');
}

if (sendButton) {
    sendButton.addEventListener('click', function() {
        const userMessage = chatInput.value.trim();
        if (userMessage) {
            addMessage(userMessage, 'user');
            chatInput.value = ''; // 입력창 초기화
            chatInput.style.height = 'auto'; // 텍스트영역 높이 초기화
            getAIResponse(userMessage); // AI 응답 받기
        }
    });
}

if (chatInput) {
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) { // Shift 없이 Enter 키
            e.preventDefault(); // 줄바꿈 방지
            sendButton.click();
        }
    });

    // 텍스트영역 자동 크기 조절
    chatInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
}

// 페이지 로드 시 초기 설정
window.addEventListener('load', function() {
    chatContainer.scrollTop = chatContainer.scrollHeight; // 최신 메시지로 스크롤
}); 