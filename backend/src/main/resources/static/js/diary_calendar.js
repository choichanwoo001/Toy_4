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
let aiCommentSection, newRecordSection, recordsListScrollable, noRecordsPlaceholder;
let saveDiaryBtn, submitDiaryBtn, diaryContent, aiChatButton, dailyQuoteBox;

// DOM 요소 초기화 함수
function initializeDOMElements() {
    console.log('=== DOM 요소 초기화 시작 ===');
    
    aiCommentSection = document.getElementById('ai-comment-section');
    newRecordSection = document.getElementById('new-record-section');
    recordsListScrollable = document.getElementById('today-records-list-scrollable');
    noRecordsPlaceholder = document.getElementById('no-records-placeholder');
    saveDiaryBtn = document.getElementById('save-diary-btn');
    submitDiaryBtn = document.getElementById('submit-diary-btn');
    diaryContent = document.getElementById('diary-content');
    aiChatButton = document.getElementById('ai-chat-button');
    dailyQuoteBox = document.querySelector('.daily-quote-box');
    
    // 각 DOM 요소의 존재 여부 확인
    console.log('aiCommentSection:', aiCommentSection);
    console.log('newRecordSection:', newRecordSection);
    console.log('recordsListScrollable:', recordsListScrollable);
    console.log('noRecordsPlaceholder:', noRecordsPlaceholder);
    console.log('saveDiaryBtn:', saveDiaryBtn);
    console.log('submitDiaryBtn:', submitDiaryBtn);
    console.log('diaryContent:', diaryContent);
    console.log('aiChatButton:', aiChatButton);
    console.log('dailyQuoteBox:', dailyQuoteBox);
    
    // null 체크 및 경고
    if (!saveDiaryBtn) {
        console.error('❌ save-diary-btn을 찾을 수 없습니다!');
    } else {
        // 버튼 활성화: hidden 클래스와 disabled 속성 제거
        saveDiaryBtn.classList.remove('hidden');
        saveDiaryBtn.disabled = false;
        console.log('✅ save-diary-btn 활성화됨');
    }
    if (!diaryContent) {
        console.error('❌ diary-content를 찾을 수 없습니다!');
    }
    if (!recordsListScrollable) {
        console.error('❌ today-records-list-scrollable을 찾을 수 없습니다!');
    }
    if (!noRecordsPlaceholder) {
        console.error('❌ no-records-placeholder를 찾을 수 없습니다!');
    }
    
    console.log('=== DOM 요소 초기화 완료 ===');
}

// Emotion selection
let selectedEmotion = null;
let emotionButtons = [];

function setupEmotionButtons() {
    emotionButtons = document.querySelectorAll('.emotion-btn');
    
    emotionButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            // 과거 날짜 체크
            const today = new Date();
            const isPast = selectedDate && (
                selectedDate.getFullYear() < today.getFullYear() ||
                (selectedDate.getFullYear() === today.getFullYear() && selectedDate.getMonth() < today.getMonth()) ||
                (selectedDate.getFullYear() === today.getFullYear() && selectedDate.getMonth() === today.getMonth() && selectedDate.getDate() < today.getDate())
            );
            
            if (isPast) {
                showErrorMessage('과거 날짜에는 감정을 선택할 수 없습니다.');
                return;
            }
            
            // Remove previous selection
            emotionButtons.forEach(b => b.classList.remove('selected'));
            // Add selection to current button
            this.classList.add('selected');
            selectedEmotion = this.dataset.emotion;
        });
    });
}

// Search functionality
let searchToggleBtn, searchBar, searchInput;
let allRecords = []; // Store all records for search

function setupSearchFunctionality() {
    searchToggleBtn = document.getElementById('search-toggle-btn');
    searchBar = document.getElementById('search-bar');
    searchInput = document.getElementById('search-input');
    
    if (searchToggleBtn) {
        searchToggleBtn.addEventListener('click', function() {
            searchBar.classList.toggle('hidden');
            if (!searchBar.classList.contains('hidden')) {
                searchInput.focus();
            }
        });
    }
    
    if (searchInput) {
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
    }
}

