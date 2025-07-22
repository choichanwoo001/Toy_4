let currentWeekOffset = 0; // 0 = 이번 주, -1 = 지난 주 등
let emotionChartInstance = null;

const currentWeekDisplay = document.getElementById('current-week-display');
const prevWeekBtn = document.getElementById('prev-week-btn');
const nextWeekBtn = document.getElementById('next-week-btn');
const reportEmotionSummary = document.getElementById('report-emotion-summary');
const reportMainKeywords = document.getElementById('report-main-keywords');
const diagnosisBasisBubbles = document.getElementById('diagnosis-basis-bubbles');
const recommendationList = document.getElementById('recommendation-list');

// 📌 API 호출 함수
async function loadWeeklyReport(weekOffset = 0) {
    try {
        const response = await fetch(`/api/report?userId=1&weekOffset=${weekOffset}`);
        if (!response.ok) throw new Error('리포트 데이터를 불러오지 못했습니다.');
        return await response.json();
    } catch (error) {
        console.error(error);
        return null;
    }
}

// 📌 주차별 리포트 렌더링
async function updateReportContent(weekOffset) {
    const report = await loadWeeklyReport(weekOffset);

    if (!report) {
        currentWeekDisplay.innerText = "리포트 없음";
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

    // 텍스트 반영
    currentWeekDisplay.innerText = report.week;
    reportEmotionSummary.innerText = report.emotionSummary;
    // reportMainKeywords.innerText = `주요 감정 키워드: ${report.keywords}`;

    // 진단 근거
    diagnosisBasisBubbles.innerHTML = '';
    report.evidenceSentences.forEach(text => {
        const span = document.createElement('span');
        span.className = 'keyword-bubble';
        span.innerText = text;
        diagnosisBasisBubbles.appendChild(span);
    });

    // 추천 행동
    recommendationList.innerHTML = '';
    report.recommendations.forEach(rec => {
        const li = document.createElement('li');
        li.className = 'recommendation-item';
        li.innerHTML = `
            <h3 class="text-lg font-semibold text-[#90533B] mb-1">${rec.title}</h3>
            <p class="text-[#495235] text-sm">${rec.description}</p>`;
        recommendationList.appendChild(li);
    });

    // 차트
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
    prevWeekBtn.disabled = false;
    nextWeekBtn.disabled = (currentWeekOffset >= 0);

    prevWeekBtn.classList.toggle('opacity-50', prevWeekBtn.disabled);
    prevWeekBtn.classList.toggle('cursor-not-allowed', prevWeekBtn.disabled);
    nextWeekBtn.classList.toggle('opacity-50', nextWeekBtn.disabled);
    nextWeekBtn.classList.toggle('cursor-not-allowed', nextWeekBtn.disabled);
}

// 📌 버튼 이벤트
prevWeekBtn.addEventListener('click', () => {
    currentWeekOffset++;
    updateReportContent(currentWeekOffset);
});
nextWeekBtn.addEventListener('click', () => {
    if (currentWeekOffset > 0) return;
    currentWeekOffset--;
    updateReportContent(currentWeekOffset);
});
document.getElementById('go-chat').addEventListener('click', () => {
    window.location.href = '/chat';
});

// 📌 페이지 진입 시 기본 리포트 로딩
window.addEventListener('load', () => {
    updateReportContent(currentWeekOffset);
});
