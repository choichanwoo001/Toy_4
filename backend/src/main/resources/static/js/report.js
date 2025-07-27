// 📌 상태 변수
let validOffsets = [];
let currentIndex = 0;
let emotionChartInstance = null;

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
        const userId = /*[[${user != null}]]*/ false ? '[[${user.userId}]]' : 1;
const response = await fetch(`/api/report?userId=${userId}&weekOffset=${weekOffset}`);
        if (!response.ok) throw new Error('리포트 데이터를 불러오지 못했습니다.');
        return await response.json();
    } catch (error) {
        console.error(error);
        return null;
    }
}

// 📌 리포트 렌더링
async function updateReportContent(weekOffset) {
    const report = await loadWeeklyReport(weekOffset);
    const isEmptyReport = !report
        || (!report.emotionSummary && report.evidenceSentences.length === 0 && report.recommendations.length === 0);

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
    const ctx = document.getElementById('emotionTrendChart').getContext('2d');
    emotionChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: report.dayLabels,
            datasets: report.emotionCharts.map(e => ({
                label: e.emotionLabel,
                data: e.emotionData,
                borderColor: e.borderColor,
                backgroundColor: e.backgroundColor,
                fill: true,
                tension: 0.3
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
    const userId = /*[[${user != null}]]*/ false ? '[[${user.userId}]]' : 1;
const res = await fetch(`/api/report/weeks?userId=${userId}`);
    validOffsets = await res.json();

    if (validOffsets.length === 0) {
        currentWeekDisplay.innerText = '리포트 없음';
        return;
    }

    currentIndex = 0;
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
    window.location.href = '/chat';
});

// 📌 초기 실행
window.addEventListener('load', () => {
    initReportPage();
});