// 초기 상태: 새로운 기록 남기기 섹션만 보이도록 설정
// 코멘트 보기 기능은 완전히 제거됨

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
        // 기록에서 감정 추출
        const emotions = allTodayRecords
            .map(record => record.emotion)
            .filter(emotion => emotion && emotion.trim() !== '')
            .slice(0, 3); // 최대 3개까지만 표시
        
        // 감정 키워드 생성
        const emotionKeywordsList = emotions.length > 0 
            ? emotions.map(emotion => `#${getEmotionKeyword(emotion)}`).join(' ')
            : '#기쁨 #평온 #대견함';
        
        // 과거 날짜인지 확인
        const today = new Date();
        const isPast = selectedDate && (
            selectedDate.getFullYear() < today.getFullYear() ||
            (selectedDate.getFullYear() === today.getFullYear() && selectedDate.getMonth() < today.getMonth()) ||
            (selectedDate.getFullYear() === today.getFullYear() && selectedDate.getMonth() === today.getMonth() && selectedDate.getDate() < today.getDate())
        );
        
        if (isPast) {
            // 과거 날짜에 대한 따뜻한 코멘트
            const dateStr = `${selectedDate.getMonth() + 1}월 ${selectedDate.getDate()}일`;
            aiCommentText.innerText = `사랑하는 제자님, ${dateStr}의 소중한 기록들을 다시 읽어보니 그때의 마음이 생생하게 느껴져요.
            제자님이 그날 느끼신 감정들과 생각들이 지금도 선생님 마음에 따뜻하게 남아있어요.
            그때의 기록들이 지금의 제자님을 더욱 풍요롭게 만들어주고 있네요.
            꾸준히 자신을 돌아보는 모습이 참 대견해요.`;
        } else {
            // 오늘 날짜에 대한 코멘트
            aiCommentText.innerText = `사랑하는 제자님, 오늘 남겨주신 소중한 기록들을 읽었어요.
            작은 순간들이 모여 제자님의 하루를 아름답게 채우고 있네요.
            오늘의 기록을 통해 [감정 키워드 예시: 기쁨, 평온]이 느껴집니다.
            꾸준히 자신을 돌아보는 모습이 참 대견해요.`;
        }
        
        // emotionKeywords가 존재할 때만 설정
        if (emotionKeywords) {
            emotionKeywords.innerText = `오늘의 감정 키워드: ${emotionKeywordsList}`;
        }
    } else {
        aiCommentText.innerText = '아직 오늘의 기록이 없어서 선생님의 코멘트가 준비되지 않았어요. 첫 기록을 남겨보세요!';
        
        // emotionKeywords가 존재할 때만 설정
        if (emotionKeywords) {
            emotionKeywords.innerText = '';
        }
    }
}

// 감정 이모지를 키워드로 변환하는 함수
function getEmotionKeyword(emotion) {
    const emotionMap = {
        '😊': '기쁨',
        '😢': '슬픔',
        '😡': '화남',
        '😌': '평온',
        '🤔': '고민',
        '😍': '사랑',
        '😴': '피곤',
        '😎': '자신감'
    };
    return emotionMap[emotion] || '감정';
}

