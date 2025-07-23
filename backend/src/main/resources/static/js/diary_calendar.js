// ===================== DIARY CALENDAR PAGE SCRIPTS =====================

// Loading state management
let isLoading = false;

// Skeleton UI functions
function showCalendarSkeleton() {
    const calendarGrid = document.getElementById('calendar-grid');
    calendarGrid.innerHTML = `
        <div class="skeleton skeleton-calendar"></div>
    `;
}

function showRecordsSkeleton() {
    const recordsList = document.getElementById('today-records-list-scrollable');
    recordsList.innerHTML = '';
    for (let i = 0; i < 5; i++) {
        const skeletonItem = document.createElement('div');
        skeletonItem.className = 'skeleton skeleton-record';
        recordsList.appendChild(skeletonItem);
    }
}

function showWeeklyReportsSkeleton() {
    const reportsList = document.getElementById('weekly-reports-list');
    reportsList.innerHTML = '';
    for (let i = 0; i < 4; i++) {
        const skeletonItem = document.createElement('div');
        skeletonItem.className = 'skeleton skeleton-record';
        reportsList.appendChild(skeletonItem);
    }
}

function hideSkeletons() {
    // Skeletons will be replaced by actual content
}

// Lazy loading for images
function lazyLoadImage(img) {
    if (img.dataset.src) {
        img.classList.add('loading');
        img.src = img.dataset.src;
        img.onload = function() {
            img.classList.remove('loading');
            img.removeAttribute('data-src');
        };
        img.onerror = function() {
            img.classList.remove('loading');
            img.style.display = 'none';
        };
    }
}

// Intersection Observer for lazy loading
const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            lazyLoadImage(img);
            observer.unobserve(img);
        }
    });
});

// Error handling
function showErrorMessage(message) {
    // Create error notification
    const errorDiv = document.createElement('div');
    errorDiv.className = 'fixed top-4 right-4 bg-red-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 max-w-sm';
    errorDiv.innerHTML = `
        <div class="flex items-center">
            <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path>
            </svg>
            <span>${message}</span>
            <button onclick="this.parentElement.parentElement.remove()" class="ml-4 text-white hover:text-gray-200">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                </svg>
            </button>
        </div>
    `;
    document.body.appendChild(errorDiv);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (errorDiv.parentElement) {
            errorDiv.remove();
        }
    }, 5000);
}

// Success message handling
function showSuccessMessage(message) {
    // Create success notification
    const successDiv = document.createElement('div');
    successDiv.className = 'fixed top-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 max-w-sm';
    successDiv.innerHTML = `
        <div class="flex items-center">
            <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
            <span>${message}</span>
            <button onclick="this.parentElement.parentElement.remove()" class="ml-4 text-white hover:text-gray-200">
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                </svg>
            </button>
        </div>
    `;
    document.body.appendChild(successDiv);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        if (successDiv.parentElement) {
            successDiv.remove();
        }
    }, 3000);
}

// Global variables
const aiCommentSection = document.getElementById('ai-comment-section');
const newRecordSection = document.getElementById('new-record-section');
const toggleCommentRecordBtn = document.getElementById('toggle-comment-record-btn');
const recordsListScrollable = document.getElementById('today-records-list-scrollable');
const noRecordsPlaceholder = document.getElementById('no-records-placeholder');
const saveDiaryBtn = document.getElementById('save-diary-btn');
const diaryContent = document.getElementById('diary-content');
const aiChatButton = document.getElementById('ai-chat-button');
const dailyQuoteBox = document.querySelector('.daily-quote-box');

// Emotion selection
let selectedEmotion = null;
const emotionButtons = document.querySelectorAll('.emotion-btn');

emotionButtons.forEach(btn => {
    btn.addEventListener('click', function() {
        // Remove previous selection
        emotionButtons.forEach(b => b.classList.remove('selected'));
        // Add selection to current button
        this.classList.add('selected');
        selectedEmotion = this.dataset.emotion;
    });
});

