// --- Report Detail Page Scripts ---
// Chart data and config (already defined in HTML, just need to render)
let currentWeekOffset = 0; // 0 for current week, -1 for previous week, etc.
const currentWeekDisplay = document.getElementById('current-week-display');
const prevWeekBtn = document.getElementById('prev-week-btn');
const nextWeekBtn = document.getElementById('next-week-btn');
const reportDiagnosisText = document.getElementById('report-diagnosis-text');
const reportMainKeywords = document.getElementById('report-main-keywords');
const diagnosisBasisBubbles = document.getElementById('diagnosis-basis-bubbles');
const recommendationList = document.getElementById('recommendation-list');
const selfReflectionQuestion = document.getElementById('self-reflection-question');

const weeklyReportData = [
    // Example data for different weeks (replace with real data from backend)
    {
        week: '2025년 7월 2주차', // Current week
        labels: ['월', '화', '수', '목', '금', '토', '일'],
        datasets: [
            { label: '기쁨', data: [5, 6, 7, 6, 8, 7, 9], borderColor: '#DA983C', backgroundColor: 'rgba(218, 152, 60, 0.2)', fill: true, tension: 0.3 },
            { label: '평온', data: [7, 7, 6, 8, 7, 6, 7], borderColor: '#8F9562', backgroundColor: 'rgba(143, 149, 98, 0.2)', fill: true, tension: 0.3 },
            { label: '불안', data: [3, 2, 3, 2, 1, 2, 1], borderColor: '#B87B5C', backgroundColor: 'rgba(184, 123, 92, 0.2)', fill: true, tension: 0.3 },
            { label: '피로', data: [6, 5, 4, 5, 4, 3, 2], borderColor: '#495235', backgroundColor: 'rgba(73, 82, 53, 0.2)', fill: true, tension: 0.3 }
        ],
        diagnosis: '제자님, [2025년 7월 2주차] 기록들을 분석해보니, 전반적으로 **차분함과 소소한 기쁨**이 느껴지는 한편, 때때로 **작은 불안감**도 함께 스쳐 지나가는 모습이 보입니다. 특히 [구체적인 날짜/사건]에 대한 기록에서 [특정 감정]이 두드러지게 나타났어요. 이는 [원인 추정] 때문일 수 있겠네요. 하지만 어려운 상황 속에서도 긍정적인 면을 찾으려 노력하는 제자님의 마음이 참 아름답습니다.',
        keywords: '#차분함 #기쁨 #불안감 #노력',
        basisBubbles: [
            "오늘 햇살이 너무 좋아서 기분 좋게 일어났어요.",
            "점심으로 맛있는 파스타를 먹었는데, 정말 행복했어요!",
            "프로젝트 회의가 있었는데, 아이디어가 잘 나와서 뿌듯했어요.",
            "하지만 발표 준비 때문에 밤늦게까지 잠을 설쳤어요.",
            "내일은 더 잘할 수 있을 거라는 희망이 생겼답니다."
        ],
        recommendations: [
            { title: '🌿 차분히 산책하기', desc: '가까운 공원이나 조용한 길을 걸으며 신선한 공기를 마시고 자연을 느껴보세요. 마음이 한결 편안해질 거예요.' },
            { title: '🎧 좋아하는 음악 듣기', desc: '편안한 자세로 좋아하는 음악을 들으며 잠시 모든 것을 잊고 휴식하는 시간을 가져보세요. 감정 해소에 도움이 된답니다.' },
            { title: '☕ 따뜻한 차 한 잔', desc: '따뜻한 차를 마시며 잠시 멈춰 서서 오늘 하루를 되돌아보는 시간을 가져보세요. 차분한 생각에 잠기기 좋습니다.' }
        ],
        reflection: '제자님, 혹시 최근에 [반복되는 감정]을 느끼는 특별한 이유가 있었을까요? 그리고 [추천 놀이/행동] 중에서 가장 마음에 드는 것은 무엇인가요? 선생님은 언제나 제자님의 성장을 응원한답니다.'
    },
    {
        week: '2025년 7월 1주차', // Previous week
        labels: ['월', '화', '수', '목', '금', '토', '일'],
        datasets: [
            { label: '기쁨', data: [3, 4, 5, 4, 6, 5, 7], borderColor: '#DA983C', backgroundColor: 'rgba(218, 152, 60, 0.2)', fill: true, tension: 0.3 },
            { label: '평온', data: [6, 6, 5, 7, 6, 5, 6], borderColor: '#8F9562', backgroundColor: 'rgba(143, 149, 98, 0.2)', fill: true, tension: 0.3 },
            { label: '불안', data: [4, 3, 4, 3, 2, 3, 2], borderColor: '#B87B5C', backgroundColor: 'rgba(184, 123, 92, 0.2)', fill: true, tension: 0.3 },
            { label: '피로', data: [7, 6, 5, 6, 5, 4, 3], borderColor: '#495235', backgroundColor: 'rgba(73, 82, 53, 0.2)', fill: true, tension: 0.3 }
        ],
        diagnosis: '제자님, [2025년 7월 1주차] 기록들을 분석해보니, 한 주간 **피로감**이 다소 높게 나타났으며, [특정 요일]에 [특정 감정]이 두드러졌습니다. 하지만 주말에는 [긍정적 감정]을 회복하려는 노력이 보였어요. 꾸준히 자신을 돌보는 것이 중요하답니다.',
        keywords: '#피로 #회복 #노력 #주말',
        basisBubbles: [
            "이번 주 내내 야근 때문에 너무 지쳤어요.",
            "피곤해서 아무것도 하기 싫은 날도 있었지만, 주말에 푹 쉬었어요.",
            "오랜만에 친구 만나서 맛있는 거 먹으니 기분이 좀 나아졌어요."
        ],
        recommendations: [
            { title: '😴 충분한 휴식 취하기', desc: '몸과 마음의 피로를 풀기 위해 충분한 수면 시간을 확보하고, 낮잠을 자는 것도 좋아요.' },
            { title: '🧘‍♀️ 명상 또는 스트레칭', desc: '짧은 시간이라도 명상이나 가벼운 스트레칭으로 몸의 긴장을 풀어보세요.' }
        ],
        reflection: '제자님, 한 주간 피로감이 높았던 이유가 무엇이라고 생각하시나요? 다음 주에는 어떤 활동으로 에너지를 채우고 싶으신가요? 선생님은 언제나 제자님의 건강을 가장 중요하게 생각한답니다.'
    }
];

