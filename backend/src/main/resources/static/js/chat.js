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
    if (messages.length > 1) { // 초기 메시지 1개보다 많으면 (사용자가 대화한 경우)
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
    
    // 대화 요약 요청 후 이전 페이지로 이동
    getChatSummary().then(() => {
        // 요약 표시 후 잠시 후 이동
        setTimeout(() => {
            window.history.back();
        }, 3000); // 3초 후 이동
    });
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
    // 줄바꿈 문자를 <br> 태그로 변환
    const formattedText = text.replace(/\n/g, '<br>');
    messageDiv.innerHTML = `<p>${formattedText}</p>`;
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight; // 맨 아래로 스크롤
}

// AI 응답 시뮬레이션 (실제 앱에서는 Gemini API 호출)
async function getAIResponse(userMessage) {
    typingIndicator.style.display = 'block'; // 타이핑 표시기 보이기
    chatContainer.scrollTop = chatContainer.scrollHeight;

    try {
        // Spring Boot API 호출
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'message': userMessage
            })
        });

        if (!response.ok) {
            throw new Error('네트워크 응답이 정상적이지 않습니다.');
        }

        const data = await response.json();
        
        typingIndicator.style.display = 'none'; // 타이핑 표시기 숨기기
        
        if (data.success) {
            addMessage(data.response, 'ai');
        } else {
            addMessage(data.error || '죄송합니다. 응답을 생성하는 중 오류가 발생했습니다.', 'ai');
        }
        
    } catch (error) {
        console.error('채팅 API 호출 오류:', error);
        typingIndicator.style.display = 'none'; // 타이핑 표시기 숨기기
        addMessage('네트워크 오류가 발생했습니다. 인터넷 연결을 확인하고 다시 시도해주세요.', 'ai');
    }
}

// 대화 요약을 요청하는 함수
async function getChatSummary() {
    try {
        addMessage("대화를 종료합니다. 지금까지의 대화를 요약해드릴게요...", 'ai');
        
        const response = await fetch('/api/chat/summary', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        });

        if (!response.ok) {
            throw new Error('요약 요청 중 네트워크 오류가 발생했습니다.');
        }

        const data = await response.json();
        
        if (data.success) {
            addMessage("📝 대화 요약:\n\n" + data.summary, 'ai');
            addMessage("이용해주셔서 감사합니다! 언제든 다시 찾아주세요. 👋", 'ai');
        } else {
            addMessage(data.error || '요약을 생성하는 중 오류가 발생했습니다.', 'ai');
        }
        
    } catch (error) {
        console.error('대화 요약 API 호출 오류:', error);
        addMessage('요약 생성 중 오류가 발생했습니다. 이용해주셔서 감사합니다!', 'ai');
    }
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