// Search functionality
const searchToggleBtn = document.getElementById('search-toggle-btn');
const searchBar = document.getElementById('search-bar');
const searchInput = document.getElementById('search-input');
let allRecords = []; // Store all records for search

searchToggleBtn.addEventListener('click', function() {
    searchBar.classList.toggle('hidden');
    if (!searchBar.classList.contains('hidden')) {
        searchInput.focus();
    }
});

searchInput.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    const recordItems = document.querySelectorAll('.record-item');
    
    recordItems.forEach(item => {
        const text = item.textContent.toLowerCase();
        if (text.includes(searchTerm)) {
            item.style.display = 'block';
            item.style.opacity = '1';
        } else {
            item.style.display = 'none';
            item.style.opacity = '0.3';
        }
    });
});

// 초기 상태: 새로운 기록 남기기 섹션 보이고 코멘트 섹션 숨기기
let isRecordMode = true; // true: 기록 모드, false: 코멘트 모드

const dailyQuotes = [
    "오늘의 작은 기록이 내일의 큰 변화를 만듭니다.",
    "당신의 감정은 소중하며, 기록될 가치가 있습니다.",
    "지나간 하루는 되돌릴 수 없지만, 기록은 영원합니다.",
    "가장 어두운 밤에 가장 밝은 별이 빛난다."
];
let currentDailyQuoteIndex = 0;

function updateDailyQuote() {
    const quoteTextElement = document.getElementById('daily-quote-text');
    if (quoteTextElement) {
        quoteTextElement.innerText = dailyQuotes[currentDailyQuoteIndex];
        currentDailyQuoteIndex = (currentDailyQuoteIndex + 1) % dailyQuotes.length;
    }
}

function updateAIComment(allTodayRecords) {
    const aiCommentText = document.getElementById('ai-comment-text');
    const emotionKeywords = document.getElementById('emotion-keywords');
    
    // null 체크 추가 - 존재하지 않는 요소에 대한 안전한 처리
    if (!aiCommentText) {
        console.warn('ai-comment-text element not found');
        return;
    }
    
    if (allTodayRecords.length > 0) {
        aiCommentText.innerText = `사랑하는 제자님, 오늘 남겨주신 소중한 기록들을 읽었어요.
        작은 순간들이 모여 제자님의 하루를 아름답게 채우고 있네요.
        오늘의 기록을 통해 [감정 키워드 예시: 기쁨, 평온]이 느껴집니다.
        꾸준히 자신을 돌아보는 모습이 참 대견해요.`;
        
        // emotionKeywords가 존재할 때만 설정
        if (emotionKeywords) {
            emotionKeywords.innerText = '오늘의 감정 키워드: #기쁨 #평온 #대견함 #일상';
        }
    } else {
        aiCommentText.innerText = '아직 오늘의 기록이 없어서 선생님의 코멘트가 준비되지 않았어요. 첫 기록을 남겨보세요!';
        
        // emotionKeywords가 존재할 때만 설정
        if (emotionKeywords) {
            emotionKeywords.innerText = '';
        }
    }
}

// 현재 모드에 따라 섹션 가시성 및 버튼 텍스트 업데이트
function updateSectionVisibility() {
    if (isRecordMode) {
        // 기록 모드: 새로운 기록 섹션 보이고, AI 코멘트 섹션 숨김
        newRecordSection.classList.remove('hidden');
        saveDiaryBtn.classList.remove('hidden');
        dailyQuoteBox.classList.remove('hidden'); // 기록 모드일 때 명언 블록 표시
        aiCommentSection.classList.add('hidden');
        aiChatButton.classList.add('hidden'); // AI 채팅 버튼 숨김
    } else {
        // 코멘트 모드: AI 코멘트 섹션 보이고, 새로운 기록 섹션 숨김
        newRecordSection.classList.add('hidden');
        saveDiaryBtn.classList.add('hidden');
        dailyQuoteBox.classList.add('hidden'); // 코멘트 모드일 때 명언 블록 숨김
        aiCommentSection.classList.remove('hidden');
        
        // 코멘트가 있는 경우에만 AI 채팅 버튼 표시
        const allRecords = Array.from(recordsListScrollable.children).filter(el => el.classList.contains('record-item') && el.id !== 'no-records-placeholder');
        if (allRecords.length > 0) { // 예시 기록이 하나라도 있으면 AI 코멘트가 있다고 간주
            aiChatButton.classList.remove('hidden'); 
        } else {
            aiChatButton.classList.add('hidden');
        }
    }
}