let emotionChartInstance = null; // Chart.js 인스턴스를 저장할 변수

function updateReportContent(weekIndex) {
    const report = weeklyReportData[weekIndex];
    if (!report) {
        // No data for this week, show a message
        currentWeekDisplay.innerText = "리포트 없음";
        reportDiagnosisText.innerText = "선생님의 감정 진단 (현상)";
        reportMainKeywords.innerText = "";
        diagnosisBasisBubbles.innerHTML = '<p class="text-[#8F9562] text-center py-4">해당 주차의 리포트가 아직 준비되지 않았습니다.</p>';
        recommendationList.innerHTML = '';
        selfReflectionQuestion.innerText = '아직 리포트가 없어 선생님의 질문도 준비되지 않았어요.';

        // Destroy existing chart if any
        if (emotionChartInstance) {
            emotionChartInstance.destroy();
            emotionChartInstance = null;
        }
        document.querySelector('.chart-container').innerHTML = '<canvas id="emotionTrendChart"></canvas>'; // Re-add canvas
        return;
    }

    currentWeekDisplay.innerText = report.week;
    reportDiagnosisText.innerText = report.diagnosis;
    reportMainKeywords.innerText = `주요 감정 키워드: ${report.keywords}`;
    selfReflectionQuestion.innerText = report.reflection;

    // Update Diagnosis Basis Bubbles
    diagnosisBasisBubbles.innerHTML = '';
    report.basisBubbles.forEach(text => {
        const span = document.createElement('span');
        span.className = 'keyword-bubble';
        span.innerText = text;
        diagnosisBasisBubbles.appendChild(span);
    });

    // Update Recommendations
    recommendationList.innerHTML = '';
    report.recommendations.forEach(rec => {
        const li = document.createElement('li');
        li.className = 'recommendation-item';
        li.innerHTML = `<h3 class="text-lg font-semibold text-[#90533B] mb-1">${rec.title}</h3>
                                <p class="text-[#495235] text-sm">${rec.desc}</p>`;
        recommendationList.appendChild(li);
    });

    // Update Chart
    if (emotionChartInstance) {
        emotionChartInstance.destroy(); // Destroy previous chart instance
    }
    const ctx = document.getElementById('emotionTrendChart').getContext('2d');
    emotionChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: report.labels,
            datasets: report.datasets.map(ds => ({
                ...ds,
                borderColor: ds.borderColor, // Use defined colors
                backgroundColor: ds.backgroundColor,
                fill: ds.fill,
                tension: ds.tension
            }))
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top', labels: { color: '#495235', font: { family: 'Noto Sans KR', size: 14 } } },
                title: { display: false }
            },
            scales: {
                x: { grid: { color: '#E0E0E0' }, ticks: { color: '#495235', font: { family: 'Noto Sans KR' } } },
                y: { beginAtZero: true, max: 10, grid: { color: '#E0E0E0' }, ticks: { color: '#495235', font: { family: 'Noto Sans KR' } } }
            }
        }
    });

    // Enable/disable navigation buttons
    prevWeekBtn.disabled = (currentWeekOffset >= weeklyReportData.length -1); // Cannot go further back than available data
    nextWeekBtn.disabled = (currentWeekOffset <= 0); // Cannot go further into the future than current week

    if (prevWeekBtn.disabled) {
        prevWeekBtn.classList.add('opacity-50', 'cursor-not-allowed');
    } else {
        prevWeekBtn.classList.remove('opacity-50', 'cursor-not-allowed');
    }
    if (nextWeekBtn.disabled) {
        nextWeekBtn.classList.add('opacity-50', 'cursor-not-allowed');
    } else {
        nextWeekBtn.classList.remove('opacity-50', 'cursor-not-allowed');
    }
}