// 섹션 가시성 관리 - 제출 여부에 따라 바뀌도록 수정
function updateSectionVisibility(hasSubmitted = false) {
    // 기록 목록과 명언은 항상 보이도록 유지
    recordsListScrollable.classList.remove('hidden');
    dailyQuoteBox.classList.remove('hidden');
    
    if (hasSubmitted) {
        // 제출했을 때: AI 코멘트 섹션 표시, 새로운 기록 섹션 숨김
        aiCommentSection.classList.remove('hidden');
        aiChatButton.classList.remove('hidden');
        newRecordSection.classList.add('hidden');
        saveDiaryBtn.classList.add('hidden');
    } else {
        // 제출하지 않았을 때: 새로운 기록 섹션 표시, AI 코멘트 섹션 숨김
        newRecordSection.classList.remove('hidden');
        saveDiaryBtn.classList.remove('hidden');
        aiCommentSection.classList.add('hidden');
        aiChatButton.classList.add('hidden');
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
function setupEventListeners() {
    console.log('=== 이벤트 리스너 설정 시작 ===');
    console.log('saveDiaryBtn:', saveDiaryBtn);
    console.log('submitDiaryBtn:', submitDiaryBtn);
    console.log('diaryContent:', diaryContent);
    
    if (saveDiaryBtn) {
        console.log('✅ saveDiaryBtn 이벤트 리스너 설정');
        saveDiaryBtn.addEventListener('click', function() {
            console.log('🔘 "생각 기록하기" 버튼 클릭됨');
            console.log('diaryContent.value:', diaryContent ? diaryContent.value : 'diaryContent is null');
            
    // 과거 날짜 체크 - 추가 보안
    const today = new Date();
    const isPast = selectedDate && (
        selectedDate.getFullYear() < today.getFullYear() ||
        (selectedDate.getFullYear() === today.getFullYear() && selectedDate.getMonth() < today.getMonth()) ||
        (selectedDate.getFullYear() === today.getFullYear() && selectedDate.getMonth() === today.getMonth() && selectedDate.getDate() < today.getDate())
    );
    
    if (isPast) {
        showErrorMessage('과거 날짜에는 기록할 수 없습니다.');
        return;
    }
    
    const content = diaryContent ? diaryContent.value.trim() : '';
    console.log('입력된 내용:', content);
    
    if (content) {
        console.log('✅ 내용이 있음, API 호출 시작');
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
        
        console.log('API 호출 데이터:', {
            userId: userId,
            content: content,
            emotion: selectedEmotion
        });
        
        // Call backend API
        fetch('/api/diaries', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            console.log('API 응답 상태:', response.status);
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
                console.log('✅ API 성공, UI 업데이트 시작');
                // Success: Add to UI
                const now = new Date();
                const time = formatAMPM(now);
                
                const newRecordItem = document.createElement('div');
                newRecordItem.className = 'record-item';
                
                // Include emotion if selected
                const emotionDisplay = selectedEmotion ? ` <span class="text-lg">${selectedEmotion}</span>` : '';
                newRecordItem.innerHTML = `<span class="text-[#8F9562] text-sm mr-2">[${time}]</span>${content}${emotionDisplay}`;
                
                if (recordsListScrollable) {
                    recordsListScrollable.prepend(newRecordItem); // Add to top of the list
                    console.log('✅ 기록 목록에 새 항목 추가됨');
                } else {
                    console.error('❌ recordsListScrollable이 null입니다!');
                }

                if (diaryContent) {
                    diaryContent.value = ''; // Clear input
                    console.log('✅ 입력 필드 초기화됨');
                } else {
                    console.error('❌ diaryContent가 null입니다!');
                }
                
                // Reset emotion selection
                emotionButtons.forEach(b => b.classList.remove('selected'));
                selectedEmotion = null;
                
                if (noRecordsPlaceholder) {
                    noRecordsPlaceholder.classList.add('hidden'); // Hide placeholder if visible
                    console.log('✅ placeholder 숨김');
                } else {
                    console.error('❌ noRecordsPlaceholder가 null입니다!');
                }

                const allRecords = Array.from(recordsListScrollable ? recordsListScrollable.children : []).filter(el => el.classList.contains('record-item') && el.id !== 'no-records-placeholder');
                updateAIComment(allRecords); // AI 코멘트 업데이트

                // AI 일기 분석 호출 제거 - 단순 기록만 저장
                // analyzeDiaryWithAI(content); // 이 줄 제거

                if (recordsListScrollable) {
                    recordsListScrollable.scrollTop = 0; // 스크롤을 최상단으로 이동
                }
                
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
            if (saveDiaryBtn) {
                saveDiaryBtn.disabled = false;
                saveDiaryBtn.textContent = '생각 기록하기';
                console.log('✅ 버튼 상태 초기화됨');
            }
        });
        
    } else {
        console.log('❌ 내용이 비어있음');
        alert('기록할 내용을 입력해주세요.');
    }
    });
    } else {
        console.error('❌ saveDiaryBtn이 null입니다! 이벤트 리스너를 설정할 수 없습니다.');
    }

    // "일기 제출" 버튼 클릭 이벤트 (오늘의 모든 기록을 합쳐서 AI에게 전달)
    if (submitDiaryBtn) {
        console.log('✅ submitDiaryBtn 이벤트 리스너 설정');
        submitDiaryBtn.addEventListener('click', async function() {
            console.log('🔘 "일기 제출" 버튼 클릭됨');
    // Show loading state
    submitDiaryBtn.disabled = true;
    submitDiaryBtn.textContent = '제출 중...';
    
    try {
        // 오늘의 모든 기록 가져오기
        const response = await fetch(`/api/diaries/today?userId=${userId}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('Today diaries response:', data);
        
        if (data.success && data.data) {
            const todayDiaries = data.data;
            
            if (todayDiaries.length === 0) {
                showErrorMessage('오늘 작성된 기록이 없습니다. 먼저 기록을 남겨주세요.');
                return;
            }
            
            // 모든 기록을 하나로 합치기
            const combinedContent = todayDiaries
                .map(diary => diary.content)
                .join('\n\n');
            
            console.log('Combined content for AI:', combinedContent);
            
            // AI 일기 분석 호출 (합쳐진 내용으로)
            await analyzeDiaryWithAI(combinedContent);
            
            // 제출 후 섹션 변경
            updateSectionVisibility(true);
            
            showSuccessMessage('오늘의 모든 기록을 AI에게 제출했습니다! AI 코멘트가 생성되었습니다.');
        } else {
            throw new Error(data.message || '오늘의 기록을 가져오는데 실패했습니다.');
        }
        
    } catch (error) {
        console.error('Error submitting diary:', error);
        showErrorMessage('일기 제출에 실패했습니다. 다시 시도해주세요.');
    } finally {
        // Reset button state
        submitDiaryBtn.disabled = false;
        submitDiaryBtn.textContent = '일기 제출';
    }
    });
    } else {
        console.error('❌ submitDiaryBtn이 null입니다! 이벤트 리스너를 설정할 수 없습니다.');
    }
    
    console.log('=== 이벤트 리스너 설정 완료 ===');
}

// ===================== AI DIARY ANALYSIS =====================
// 2025-01-XX: AI 일기 분석 및 코멘트 생성 기능 추가
async function analyzeDiaryWithAI(content) {
    try {
        console.log('=== AI Diary Analysis Started ===');
        console.log('Content:', content);
        
        // AI 분석 요청 데이터 준비
        const formData = new FormData();
        formData.append('userId', userId);
        formData.append('content', content);
        
        // AI 분석 API 호출
        const response = await fetch('/api/diaries/analyze', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log('AI Analysis Response:', data);
        
        const isSuccess = data.success === true || data.isSuccess === true;
        
        if (isSuccess && data.data) {
            const aiResult = data.data;
            
            // AI 코멘트 섹션 표시
            const aiCommentSection = document.getElementById('ai-comment-section');
            const aiCommentText = document.getElementById('ai-comment-text');
            const emotionKeywords = document.getElementById('emotion-keywords');
            
            if (aiCommentSection && aiCommentText && emotionKeywords) {
                // AI 코멘트 업데이트
                if (aiResult.comment) {
                    aiCommentText.textContent = aiResult.comment;
                }
                
                // 감정 키워드 업데이트
                if (aiResult.emotion_keywords && aiResult.emotion_keywords.length > 0) {
                    const keywords = aiResult.emotion_keywords.map(keyword => `#${keyword}`).join(' ');
                    emotionKeywords.textContent = `오늘의 감정 키워드: ${keywords}`;
                }
                
                // 인용문이 있는 경우 추가
                if (aiResult.quote) {
                    const quoteElement = document.createElement('p');
                    quoteElement.className = 'text-[#8F9562] text-sm italic mt-2';
                    quoteElement.textContent = `"${aiResult.quote}"`;
                    aiCommentText.appendChild(quoteElement);
                }
                
                // AI 코멘트 섹션 표시
                aiCommentSection.classList.remove('hidden');
                
                console.log('AI Comment updated successfully');
            }
            
            // 조언이 있는 경우 표시
            if (aiResult.advice) {
                console.log('AI Advice:', aiResult.advice);
                // 필요시 조언을 UI에 표시하는 로직 추가
            }
            
            showSuccessMessage('AI가 당신의 일기를 분석했습니다!');
        } else {
            console.warn('AI analysis completed but no data returned');
        }
        
    } catch (error) {
        console.error('Error in AI diary analysis:', error);
        // AI 분석 실패는 사용자에게 알리지 않음 (선택적 기능이므로)
    }
}
// ===================== END AI DIARY ANALYSIS =====================

// 코멘트/기록 전환 버튼 관련 코드 제거됨
// 이제 항상 기록 모드만 유지됨

// "AI와 채팅하기" 버튼 클릭 이벤트
function setupAIChatButton() {
    if (aiChatButton) {
        aiChatButton.addEventListener('click', function() {
            // 현재 선택된 날짜의 일기 정보를 채팅 페이지로 전달
            const selectedDateStr = selectedDate ? 
                `${selectedDate.getFullYear()}-${String(selectedDate.getMonth() + 1).padStart(2, '0')}-${String(selectedDate.getDate()).padStart(2, '0')}` : 
                new Date().toISOString().split('T')[0];
            
            // 현재 사용자 ID와 선택된 날짜를 쿼리 파라미터로 전달
            const chatUrl = `/chat?userId=${userId}&diaryDate=${selectedDateStr}`;
            window.location.href = chatUrl;
        });
    }
}

// 초기 로드 시 설정
document.addEventListener('DOMContentLoaded', async function() {
    // DOM 요소 초기화
    initializeDOMElements();
    
    // 이벤트 리스너 설정
    setupEventListeners();
    setupSearchFunctionality();
    setupAIChatButton();
    setupEmotionButtons();
    setupCalendarNavigation();
    
    // 사용자 ID 설정 및 달력 데이터 로드
    await initUserId();
    fetchAndRender(); // 달력 데이터 로드 및 렌더링

    // 오늘의 제출 상태 확인
    await checkTodaySubmissionStatus();
    
    // 초기 명언 설정
    updateDailyQuote();
    setInterval(updateDailyQuote, 10000); // 10초마다 명언 변경 (선택 사항)
    
    // 초기 기록이 없는 경우 placeholder 표시
    const initialRecords = Array.from(recordsListScrollable.children).filter(el => el.classList.contains('record-item') && el.id !== 'no-records-placeholder');
    if (initialRecords.length === 0) {
        if (noRecordsPlaceholder) {
            noRecordsPlaceholder.classList.remove('hidden');
        } else {
            console.warn('⚠️ noRecordsPlaceholder가 null입니다. placeholder를 표시할 수 없습니다.');
        }
    } else {
        if (noRecordsPlaceholder) {
            noRecordsPlaceholder.classList.add('hidden');
        } else {
            console.warn('⚠️ noRecordsPlaceholder가 null입니다. placeholder를 숨길 수 없습니다.');
        }
    }
    updateAIComment(initialRecords); // 초기 AI 코멘트 내용 설정
});

// 오늘의 제출 상태 확인 함수
async function checkTodaySubmissionStatus() {
    if (!userId) {
        updateSectionVisibility(false); // 로그인하지 않은 경우 기본 상태
        return;
    }
    
    try {
        const response = await fetch(`/api/diaries/today?userId=${userId}`);
        if (response.ok) {
            const data = await response.json();
            if (data.success && data.data) {
                const todayDiaries = data.data;
                // 오늘 기록이 있고 제출된 상태인지 확인 (백엔드에서 제출 상태 필드 확인 필요)
                const hasSubmitted = todayDiaries.some(diary => diary.submitted === true);
                updateSectionVisibility(hasSubmitted);
            } else {
                updateSectionVisibility(false);
            }
        } else {
            updateSectionVisibility(false);
        }
    } catch (error) {
        console.error('Error checking submission status:', error);
        updateSectionVisibility(false);
    }
}

// ===================== CALENDAR FUNCTIONALITY =====================

// 유틸 함수: 월요일 기준 주차 계산
function getMonday(date) {
    const d = new Date(date);
    const day = d.getDay();
    const diff = d.getDate() - day + (day === 0 ? -6 : 1);
    return new Date(d.setDate(diff));
}

// 동적 달력/일기/모달 스크립트
let currentYear = new Date().getFullYear();
let currentMonth = new Date().getMonth() + 1;
let userId = null; // 로그인하지 않은 상태를 나타내는 기본값
let currentDiaries = [];
let selectedDate = null;

// 사용자 ID 초기화 함수
async function initUserId() {
    console.log('=== initUserId 시작 ===');
    try {
        // 현재 로그인한 사용자 정보 가져오기
        console.log('API 호출: /api/current-user');
        const userResponse = await fetch('/api/current-user');
        console.log('API 응답 상태:', userResponse.status);
        
        if (userResponse.ok) {
            const userData = await userResponse.json();
            console.log('API 응답 데이터:', userData);
            
            if (userData && userData.userId) {
                userId = userData.userId;
                console.log('✅ 현재 로그인한 사용자 ID:', userId);
            } else {
                console.log('❌ 로그인되지 않음 또는 userId 없음');
                // 로그인되지 않은 경우, URL 파라미터에서 userId 확인
                const urlParams = new URLSearchParams(window.location.search);
                const urlUserId = urlParams.get('userId');
                if (urlUserId) {
                    userId = parseInt(urlUserId);
                    console.log('URL 파라미터에서 사용자 ID:', userId);
                } else {
                    console.log('기본 userId 사용:', userId);
                }
            }
        } else {
            console.log('❌ API 응답 실패:', userResponse.status);
        }
    } catch (error) {
        console.error('❌ 사용자 정보 확인 실패:', error);
        // 오류 발생 시 URL 파라미터에서 userId 확인
        const urlParams = new URLSearchParams(window.location.search);
        const urlUserId = urlParams.get('userId');
        if (urlUserId) {
            userId = parseInt(urlUserId);
        }
    }
    console.log('=== initUserId 완료, 최종 userId:', userId, '===');
}

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
            img.src = '/image/default_stamp.png';
            img.alt = '참잘했어요 스탬프';
            img.className = 'stamp-image-calendar';
            cell.appendChild(img);
            
            // 스탬프 이미지는 즉시 로드
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
    
    const today = new Date();
    const isPast = (year < today.getFullYear()) ||
        (year === today.getFullYear() && month < today.getMonth()+1) ||
        (year === today.getFullYear() && month === today.getMonth()+1 && day < today.getDate());
    
    if (records.length === 0) {
        if (!userId) {
            recordsList.innerHTML = `<p class='text-[#8F9562] text-center py-4'>로그인 후 기록을 남겨보세요!<br>소중한 순간들을 기록할 수 있어요.</p>`;
        } else if (isPast) {
            recordsList.innerHTML = `<p class='text-[#8F9562] text-center py-4'>${month}월 ${day}일에는 기록이 없었어요.<br>그날의 소중한 순간들을 기록해보세요!</p>`;
        } else {
            recordsList.innerHTML = `<p class='text-[#8F9562] text-center py-4'>이 날짜의 기록이 없습니다. 기록을 남겨보세요!</p>`;
        }
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
    if (year === today.getFullYear() && month === today.getMonth()+1 && day === today.getDate()) {
        setTimeout(() => { recordsList.scrollTop = recordsList.scrollHeight; }, 0);
    }

    // 오늘 이전 날짜면 기록 입력창 완전히 비활성화
    const newRecordSection = document.getElementById('new-record-section');
    const saveDiaryBtn = document.getElementById('save-diary-btn');
    const aiCommentSection = document.getElementById('ai-comment-section');
    
    if (isPast) {
        // 과거 날짜: 기록 입력 완전 비활성화
        if (newRecordSection) {
            newRecordSection.classList.add('hidden');
            // 추가로 입력 필드도 비활성화
            const diaryContent = document.getElementById('diary-content');
            if (diaryContent) {
                diaryContent.disabled = true;
                diaryContent.placeholder = '과거 날짜에는 기록할 수 없습니다.';
            }
            // 감정 버튼들도 비활성화
            const emotionButtons = document.querySelectorAll('.emotion-btn');
            emotionButtons.forEach(btn => {
                btn.disabled = true;
                btn.style.opacity = '0.5';
                btn.style.cursor = 'not-allowed';
            });
        }
        if (saveDiaryBtn) {
            saveDiaryBtn.classList.add('hidden');
            saveDiaryBtn.disabled = true;
        }
        
        // 과거 날짜에서 기록이 있는 경우에만 AI 코멘트 표시
        if (aiCommentSection) {
            if (records.length > 0) {
                aiCommentSection.classList.remove('hidden');
                // AI 코멘트 내용 업데이트
                updateAIComment(records);
                // AI와 채팅하기 버튼도 활성화
                if (aiChatButton) {
                    aiChatButton.classList.remove('hidden');
                }
            } else {
                aiCommentSection.classList.add('hidden');
                // AI와 채팅하기 버튼도 숨김
                if (aiChatButton) {
                    aiChatButton.classList.add('hidden');
                }
            }
        }
    } else {
        // 오늘 또는 미래 날짜: 제출 상태에 따라 섹션 결정
        if (!userId) {
            // 로그인하지 않은 경우 기록 입력 비활성화
            if (newRecordSection) {
                newRecordSection.classList.add('hidden');
            }
            if (saveDiaryBtn) {
                saveDiaryBtn.classList.add('hidden');
                saveDiaryBtn.disabled = true;
            }
            if (aiCommentSection) aiCommentSection.classList.add('hidden');
        } else {
            // 로그인한 경우 제출 상태 확인 후 적절한 섹션 표시
            checkTodaySubmissionStatus();
        }
    }
}

// 달력 네비게이션 이벤트 리스너
function setupCalendarNavigation() {
    const prevMonthBtn = document.getElementById('prev-month-btn');
    const nextMonthBtn = document.getElementById('next-month-btn');
    
    if (prevMonthBtn) {
        prevMonthBtn.onclick = function() {
            if (--currentMonth < 1) { currentMonth = 12; currentYear--; }
            fetchAndRender();
        };
    }
    
    if (nextMonthBtn) {
        nextMonthBtn.onclick = function() {
            if (++currentMonth > 12) { currentMonth = 1; currentYear++; }
            fetchAndRender();
        };
    }
}

function fetchAndRender() {
    // Show loading state
    isLoading = true;
    showCalendarSkeleton();
    showRecordsSkeleton();
    showWeeklyReportsSkeleton();
    
    document.getElementById('calendar-title').textContent = `${currentYear}년 ${currentMonth}월`;
    
    // 로그인하지 않은 경우 빈 달력만 표시
    console.log('=== fetchAndRender - 현재 userId:', userId, '===');
    if (!userId) {
        console.log('❌ 로그인하지 않은 상태 - 빈 달력 표시');
        currentDiaries = [];
        renderCalendar(currentYear, currentMonth, currentDiaries);
        updateCalendarSummary(currentDiaries, currentYear, currentMonth);
        renderWeeklyReports(currentDiaries, currentYear, currentMonth);
        
        // 오늘 날짜의 빈 기록 표시
        const today = new Date();
        if (currentYear === today.getFullYear() && currentMonth === today.getMonth()+1) {
            selectDiaryDate(currentYear, currentMonth, today.getDate(), currentDiaries);
        } else {
            renderRecordsList([], currentYear, currentMonth, 1);
        }
        isLoading = false;
        return;
    }
    
    console.log('✅ 로그인한 사용자 - API 호출:', `/api/diaries?userId=${userId}&year=${currentYear}&month=${currentMonth}`);
    
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
                btn.onclick = () => {
                    // 주차 정보를 계산하여 리포트 페이지로 이동
                    // 현재 날짜를 기준으로 한 주차 오프셋 계산
                    const today = new Date();
                    const currentWeekStart = getMonday(today);
                    const targetWeekStart = new Date(weekStart);
                    
                    // 두 날짜 간의 주차 차이 계산
                    const timeDiff = currentWeekStart.getTime() - targetWeekStart.getTime();
                    const weekDiff = Math.round(timeDiff / (1000 * 60 * 60 * 24 * 7));
                    
                    const reportUrl = `/report?userId=${userId}&weekOffset=${weekDiff}&year=${year}&month=${month}`;
                    window.location.href = reportUrl;
                };
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