// 시간 포맷: 오전/오후 00:00
function formatAMPM(date) {
    let hours = date.getHours();
    let minutes = date.getMinutes();
    const isAM = hours < 12;
    let period = isAM ? '오전' : '오후';
    hours = hours % 12;
    if (hours === 0) hours = 12;
    return `${period} ${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}`;
}

// "생각 기록하기" 버튼 클릭 이벤트
saveDiaryBtn.addEventListener('click', function() {
    const content = diaryContent.value.trim();
    if (content) {
        // Show loading state
        saveDiaryBtn.disabled = true;
        saveDiaryBtn.textContent = '저장 중...';
        
        // Prepare data for API call
        const formData = new FormData();
        formData.append('userId', userId);
        formData.append('content', content);
        formData.append('appliedStamp', '참잘했어요'); // 기본 스탬프
        if (selectedEmotion) {
            formData.append('emotion', selectedEmotion);
        }
        
        // Call backend API
        fetch('/api/diaries', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('API Response:', data); // 디버깅용 로그 추가
            console.log('Response type:', typeof data);
            console.log('Response keys:', Object.keys(data));
            
            // success 필드 또는 isSuccess 필드 확인 (JSON 직렬화 문제 대응)
            const isSuccess = data.success === true || data.isSuccess === true;
            console.log('Is success:', isSuccess);
            
            if (isSuccess) {
                // Success: Add to UI
                const now = new Date();
                const time = formatAMPM(now);
                
                const newRecordItem = document.createElement('div');
                newRecordItem.className = 'record-item';
                
                // Include emotion if selected
                const emotionDisplay = selectedEmotion ? ` <span class="text-lg">${selectedEmotion}</span>` : '';
                newRecordItem.innerHTML = `<span class="text-[#8F9562] text-sm mr-2">[${time}]</span>${content}${emotionDisplay}`;
                
                recordsListScrollable.prepend(newRecordItem); // Add to top of the list

                diaryContent.value = ''; // Clear input
                
                // Reset emotion selection
                emotionButtons.forEach(b => b.classList.remove('selected'));
                selectedEmotion = null;
                
                noRecordsPlaceholder.classList.add('hidden'); // Hide placeholder if visible

                const allRecords = Array.from(recordsListScrollable.children).filter(el => el.classList.contains('record-item') && el.id !== 'no-records-placeholder');
                updateAIComment(allRecords); // AI 코멘트 업데이트

                recordsListScrollable.scrollTop = 0; // 스크롤을 최상단으로 이동
                
                // Refresh calendar data
                fetchAndRender();
                
                // ===================== NEW EMOTION STATS UPDATE =====================
                // 2025-01-XX: 일기 저장 후 감정 통계 즉시 업데이트
                updateEmotionStats(currentYear, currentMonth);
                // ===================== END NEW EMOTION STATS UPDATE =====================
                
                // Show success message
                showSuccessMessage('기록이 성공적으로 저장되었습니다!');
            } else {
                throw new Error(data.message || '저장에 실패했습니다.');
            }
        })
        .catch(error => {
            console.error('Error saving diary:', error);
            showErrorMessage('기록 저장에 실패했습니다. 다시 시도해주세요.');
        })
        .finally(() => {
            // Reset button state
            saveDiaryBtn.disabled = false;
            saveDiaryBtn.textContent = '생각 기록하기';
        });
        
    } else {
        alert('기록할 내용을 입력해주세요.');
    }
});

