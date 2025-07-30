// 📌 상태 변수
let validOffsets = [];
let currentIndex = 0;
let emotionChartInstance = null;

// 📌 세션에서 userId를 Thymeleaf로 안전하게 받음
let reportUserId = window.reportUserId;

// 📌 DOM 요소
const currentWeekDisplay = document.getElementById('current-week-display');
const prevWeekBtn = document.getElementById('prev-week-btn');
const nextWeekBtn = document.getElementById('next-week-btn');
const reportEmotionSummary = document.getElementById('report-emotion-summary');
const reportMainKeywords = document.getElementById('report-main-keywords');
const diagnosisBasisBubbles = document.getElementById('diagnosis-basis-bubbles');
const recommendationList = document.getElementById('recommendation-list');

// 📌 유틸 함수: 월요일 기준 주차 문자열 생성
function getMonday(date) {
    const d = new Date(date);
    const day = d.getDay();
    const diff = d.getDate() - day + (day === 0 ? -6 : 1);
    return new Date(d.setDate(diff));
}

function getWeekFromOffset(offset) {
    const today = new Date();
    const baseMonday = getMonday(today);
    const targetMonday = new Date(baseMonday);
    targetMonday.setDate(baseMonday.getDate() + offset * 7);

    const yyyy = targetMonday.getFullYear();
    const mm = String(targetMonday.getMonth() + 1).padStart(2, '0');
    const dd = String(targetMonday.getDate()).padStart(2, '0');
    return `${yyyy}년 ${mm}월 ${dd}일 주차`;
}

// 📌 API 호출 함수
async function loadWeeklyReport(weekOffset) {
    try {
        console.log(`🔍 API 호출: /api/report?userId=${reportUserId}&weekOffset=${weekOffset}`);
        const response = await fetch(`/api/report?userId=${reportUserId}&weekOffset=${weekOffset}`);
        console.log(`📡 API 응답 상태:`, response.status);
        
        if (!response.ok) {
            console.error(`❌ API 응답 실패: ${response.status}`);
            throw new Error('리포트 데이터를 불러오지 못했습니다.');
        }
        
        const data = await response.json();
        console.log(`📊 API 응답 데이터:`, data);
        return data;
    } catch (error) {
        console.error(`❌ API 호출 오류:`, error);
        return null;
    }
}