// Event listeners for week navigation
prevWeekBtn.addEventListener('click', () => {
    currentWeekOffset++;
    updateReportContent(currentWeekOffset);
});

nextWeekBtn.addEventListener('click', () => {
    currentWeekOffset--;
    updateReportContent(currentWeekOffset);
});

// Initial render of the report page
window.addEventListener('load', function() {
    updateReportContent(currentWeekOffset); // Show current week's report on load
});

// --- AI Chat Page Scripts ---
const chatInput = document.getElementById('chat-input');
const sendButton = document.getElementById('send-button');
const chatContainer = document.querySelector('.chat-container');
const typingIndicator = document.getElementById('typing-indicator');

// Function to add message to chat
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
    chatContainer.scrollTop = chatContainer.scrollHeight; // Scroll to bottom
}

// Simulate AI response (in real app, call Gemini API)
async function getAIResponse(userMessage) {
    typingIndicator.classList.remove('hidden');
    chatContainer.scrollTop = chatContainer.scrollHeight;

    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 1500));

    typingIndicator.classList.add('hidden');
    // Example AI response based on user input
    let aiResponse = "선생님은 제자님의 말씀을 잘 들었어요. 더 자세히 이야기해줄 수 있을까요?";
    if (userMessage.includes("힘들") || userMessage.includes("지쳐")) {
        aiResponse = "힘든 마음이 드셨군요. 선생님은 제자님의 그런 감정을 이해한답니다. 무엇이 제자님을 힘들게 했는지 좀 더 이야기해줄 수 있을까요?";
    } else if (userMessage.includes("기분 좋") || userMessage.includes("행복")) {
        aiResponse = "기분 좋은 일이 있으셨다니 선생님도 기쁘네요! 어떤 일이었는지 더 자세히 들려주세요!";
    }
    addMessage(aiResponse, 'ai');
}