// "코멘트/기록 전환" 버튼 클릭 이벤트
if (toggleCommentRecordBtn) {
    toggleCommentRecordBtn.addEventListener('click', function() {
        isRecordMode = !isRecordMode; // 모드 토글
        updateSectionVisibility(); // 가시성 업데이트
        
        // 코멘트 모드로 전환 시, AI 코멘트 내용 다시 계산
        if (!isRecordMode) {
            const allRecords = Array.from(recordsListScrollable.children).filter(el => el.classList.contains('record-item') && el.id !== 'no-records-placeholder');
            updateAIComment(allRecords);
        }
    });
}

// "AI와 채팅하기" 버튼 클릭 이벤트
aiChatButton.addEventListener('click', function() {
    alert('AI 채팅 페이지로 이동합니다!');
    // 실제 구현 시 window.location.href = '/chat'; 등으로 페이지 이동
});

// 초기 로드 시 설정
document.addEventListener('DOMContentLoaded', function() {
    // 초기 상태는 기록 모드로 시작하며, 코멘트 블록은 숨겨집니다.
    isRecordMode = true; 
    updateSectionVisibility();
    updateDailyQuote(); // 초기 명언 설정
    setInterval(updateDailyQuote, 10000); // 10초마다 명언 변경 (선택 사항)

    // 초기 기록이 없는 경우 placeholder 표시
    const initialRecords = Array.from(recordsListScrollable.children).filter(el => el.classList.contains('record-item') && el.id !== 'no-records-placeholder');
    if (initialRecords.length === 0) {
        noRecordsPlaceholder.classList.remove('hidden');
    } else {
        noRecordsPlaceholder.classList.add('hidden');
    }
    updateAIComment(initialRecords); // 초기 AI 코멘트 내용 설정 (숨겨져 있어도 내용 미리 준비)
});

// ===================== CALENDAR FUNCTIONALITY =====================

// 동적 달력/일기/모달 스크립트
let currentYear = new Date().getFullYear();
let currentMonth = new Date().getMonth() + 1;
const userId = /*[[${user != null}]]*/ false ? '[[${user.userId}]]' : 1; // Thymeleaf에서 유저ID 주입, 없으면 1
let currentDiaries = [];
let selectedDate = null;

