// 시간 드롭다운만 채우기
function populateTimeSelectors() {
    const hourSelect = document.getElementById('comment-hour');

    // 시간 (00-23)
    for (let i = 0; i < 24; i++) {
        const option = document.createElement('option');
        option.value = String(i).padStart(2, '0');
        option.textContent = String(i).padStart(2, '0');
        hourSelect.appendChild(option);
    }
}
window.onload = populateTimeSelectors; 