// 📌 리포트 렌더링
async function updateReportContent(weekOffset) {
    const report = await loadWeeklyReport(weekOffset);
    console.log('Report data:', report); // 디버깅용 로그
    
    const isEmptyReport = !report
        || (report.emotionSummary === "이번 주 감정 분석이 준비되지 않았습니다." && report.evidenceSentences.length === 0 && report.recommendations.length === 0);

    if (isEmptyReport) {
        currentWeekDisplay.innerText = `${report?.week ?? getWeekFromOffset(weekOffset)} (리포트 없음)`;
        reportEmotionSummary.innerText = "선생님의 감정 진단 (현상)";
        reportMainKeywords.innerText = "";
        diagnosisBasisBubbles.innerHTML = '<p class="text-[#8F9562] text-center py-4">해당 주차의 리포트가 아직 준비되지 않았습니다.</p>';
        recommendationList.innerHTML = '';

        if (emotionChartInstance) {
            emotionChartInstance.destroy();
            emotionChartInstance = null;
        }
        document.querySelector('.chart-container').innerHTML = '<canvas id="emotionTrendChart"></canvas>';
        return;
    }

    currentWeekDisplay.innerText = report.week;
    reportEmotionSummary.innerText = report.emotionSummary;

    diagnosisBasisBubbles.innerHTML = '';
    report.evidenceSentences.forEach(text => {
        const span = document.createElement('span');
        span.className = 'keyword-bubble';
        span.innerText = text;
        diagnosisBasisBubbles.appendChild(span);
    });

    recommendationList.innerHTML = '';
    report.recommendations.forEach(rec => {
        const li = document.createElement('li');
        li.className = 'recommendation-item';
        li.innerHTML = `
            <h3 class="text-lg font-semibold text-[#90533B] mb-1">${rec.title}</h3>
            <p class="text-[#495235] text-sm">${rec.description}</p>`;
        recommendationList.appendChild(li);
    });

    if (emotionChartInstance) emotionChartInstance.destroy();
    
    console.log(`📈 감정 차트 데이터 확인:`, report.emotionCharts);
    console.log(`📈 감정 차트 개수:`, report.emotionCharts ? report.emotionCharts.length : 0);
    
    // 감정 차트 데이터가 있는지 확인
    if (report.emotionCharts && report.emotionCharts.length > 0) {
        console.log(`✅ 감정 차트 데이터가 있습니다. 차트를 생성합니다.`);
        const ctx = document.getElementById('emotionTrendChart').getContext('2d');
        console.log(`🎨 Canvas 컨텍스트:`, ctx);
        
        emotionChartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: report.dayLabels || ['월', '화', '수', '목', '금', '토', '일'],
                datasets: report.emotionCharts.map(e => ({
                    label: e.emotionLabel,
                    data: e.emotionData,
                    borderColor: e.borderColor,
                    backgroundColor: e.backgroundColor,
                    fill: true,
                    tension: 0.3,
                    borderWidth: 2
                }))
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { 
                        position: 'top', 
                        labels: { 
                            color: '#495235', 
                            font: { family: 'Noto Sans KR', size: 14 },
                            usePointStyle: true,
                            padding: 20
                        } 
                    },
                    title: { display: false }
                },
                scales: {
                    x: { 
                        grid: { color: '#E0E0E0' }, 
                        ticks: { color: '#495235', font: { family: 'Noto Sans KR' } } 
                    },
                    y: { 
                        beginAtZero: true, 
                        max: 10, 
                        grid: { color: '#E0E0E0' }, 
                        ticks: { color: '#495235', font: { family: 'Noto Sans KR' } } 
                    }
                },
                interaction: {
                    intersect: false,
                    mode: 'index'
                }
            }
        });
    } else {
        // 감정 차트 데이터가 없을 때 빈 차트 표시
        const ctx = document.getElementById('emotionTrendChart').getContext('2d');
        emotionChartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['월', '화', '수', '목', '금', '토', '일'],
                datasets: []
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    title: { 
                        display: true, 
                        text: '감정 데이터가 없습니다',
                        color: '#8F9562',
                        font: { family: 'Noto Sans KR', size: 16 }
                    }
                },
                scales: {
                    x: { grid: { color: '#E0E0E0' }, ticks: { color: '#495235', font: { family: 'Noto Sans KR' } } },
                    y: { beginAtZero: true, max: 10, grid: { color: '#E0E0E0' }, ticks: { color: '#495235', font: { family: 'Noto Sans KR' } } }
                }
            }
        });
    }

    // 버튼 상태
    prevWeekBtn.disabled = currentIndex >= validOffsets.length - 1;
    nextWeekBtn.disabled = currentIndex <= 0;

    prevWeekBtn.classList.toggle('opacity-50', prevWeekBtn.disabled);
    prevWeekBtn.classList.toggle('cursor-not-allowed', prevWeekBtn.disabled);
    nextWeekBtn.classList.toggle('opacity-50', nextWeekBtn.disabled);
    nextWeekBtn.classList.toggle('cursor-not-allowed', nextWeekBtn.disabled);
}

// 📌 주차 목록 로딩
async function initReportPage() {
    // URL 파라미터에서 weekOffset 가져오기
    const urlParams = new URLSearchParams(window.location.search);
    const weekOffset = urlParams.get('weekOffset');

    // userId가 없으면 로그인 페이지로 리다이렉트
    if (!reportUserId) {
        console.error('사용자 ID가 없습니다. 로그인이 필요합니다.');
        window.location.href = '/?loginRequired=true';
        return;
    }

    const res = await fetch(`/api/report/weeks?userId=${reportUserId}`);
    validOffsets = await res.json();

    if (validOffsets.length === 0) {
        currentWeekDisplay.innerText = '리포트 없음';
        return;
    }

    // URL에서 전달받은 weekOffset이 있으면 해당 주차로 설정
    if (weekOffset !== null) {
        const targetWeekOffset = parseInt(weekOffset);
        const weekIndex = validOffsets.indexOf(targetWeekOffset);
        if (weekIndex !== -1) {
            currentIndex = weekIndex;
        } else {
            // 해당 주차가 없으면 첫 번째 주차로 설정
            currentIndex = 0;
        }
    } else {
        currentIndex = 0;
    }
    
    updateReportContent(validOffsets[currentIndex]);
}

// 📌 버튼 이벤트
prevWeekBtn.addEventListener('click', () => {
    if (currentIndex < validOffsets.length - 1) {
        currentIndex++;
        updateReportContent(validOffsets[currentIndex]);
    }
});

nextWeekBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        updateReportContent(validOffsets[currentIndex]);
    }
});

document.getElementById('go-chat').addEventListener('click', () => {
    // 채팅 페이지로 이동할 때 현재 사용자 정보도 함께 전달
    const chatUrl = reportUserId ? `/chat?userId=${reportUserId}` : '/chat';
    window.location.href = chatUrl;
});

// 📌 초기 실행
window.addEventListener('load', () => {
    initReportPage();
});