function renderCalendar(year, month, diaryData) {
    const calendarGrid = document.getElementById('calendar-grid');
    calendarGrid.innerHTML = '';
    const days = ['월','화','수','목','금','토','일'];
    days.forEach(d => {
        const div = document.createElement('div');
        div.className = 'text-center font-medium';
        div.textContent = d;
        calendarGrid.appendChild(div);
    });
    
    // 월요일이 0, 일요일이 6이 되도록 조정
    let firstDay = new Date(year, month-1, 1).getDay();
    firstDay = firstDay === 0 ? 6 : firstDay - 1; // 일요일(0)을 6으로, 월요일(1)을 0으로 변환
    
    const lastDate = new Date(year, month, 0).getDate();
    const today = new Date();
    
    // 이전 달의 마지막 날짜들 계산
    const prevMonth = month === 1 ? 12 : month - 1;
    const prevYear = month === 1 ? year - 1 : year;
    const prevMonthLastDate = new Date(prevYear, prevMonth, 0).getDate();
    
    // 이전 달의 날짜들을 흐릿하게 표시
    for(let i=0; i<firstDay; i++) {
        const prevDate = prevMonthLastDate - firstDay + i + 1;
        const cell = document.createElement('div');
        cell.className = 'date-cell';
        cell.style.opacity = '0.3';
        cell.style.background = '#f8f8f8';
        cell.style.cursor = 'default';
        cell.style.pointerEvents = 'none';
        
        const numSpan = document.createElement('span');
        numSpan.className = 'date-number';
        // 이전 달의 유효한 날짜 범위를 벗어나지 않도록 체크
        if (prevDate > 0 && prevDate <= prevMonthLastDate) {
            numSpan.textContent = prevDate;
        } else {
            numSpan.textContent = ''; // 빈 칸으로 표시
        }
        // 디버깅용 콘솔 로그 (나중에 제거)
        console.log(`prevDate: ${prevDate}, prevMonthLastDate: ${prevMonthLastDate}, firstDay: ${firstDay}, i: ${i}`);
        numSpan.style.color = '#999';
        cell.appendChild(numSpan);
        
        calendarGrid.appendChild(cell);
    }
    
    // 현재 달의 날짜들
    for(let d=1; d<=lastDate; d++) {
        const cell = document.createElement('div');
        cell.className = 'date-cell';
        // 날짜 숫자 중앙 표시
        const numSpan = document.createElement('span');
        numSpan.className = 'date-number';
        numSpan.textContent = d;
        cell.appendChild(numSpan);
        // 일기 데이터가 있으면 표시
        const diary = diaryData.find(item => new Date(item.createdAt).getDate() === d);
        if (diary) {
            cell.classList.add('has-diary');
            // appliedStamp는 포인트 계산용이므로 이미지로 사용하지 않음, 참잘했어요 스탬프만 고정 표시
            const img = document.createElement('img');
            img.dataset.src = '/images/참잘했어요.png';
            img.alt = '참잘했어요 스탬프';
            img.className = 'stamp-image-calendar loading';
            cell.appendChild(img);
            
            // Observe for lazy loading
            imageObserver.observe(img);
            
            if (diary.emotion) {
                const span = document.createElement('span');
                span.className = 'emotion-icon';
                span.textContent = diary.emotion;
                cell.appendChild(span);
            }
        }
        if (year === today.getFullYear() && month === today.getMonth()+1 && d === today.getDate()) {
            cell.classList.add('today');
        }
        const isFuture = (year > today.getFullYear()) ||
            (year === today.getFullYear() && month > today.getMonth()+1) ||
            (year === today.getFullYear() && month === today.getMonth()+1 && d > today.getDate());
        if (isFuture) {
            cell.style.pointerEvents = 'none';
            cell.style.opacity = '0.5';
            cell.style.background = '#f3f3f3';
        } else {
            cell.onclick = function() {
                selectDiaryDate(year, month, d, diaryData);
            };
        }
        calendarGrid.appendChild(cell);
    }
    
    // 다음 달의 날짜들을 흐릿하게 표시
    const totalCells = 35; // 5주 x 7일 = 35개 셀
    const filledCells = firstDay + lastDate;
    const remainingCells = totalCells - filledCells;
    
    for(let i=1; i<=remainingCells; i++) {
        const cell = document.createElement('div');
        cell.className = 'date-cell';
        cell.style.opacity = '0.3';
        cell.style.background = '#f8f8f8';
        cell.style.cursor = 'default';
        cell.style.pointerEvents = 'none';
        
        const numSpan = document.createElement('span');
        numSpan.className = 'date-number';
        numSpan.textContent = i;
        numSpan.style.color = '#999';
        cell.appendChild(numSpan);
        
        calendarGrid.appendChild(cell);
    }
}

function selectDiaryDate(year, month, day, diaryData) {
    // Remove previous selection
    const prevSelected = document.querySelector('.date-cell.selected');
    if (prevSelected) {
        prevSelected.classList.remove('selected');
    }
    
    selectedDate = new Date(year, month-1, day);
    
    // Add selection to current date
    const currentCells = document.querySelectorAll('.date-cell');
    currentCells.forEach(cell => {
        const cellDate = cell.querySelector('.date-number');
        if (cellDate && cellDate.textContent == day) {
            cell.classList.add('selected');
        }
    });
    
    // 해당 날짜의 모든 기록(시간별 등) 필터링
    const records = diaryData.filter(item => {
        const d = new Date(item.createdAt);
        return d.getFullYear() === year && d.getMonth()+1 === month && d.getDate() === day;
    });
    renderRecordsList(records, year, month, day);
}