if (sendButton) { // Check if element exists before adding listener
    sendButton.addEventListener('click', function() {
        const userMessage = chatInput.value.trim();
        if (userMessage) {
            addMessage(userMessage, 'user');
            chatInput.value = ''; // Clear input
            getAIResponse(userMessage); // Get AI response
        }
    });
}

if (chatInput) { // Check if element exists before adding listener
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) { // Enter key without Shift
            e.preventDefault(); // Prevent new line
            sendButton.click();
        }
    });
}

// Initial AI message on load for Chat Page
window.addEventListener('load', function() {
    // Only add initial message if chatContainer is part of the current view (e.g., not hidden)
    // For this combined mockup, it will always be present, so check if it's not empty
    if (chatContainer && chatContainer.children.length <= 1) { // Check if only system message
        addMessage("안녕하세요, 제자님! 리포트를 보니 최근 감정 변화가 있었네요. 어떤 점이 가장 궁금하신가요?", 'ai');
    }
});

// --- Point Shop Page Scripts ---
let currentPoints = 1250; // 사용자 현재 포인트 (예시)
const currentPointsDisplay = document.getElementById('current-points');
const shopItemsSection = document.getElementById('shop-items-section');
const myStampsCollectionSection = document.getElementById('my-stamps-collection-section');
const ownedStampsGrid = document.getElementById('owned-stamps-grid');
const toggleMyStampsBtn = document.getElementById('toggle-my-stamps-btn');

// 모든 도장 아이템 데이터 (상점과 보유 목록 렌더링에 사용)
const allStampItems = [
    { id: 'stamp0', name: '지장', desc: '특별한 날에만 만날 수 있는 한정판 도장입니다.', cost: 1500, img: 'https://placehold.co/100x100/DA983C/FFFFFF?text=지장' },
    { id: 'stamp1', name: '참 잘했어요 도장', desc: '기본적인 격려 도장입니다.', cost: 500, img: 'http://googleusercontent.com/file_content/4' },
    { id: 'stamp2', name: '최고예요 도장', desc: '특별한 성취를 축하하는 도장입니다.', cost: 800, img: 'https://placehold.co/100x100/8F9562/FFFFFF?text=최고예요' },
    { id: 'stamp3', name: '칭찬해요 도장', desc: '노력에 대한 칭찬을 담은 도장입니다.', cost: 700, img: 'https://placehold.co/100x100/B87B5C/FFFFFF?text=칭찬해요' },
    { id: 'stamp4', name: '잘했어요 도장', desc: '꾸준함에 대한 격려 도장입니다.', cost: 600, img: 'https://placehold.co/100x100/495235/FFFFFF?text=잘했어요' },
    { id: 'stamp5', name: '고마워요 도장', desc: '감사의 마음을 전하는 도장입니다.', cost: 900, img: 'https://placehold.co/100x100/90533B/FFFFFF?text=고마워요' },
    { id: 'stamp6', name: '특별한 날 도장', desc: '기념하고 싶은 날에 사용하는 도장입니다.', cost: 1200, img: 'https://placehold.co/100x100/DA983C/FFFFFF?text=특별한날' }
];

// 사용자가 보유한 도장 ID 목록 (예시)
let ownedStampIds = ['stamp1', 'stamp3'];

function updatePointsDisplay() {
    if (currentPointsDisplay) {
        currentPointsDisplay.innerText = currentPoints.toLocaleString() + ' P';
    }
}

