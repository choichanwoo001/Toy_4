// --- Main Page Scripts ---
const mainQuotes = [
    "당신의 하루는 기록될 가치가 있습니다.",
    "작은 기록들이 모여 당신을 더 잘 알게 합니다.",
    "오늘의 감정은 내일의 지혜가 됩니다.",
    "선생님은 언제나 당신의 이야기를 응원합니다."
];
let currentQuoteIndex = 0;
const mainQuoteDisplay = document.getElementById('main-quote-display');
const mainAuthButtonsDiv = document.getElementById('main-auth-buttons');
const mainServiceFeaturesSection = document.getElementById('main-service-features-section');
const mainLoginFormSection = document.getElementById('login-form-section');
const mainRegistrationFormSection = document.getElementById('registration-form-section');

// Simulate login state (in a real app, check cookie/session)
const isLoggedIn = false; // true로 바꾸면 '일기 쓰러 가기'만 보임

function showForm(formType) {
    if (mainServiceFeaturesSection) {
        mainServiceFeaturesSection.classList.add('hidden'); // Hide features
    }
    
    if (formType === 'login') {
        if (mainLoginFormSection) mainLoginFormSection.classList.remove('hidden');
        if (mainRegistrationFormSection) mainRegistrationFormSection.classList.add('hidden');
    } else if (formType === 'register') {
        if (mainRegistrationFormSection) mainRegistrationFormSection.classList.remove('hidden');
        if (mainLoginFormSection) mainLoginFormSection.classList.add('hidden');
    }
    
    // Scroll to the form
    const formSection = document.getElementById(`${formType}-form-section`);
    if (formSection) {
        formSection.scrollIntoView({
            behavior: 'smooth',
            block: 'center'
        });
    }
}

function hideForm(formType) {
    if (formType === 'login') {
        if (mainLoginFormSection) mainLoginFormSection.classList.add('hidden');
    } else if (formType === 'register') {
        if (mainRegistrationFormSection) mainRegistrationFormSection.classList.add('hidden');
    }
    if (!isLoggedIn) { // Only show features if not logged in
        if (mainServiceFeaturesSection) mainServiceFeaturesSection.classList.remove('hidden');
    }
    
    // Scroll back to the main page top if forms are hidden
    const mainPageSection = document.getElementById('main-page-section');
    if (mainPageSection) {
        mainPageSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

function renderAuthButtons() {
    if (!mainAuthButtonsDiv) return; // Safety check
    
    mainAuthButtonsDiv.innerHTML = ''; // Clear existing buttons
    if (isLoggedIn) {
        const diaryButton = document.createElement('button');
        diaryButton.id = 'go-to-diary-btn';
        diaryButton.className = 'btn-main';
        diaryButton.innerText = '일기 쓰러 가기';
        diaryButton.addEventListener('click', () => alert('일기 작성 페이지로 이동합니다!'));
        mainAuthButtonsDiv.appendChild(diaryButton);
        if (mainServiceFeaturesSection) {
            mainServiceFeaturesSection.classList.add('hidden'); // Hide features if logged in
        }
    } else {
        const signUpButton = document.createElement('button');
        signUpButton.id = 'sign-up-btn';
        signUpButton.className = 'btn-main'; // 회원가입을 메인 버튼으로
        signUpButton.innerText = '회원가입';
        signUpButton.addEventListener('click', () => showForm('register'));
        mainAuthButtonsDiv.appendChild(signUpButton);

        const loginButton = document.createElement('button'); // 로그인 버튼 추가
        loginButton.id = 'login-btn';
        loginButton.className = 'btn-secondary';
        loginButton.innerText = '로그인';
        loginButton.addEventListener('click', () => showForm('login'));
        mainAuthButtonsDiv.appendChild(loginButton);

        if (mainServiceFeaturesSection) {
            mainServiceFeaturesSection.classList.remove('hidden'); // Show features if not logged in
        }
    }
}

function displayNextQuote() {
    if (!mainQuoteDisplay) return; // Safety check
    
    mainQuoteDisplay.classList.remove('fade-in');
    setTimeout(() => {
        currentQuoteIndex = (currentQuoteIndex + 1) % mainQuotes.length;
        mainQuoteDisplay.innerText = mainQuotes[currentQuoteIndex];
        mainQuoteDisplay.classList.add('fade-in');
    }, 500); // 짧게 사라진 후 다음 명언 표시
}

// Initial display for Main Page
function initializeMainPage() {
    renderAuthButtons(); // Render buttons based on login state
    
    if (mainQuoteDisplay) {
        mainQuoteDisplay.innerText = mainQuotes[0];
        setTimeout(() => {
            mainQuoteDisplay.classList.add('fade-in');
        }, 100); // 페이지 로드 후 바로 페이드인
    }

    // Cycle through quotes every few seconds
    setInterval(displayNextQuote, 5000); // 5초마다 명언 변경
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeMainPage();
});

// Form submission handlers
function handleLoginSubmit(event) {
    event.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    
    // Here you would typically send the data to your backend
    console.log('Login attempt:', { email, password });
    alert('로그인 기능은 백엔드 연동 후 사용 가능합니다.');
}

function handleRegistrationSubmit(event) {
    event.preventDefault();
    const name = document.getElementById('reg-name').value;
    const email = document.getElementById('reg-email').value;
    const password = document.getElementById('reg-password').value;
    const confirmPassword = document.getElementById('reg-confirm-password').value;
    const phone = document.getElementById('reg-phone').value;
    const termsAgreed = document.getElementById('terms-agree').checked;
    
    // Basic validation
    if (!name || !email || !password || !confirmPassword || !phone) {
        alert('모든 필드를 입력해주세요.');
        return;
    }
    
    if (password !== confirmPassword) {
        alert('비밀번호가 일치하지 않습니다.');
        return;
    }
    
    if (!termsAgreed) {
        alert('약관에 동의해주세요.');
        return;
    }
    
    // Here you would typically send the data to your backend
    console.log('Registration attempt:', { name, email, password, phone });
    alert('회원가입 기능은 백엔드 연동 후 사용 가능합니다.');
}

// Add form event listeners when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Login form submission
    const loginForm = document.querySelector('#login-form-section form');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLoginSubmit);
    }
    
    // Registration form submission
    const registrationForm = document.querySelector('#registration-form-section form');
    if (registrationForm) {
        registrationForm.addEventListener('submit', handleRegistrationSubmit);
    }
    
    // Kakao login button
    const kakaoLoginBtn = document.querySelector('#login-form-section .btn-kakao');
    if (kakaoLoginBtn) {
        kakaoLoginBtn.addEventListener('click', function() {
            alert('카카오 로그인 기능은 카카오 API 연동 후 사용 가능합니다.');
        });
    }
    
    // Kakao registration button
    const kakaoRegBtn = document.querySelector('#registration-form-section .btn-kakao');
    if (kakaoRegBtn) {
        kakaoRegBtn.addEventListener('click', function() {
            alert('카카오 회원가입 기능은 카카오 API 연동 후 사용 가능합니다.');
        });
    }
});

// Utility functions for other pages (if needed)
function showAlert(message) {
    alert(message);
}

function redirectToPage(url) {
    window.location.href = url;
}

// Export functions for use in other scripts (if needed)
window.MainPageUtils = {
    showForm,
    hideForm,
    renderAuthButtons,
    displayNextQuote,
    initializeMainPage,
    showAlert,
    redirectToPage
}; 