function renderRecordsList(records, year, month, day) {
    const recordsList = document.getElementById('today-records-list-scrollable');
    recordsList.innerHTML = '';
    if (records.length === 0) {
        recordsList.innerHTML = `<p class='text-[#8F9562] text-center py-4'>이 날짜의 기록이 없습니다. 기록을 남겨보세요!</p>`;
    } else {
        records.slice().reverse().forEach(rec => {
            const time = formatAMPM(new Date(rec.createdAt));
            recordsList.innerHTML += `<div class='record-item'>
                <span class='text-[#8F9562] text-sm mr-2'>[${time}]</span>
                <span>${rec.content}</span>
                <span class='ml-2'>${rec.emotion ? '감정: '+rec.emotion : ''}</span>
                <!-- appliedStamp 이미지는 표시하지 않음 -->
            </div>`;
        });
    }
    // 오른쪽 상단에 날짜 표시(선택적)
    const header = document.querySelector('.right-section-container h2');
    if (header) header.textContent = `${year}년 ${month}월 ${day}일 기록`;

    // 오늘 날짜면 스크롤을 맨 아래로 이동
    const today = new Date();
    if (year === today.getFullYear() && month === today.getMonth()+1 && day === today.getDate()) {
        setTimeout(() => { recordsList.scrollTop = recordsList.scrollHeight; }, 0);
    }

    // 오늘 이전 날짜면 기록 입력창 숨기고 코멘트만 보이게, 일기 없는 날은 코멘트 숨김
    const isPast = (year < today.getFullYear()) ||
        (year === today.getFullYear() && month < today.getMonth()+1) ||
        (year === today.getFullYear() && month === today.getMonth()+1 && day < today.getDate());
    const newRecordSection = document.getElementById('new-record-section');
    const saveDiaryBtn = document.getElementById('save-diary-btn');
    const aiCommentSection = document.getElementById('ai-comment-section');
    if (isPast) {
        if (newRecordSection) newRecordSection.classList.add('hidden');
        if (saveDiaryBtn) saveDiaryBtn.classList.add('hidden');
        if (aiCommentSection) {
            if (records.length > 0) aiCommentSection.classList.remove('hidden');
            else aiCommentSection.classList.add('hidden');
        }
    } else {
        if (newRecordSection) newRecordSection.classList.remove('hidden');
        if (saveDiaryBtn) saveDiaryBtn.classList.remove('hidden');
        if (aiCommentSection) aiCommentSection.classList.add('hidden');
    }
}

// 달력 네비게이션 이벤트 리스너
document.getElementById('prev-month-btn').onclick = function() {
    if (--currentMonth < 1) { currentMonth = 12; currentYear--; }
    fetchAndRender();
};

document.getElementById('next-month-btn').onclick = function() {
    if (++currentMonth > 12) { currentMonth = 1; currentYear++; }
    fetchAndRender();
};

function fetchAndRender() {
    // Show loading state
    isLoading = true;
    showCalendarSkeleton();
    showRecordsSkeleton();
    showWeeklyReportsSkeleton();
    
    document.getElementById('calendar-title').textContent = `${currentYear}년 ${currentMonth}월`;
    
    fetch(`/api/diaries?userId=${userId}&year=${currentYear}&month=${currentMonth}`)
        .then(res => {
            if (!res.ok) {
                throw new Error(`HTTP error! status: ${res.status}`);
            }
            return res.json();
        })
        .then(data => {
            currentDiaries = data.data || [];
            renderCalendar(currentYear, currentMonth, currentDiaries);
            updateCalendarSummary(currentDiaries, currentYear, currentMonth);
            renderWeeklyReports(currentDiaries, currentYear, currentMonth);
            
            // ===================== NEW EMOTION STATS CALL =====================
            // 2025-01-XX: 감정 통계 API 호출 추가
            updateEmotionStats(currentYear, currentMonth);
            // ===================== END NEW EMOTION STATS CALL =====================
            
            // 기본: 오늘 날짜의 기록 표시
            const today = new Date();
            if (currentYear === today.getFullYear() && currentMonth === today.getMonth()+1) {
                selectDiaryDate(currentYear, currentMonth, today.getDate(), currentDiaries);
            } else {
                renderRecordsList([], currentYear, currentMonth, 1);
            }
            isLoading = false;
        })
        .catch(error => {
            console.error('Error fetching diary data:', error);
            showErrorMessage('데이터를 불러오는 중 오류가 발생했습니다. 다시 시도해주세요.');
            isLoading = false;
        });
}