function checkBuyButtonsAvailability() {
    document.querySelectorAll('.btn-buy').forEach(button => {
        const cost = parseInt(button.dataset.cost);
        const stampId = button.closest('.shop-item-card').dataset.stampId;

        if (currentPoints >= cost && !ownedStampIds.includes(stampId)) {
            button.classList.remove('disabled');
            button.disabled = false;
            button.innerText = '구매하기';
        } else if (ownedStampIds.includes(stampId)) {
            button.classList.add('disabled');
            button.disabled = true;
            button.innerText = '보유 중';
        } else {
            button.classList.add('disabled');
            button.disabled = true;
            button.innerText = '포인트 부족';
        }
    });
}

function renderOwnedStamps() {
    if (!ownedStampsGrid) return;
    ownedStampsGrid.innerHTML = '';
    if (ownedStampIds.length === 0) {
        ownedStampsGrid.innerHTML = '<p class="col-span-full text-center text-[#8F9562] py-4">아직 보유한 도장이 없어요. 상점에서 새로운 도장을 구매해보세요!</p>';
        return;
    }

    ownedStampIds.forEach(id => {
        const stamp = allStampItems.find(item => item.id === id);
        if (stamp) {
            const card = document.createElement('div');
            card.className = 'owned-stamp-card';
            card.innerHTML = `
                        <img src="${stamp.img}" alt="${stamp.name}" class="stamp-preview-image-shop">
                        <h3 class="text-xl font-semibold text-[#90533B] mb-2">총총총 ${stamp.name}</h3>
                        <p class="text-[#495235] mb-4">${stamp.desc}</p>
                        <button class="btn-apply" data-stamp-id="${stamp.id}" data-stamp-name="${stamp.name}">적용하기</button>
                    `;
            ownedStampsGrid.appendChild(card);
        }
    });

    document.querySelectorAll('.btn-apply').forEach(button => {
        button.addEventListener('click', function() {
            const stampName = this.dataset.stampName;
            alert(`${stampName} 도장을 적용했습니다!`);
        });
    });
}

function showShopView() {
    if (!shopItemsSection || !myStampsCollectionSection || !toggleMyStampsBtn) return;
    shopItemsSection.classList.remove('hidden');
    myStampsCollectionSection.classList.add('hidden');
    toggleMyStampsBtn.innerText = '내 도장 목록 보기';
    checkBuyButtonsAvailability();
}

function showMyStampsView() {
    if (!shopItemsSection || !myStampsCollectionSection || !toggleMyStampsBtn) return;
    shopItemsSection.classList.add('hidden');
    myStampsCollectionSection.classList.remove('hidden');
    toggleMyStampsBtn.innerText = '상점으로 돌아가기';
    renderOwnedStamps();
}

if (toggleMyStampsBtn) {
    toggleMyStampsBtn.addEventListener('click', function() {
        if (shopItemsSection.classList.contains('hidden')) {
            showShopView();
        } else {
            showMyStampsView();
        }
    });
}

document.querySelectorAll('.btn-buy').forEach(button => {
    button.addEventListener('click', function() {
        const cost = parseInt(this.dataset.cost);
        const stampName = this.dataset.stampName;
        const stampId = this.closest('.shop-item-card').dataset.stampId;

        if (currentPoints >= cost) {
            if (confirm(`${stampName} 도장을 ${cost} 포인트로 구매하시겠어요?`)) {
                currentPoints -= cost;
                ownedStampIds.push(stampId);
                updatePointsDisplay();
                checkBuyButtonsAvailability();
                alert(`${stampName} 도장을 구매했습니다! 남은 포인트: ${currentPoints} P`);
            }
        } else {
            alert('포인트가 부족합니다!');
        }
    });
});

// Initial setup for Point Shop on load
window.addEventListener('load', function() {
    updatePointsDisplay();
    showShopView();
});