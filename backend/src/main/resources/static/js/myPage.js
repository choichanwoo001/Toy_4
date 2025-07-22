// 시간 및 분 드롭다운 채우기
function populateTimeSelectors() {
    const hourSelect = document.getElementById('comment-hour');
    const minuteSelect = document.getElementById('comment-minute');

    // 시간 (00-23)
    for (let i = 0; i < 24; i++) {
        const option = document.createElement('option');
        option.value = String(i).padStart(2, '0');
        option.textContent = String(i).padStart(2, '0');
        hourSelect.appendChild(option);
    }

    // 분 (00-59)
    for (let i = 0; i < 60; i++) {
        const option = document.createElement('option');
        option.value = String(i).padStart(2, '0');
        option.textContent = String(i).padStart(2, '0');
        minuteSelect.appendChild(option);
    }

    // 현재 시간을 기본값으로 설정 (선택 사항)
    const now = new Date();
    hourSelect.value = String(now.getHours()).padStart(2, '0');
    minuteSelect.value = String(now.getMinutes()).padStart(2, '0');
}
window.onload = populateTimeSelectors; 