// 주차별 감정 리포트 동적 생성
function renderWeeklyReports(diaryData, year, month) {
    const reportsList = document.getElementById('weekly-reports-list');
    reportsList.innerHTML = '';
    
    // 1. 해당 월 1일이 속한 주의 월요일 찾기 (전월 포함)
    const firstDate = new Date(year, month-1, 1);
    let firstMonday = new Date(firstDate);
    let dayOfWeek = firstDate.getDay(); // 0:일, 1:월, ... 6:토
    
    // 1일이 월요일이 아니면, 그 주의 월요일을 전월로 이동해서 찾음
    if (dayOfWeek !== 1) {
        // 1일에서 dayOfWeek-1 만큼 빼면 그 주 월요일
        let diff = (dayOfWeek === 0) ? 6 : (dayOfWeek - 1);
        firstMonday.setDate(firstDate.getDate() - diff);
    }
    
    // 2. 각 주차별로 월~일 구간 계산 (전월 포함하여 전체 주차 표시)
    const lastDateNum = new Date(year, month, 0).getDate();
    let weekStart = new Date(firstMonday);
    let weekIdx = 1;
    
    while (true) {
        let weekEnd = new Date(weekStart);
        weekEnd.setDate(weekStart.getDate() + 6);
        
        // 주차의 시작일과 종료일
        let startDay = weekStart.getDate();
        let endDay = weekEnd.getDate();
        let startMonth = weekStart.getMonth() + 1;
        let endMonth = weekEnd.getMonth() + 1;
        let startYear = weekStart.getFullYear();
        let endYear = weekEnd.getFullYear();
        
        // 주차가 해당 월에 속하는지 확인 (시작일이나 종료일 중 하나라도 해당 월에 속하면)
        if (startMonth === month || endMonth === month) {
            // 주차의 시작일과 종료일
            let startDay = weekStart.getDate();
            let endDay = weekEnd.getDate();
            let startMonth = weekStart.getMonth() + 1;
            let endMonth = weekEnd.getMonth() + 1;
            let startYear = weekStart.getFullYear();
            let endYear = weekEnd.getFullYear();
            
            // 일요일이 포함된 월을 기준으로 리포트 월 결정
            let reportMonth = endMonth; // 일요일이 있는 월
            let reportYear = endYear;
            
            // 해당 월의 몇 번째 주차인지 계산
            let reportWeekIdx = 1;
            let tempWeekStart = new Date(reportYear, reportMonth-1, 1);
            let tempDayOfWeek = tempWeekStart.getDay();
            
            // 해당 월 1일이 속한 주의 월요일 찾기
            if (tempDayOfWeek !== 1) {
                let diff = (tempDayOfWeek === 0) ? 6 : (tempDayOfWeek - 1);
                tempWeekStart.setDate(tempWeekStart.getDate() - diff);
            }
            
            // 현재 주차가 해당 월의 몇 번째 주차인지 계산
            while (tempWeekStart.getTime() < weekEnd.getTime()) {
                tempWeekStart.setDate(tempWeekStart.getDate() + 7);
                if (tempWeekStart.getTime() <= weekEnd.getTime()) {
                    reportWeekIdx++;
                }
            }
            
            // 일요일이 포함된 월이 현재 보고 있는 월과 같은 경우에만 리포트 표시
            if (reportMonth === month) {
                // 텍스트 예: 7월 1주차 리포트 (6/30 ~ 7/6)
                let weekLabel = `${reportMonth}월 ${reportWeekIdx}주차 리포트 (${startMonth}/${startDay} ~ ${endMonth}/${endDay})`;
                
                // 리포트 블록 생성
                const div = document.createElement('div');
                div.className = 'flex items-center justify-between bg-white p-4 rounded-lg border border-[#B87B5C]';
                const span = document.createElement('span');
                span.className = 'text-[#495235] font-medium';
                span.textContent = weekLabel;
                div.appendChild(span);
                const btn = document.createElement('button');
                btn.className = 'btn-nav bg-[#8F9562] hover:bg-[#495235] text-sm';
                btn.textContent = '리포트 보기';
                btn.onclick = () => alert(`${weekLabel} 페이지로 이동합니다!`);
                div.appendChild(btn);
                reportsList.appendChild(div);
            }
        }
        
        // 다음 주로 이동
        weekStart.setDate(weekStart.getDate() + 7);
        weekIdx++;
        
        // 주차 시작일이 해당 월을 완전히 벗어나면 종료
        if (weekStart.getMonth() > month-1) break;
    }
}

// 달력 요약(이번 달 일기, 연속 기록) 갱신 함수
function updateCalendarSummary(diaryData, year, month) {
    // 1. 날짜별로 일기 작성 여부 집계
    const daysWithDiary = new Set();
    diaryData.forEach(item => {
        const d = new Date(item.createdAt);
        if (d.getFullYear() === year && d.getMonth()+1 === month) {
            daysWithDiary.add(d.getDate());
        }
    });
    const diaryCount = daysWithDiary.size;

    // 2. 연속 기록 계산
    // 날짜 배열로 변환 후 정렬
    const sortedDays = Array.from(daysWithDiary).sort((a, b) => a - b);
    let maxStreak = 0, curStreak = 0, prevDay = null;
    sortedDays.forEach(day => {
        if (prevDay !== null && day === prevDay + 1) {
            curStreak++;
        } else {
            curStreak = 1;
        }
        if (curStreak > maxStreak) maxStreak = curStreak;
        prevDay = day;
    });

    // 3. DOM에 반영
    const summary = document.getElementById('calendar-summary');
    if (summary) {
        summary.textContent = `이번 달 일기: ${diaryCount}일 작성 | 연속 기록: ${maxStreak}일`;
    }
}

// ===================== NEW EMOTION STATS FUNCTION =====================
// 2025-01-XX: 월별 감정 통계 표시 기능 추가
// 주요 감정 표시 함수
function updateEmotionStats(year, month) {
    fetch(`/api/diaries/emotions?userId=${userId}&year=${year}&month=${month}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Emotion Stats Response:', data);
            
            if (data.success && data.data) {
                const emotionStats = data.data;
                const topEmotions = emotionStats.topEmotions || [];
                
                // 주요 감정 표시 업데이트
                const emotionsElement = document.getElementById('calendar-emotions');
                if (emotionsElement) {
                    if (topEmotions.length > 0) {
                        const emotionDisplay = topEmotions.map(item => 
                            `<span class="emotion-stat-item">
                                <span>${item.emotion}</span>
                                <span class="emotion-stat-count">${item.count}회</span>
                            </span>`
                        ).join('');
                        emotionsElement.innerHTML = `주요 감정: ${emotionDisplay}`;
                    } else {
                        emotionsElement.textContent = '주요 감정: 기록된 감정이 없습니다';
                    }
                }
            } else {
                console.warn('Failed to get emotion stats:', data.message);
                const emotionsElement = document.getElementById('calendar-emotions');
                if (emotionsElement) {
                    emotionsElement.textContent = '주요 감정: 데이터를 불러올 수 없습니다';
                }
            }
        })
        .catch(error => {
            console.error('Error fetching emotion stats:', error);
            const emotionsElement = document.getElementById('calendar-emotions');
            if (emotionsElement) {
                emotionsElement.textContent = '주요 감정: 오류가 발생했습니다';
            }
        });
}
// ===================== END NEW EMOTION STATS FUNCTION =====================

// 최초 렌더링
fetchAndRender(); 