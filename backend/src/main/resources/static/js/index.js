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

// 로그인 상태 변수
let isLoggedIn = false;

/**
 * 서버에서 현재 로그인 상태를 확인하는 함수
 * 세션 정보를 통해 사용자가 로그인되어 있는지 확인
 */
async function checkLoginStatus() {
    try {
        const response = await fetch('/api/check-login-status', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        });
        
        if (response.ok) {
            const loginStatus = await response.text();
            isLoggedIn = loginStatus === 'true';
            renderAuthButtons();
        }
    } catch (error) {
        console.error('로그인 상태 확인 중 오류:', error);
    }
}

/**
 * 사용자 로그아웃 처리 함수
 * 서버에 로그아웃 요청을 보내고 로컬 상태를 업데이트
 */
async function logout() {
    try {
        const response = await fetch('/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        });
        
        if (response.ok) {
            isLoggedIn = false;
            renderAuthButtons();
            // 페이지 새로고침
            window.location.reload();
        }
    } catch (error) {
        console.error('로그아웃 중 오류:', error);
    }
}

/**
 * 로그인/회원가입 폼을 표시하는 함수
 * @param {string} formType - 'login' 또는 'register'
 */
function showForm(formType) {
    if (formType === 'login') {
        mainLoginFormSection.classList.remove('hidden');
        mainRegistrationFormSection.classList.add('hidden');
        // 로그인 폼 초기화
        resetLoginForm();
    } else if (formType === 'register') {
        mainRegistrationFormSection.classList.remove('hidden');
        mainLoginFormSection.classList.add('hidden');
        // 회원가입 폼 초기화
        resetRegistrationForm();
    }
}

/**
 * 로그인/회원가입 폼을 숨기는 함수
 * @param {string} formType - 'login' 또는 'register'
 */
function hideForm(formType) {
    if (formType === 'login') {
        mainLoginFormSection.classList.add('hidden');
    } else if (formType === 'register') {
        mainRegistrationFormSection.classList.add('hidden');
    }
}

/**
 * 로그인 상태에 따라 인증 버튼을 렌더링하는 함수
 * 로그인 상태면 '일기 쓰러 가기'와 '로그아웃' 버튼 표시
 * 비로그인 상태면 '로그인'과 '회원가입' 버튼 표시
 */
function renderAuthButtons() {
    if (isLoggedIn) {
        mainAuthButtonsDiv.innerHTML = `
            <button class="btn-main" onclick="window.location.href='/diary'">일기 쓰러 가기</button>
            <button class="btn-kakao" onclick="logout()">로그아웃</button>
        `;
    } else {
        mainAuthButtonsDiv.innerHTML = `
            <button class="btn-main" onclick="showForm('login')">로그인</button>
            <button class="btn-kakao" onclick="showForm('register')">회원가입</button>
        `;
    }
}

/**
 * 메인 페이지의 인용구를 순환하여 표시하는 함수
 * 미리 정의된 인용구 배열에서 다음 인용구를 표시
 */
function displayNextQuote() {
    if (mainQuoteDisplay) {
        mainQuoteDisplay.textContent = `"${mainQuotes[currentQuoteIndex]}"`;
        currentQuoteIndex = (currentQuoteIndex + 1) % mainQuotes.length;
    }
}

/**
 * 메인 페이지 초기화 함수
 * URL 파라미터 확인, 로그인 상태 체크, 인용구 표시, 폼 초기화를 수행
 */
function initializeMainPage() {
    // URL 파라미터 확인 (로그인/회원가입 성공 여부)
    const urlParams = new URLSearchParams(window.location.search);
    const loginSuccess = urlParams.get('login');
    const registerSuccess = urlParams.get('registered');
    
    // 로그인 또는 회원가입 성공 시 즉시 로그인 상태로 설정
    if (loginSuccess === 'true' || registerSuccess === 'true') {
        isLoggedIn = true;
        renderAuthButtons();
        
        // 성공 메시지 표시 (선택사항)
        if (loginSuccess === 'true') {
            showMessage('로그인되었습니다!', 'success');
        } else if (registerSuccess === 'true') {
            showMessage('회원가입이 완료되었습니다!', 'success');
        }
        
        // URL에서 파라미터 제거
        const newUrl = window.location.pathname;
        window.history.replaceState({}, document.title, newUrl);
    } else {
        // 일반적인 경우 서버에서 로그인 상태 확인
        checkLoginStatus().then(() => {
            renderAuthButtons();
        });
    }
    
    displayNextQuote();
    setInterval(displayNextQuote, 5000);
    
    // 페이지 로드 시 폼들을 숨김 상태로 초기화
    if (mainLoginFormSection) {
        mainLoginFormSection.classList.add('hidden');
    }
    if (mainRegistrationFormSection) {
        mainRegistrationFormSection.classList.add('hidden');
    }
}

/**
 * 사용자에게 알림 메시지를 표시하는 함수
 * @param {string} message - 표시할 메시지
 * @param {string} type - 'success' 또는 'error'
 */
function showMessage(message, type) {
    // 간단한 알림 메시지 표시
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 10px 20px;
        border-radius: 5px;
        color: white;
        font-weight: bold;
        z-index: 10000;
        ${type === 'success' ? 'background-color: #4CAF50;' : 'background-color: #f44336;'}
    `;
    
    document.body.appendChild(messageDiv);
    
    // 3초 후 메시지 제거
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.parentNode.removeChild(messageDiv);
        }
    }, 3000);
}

// --- Registration Form Validation ---
let emailCheckTimer = null;
let nicknameCheckTimer = null;
let isNicknameValid = false;
let isEmailValid = false;
let isPasswordValid = false;
let isConfirmPasswordValid = false;
let isTermsAgreed = false;

// 사용자가 입력을 시작했는지 추적하는 변수들
let nicknameTouched = false;
let emailTouched = false;
let passwordTouched = false;
let confirmPasswordTouched = false;

/**
 * 서버에서 닉네임 중복 여부를 확인하는 함수
 * @param {string} nickname - 확인할 닉네임
 * @returns {boolean} 중복되지 않으면 true, 중복되면 false
 */
async function checkNicknameAvailability(nickname) {
    try {
        const response = await fetch('/api/check-nickname', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `nickname=${encodeURIComponent(nickname)}`
        });
        
        if (response.ok) {
            const isDuplicate = await response.text();
            return isDuplicate === 'false'; // 중복되지 않으면 true 반환
        }
        return false;
    } catch (error) {
        console.error('닉네임 중복 확인 중 오류:', error);
        return false;
    }
}

/**
 * 서버에서 이메일 중복 여부를 확인하는 함수
 * @param {string} email - 확인할 이메일
 * @returns {boolean} 중복되지 않으면 true, 중복되면 false
 */
async function checkEmailAvailability(email) {
    try {
        const response = await fetch('/api/check-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `email=${encodeURIComponent(email)}`
        });
        
        if (response.ok) {
            const isDuplicate = await response.text();
            return isDuplicate === 'false'; // 중복되지 않으면 true 반환
        }
        return false;
    } catch (error) {
        console.error('이메일 중복 확인 중 오류:', error);
        return false;
    }
}

/**
 * 이메일 형식이 올바른지 검증하는 함수
 * @param {string} email - 검증할 이메일
 * @returns {boolean} 올바른 형식이면 true, 아니면 false
 */
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * 닉네임 입력 필드의 실시간 검증을 처리하는 함수
 * 길이 검사, 중복 검사를 수행하고 UI 상태를 업데이트
 */
async function handleNicknameInput() {
    const nicknameInput = document.getElementById('reg-name');
    const nicknameError = document.getElementById('nickname-error');
    const nicknameSuccess = document.getElementById('nickname-success');
    const nickname = nicknameInput.value.trim();

    // 사용자가 입력을 시작했음을 표시
    nicknameTouched = true;

    // 이전 타이머 클리어
    if (nicknameCheckTimer) {
        clearTimeout(nicknameCheckTimer);
    }

    // 닉네임이 비어있으면 검증하지 않음
    if (!nickname) {
        nicknameInput.classList.remove('error', 'success');
        nicknameError.classList.remove('show');
        nicknameSuccess.classList.remove('show');
        isNicknameValid = false;
        updateSubmitButton();
        return;
    }

    // 닉네임 길이 검사 (2-20자)
    if (nickname.length < 2 || nickname.length > 20) {
        nicknameInput.classList.remove('success');
        nicknameInput.classList.add('error');
        nicknameError.textContent = '닉네임은 2-20자 사이여야 합니다.';
        nicknameError.classList.add('show');
        nicknameSuccess.classList.remove('show');
        isNicknameValid = false;
        updateSubmitButton();
        return;
    }

    // 중복 검사는 사용자가 타이핑을 멈춘 후 500ms 후에 실행
    nicknameCheckTimer = setTimeout(async () => {
        const isAvailable = await checkNicknameAvailability(nickname);
        if (isAvailable) {
            nicknameInput.classList.remove('error');
            nicknameInput.classList.add('success');
            nicknameError.classList.remove('show');
            nicknameSuccess.classList.add('show');
            isNicknameValid = true;
        } else {
            nicknameInput.classList.remove('success');
            nicknameInput.classList.add('error');
            nicknameError.textContent = '중복된 닉네임입니다.';
            nicknameError.classList.add('show');
            nicknameSuccess.classList.remove('show');
            isNicknameValid = false;
        }
        updateSubmitButton();
    }, 500);
}

/**
 * 이메일 입력 필드의 실시간 검증을 처리하는 함수
 * 형식 검사, 중복 검사를 수행하고 UI 상태를 업데이트
 */
async function handleEmailInput() {
    const emailInput = document.getElementById('reg-email');
    const emailError = document.getElementById('email-error');
    const emailSuccess = document.getElementById('email-success');
    const email = emailInput.value.trim();

    // 사용자가 입력을 시작했음을 표시
    emailTouched = true;

    // 이전 타이머 클리어
    if (emailCheckTimer) {
        clearTimeout(emailCheckTimer);
    }

    // 이메일이 비어있으면 검증하지 않음
    if (!email) {
        emailInput.classList.remove('error', 'success');
        emailError.classList.remove('show');
        emailSuccess.classList.remove('show');
        isEmailValid = false;
        updateSubmitButton();
        return;
    }

    // 이메일 형식 검사
    if (!validateEmail(email)) {
        emailInput.classList.remove('success');
        emailInput.classList.add('error');
        emailError.textContent = '올바른 이메일 형식을 입력해주세요.';
        emailError.classList.add('show');
        emailSuccess.classList.remove('show');
        isEmailValid = false;
        updateSubmitButton();
        return;
    }

    // 중복 검사는 사용자가 타이핑을 멈춘 후 500ms 후에 실행
    emailCheckTimer = setTimeout(async () => {
        const isAvailable = await checkEmailAvailability(email);
        if (isAvailable) {
            emailInput.classList.remove('error');
            emailInput.classList.add('success');
            emailError.classList.remove('show');
            emailSuccess.classList.add('show');
            isEmailValid = true;
        } else {
            emailInput.classList.remove('success');
            emailInput.classList.add('error');
            emailError.textContent = '중복된 이메일입니다.';
            emailError.classList.add('show');
            emailSuccess.classList.remove('show');
            isEmailValid = false;
        }
        updateSubmitButton();
    }, 500);
}

/**
 * 비밀번호 입력 필드의 실시간 검증을 처리하는 함수
 * 길이 검사(8-20자)를 수행하고 UI 상태를 업데이트
 */
function handlePasswordInput() {
    const passwordInput = document.getElementById('reg-password');
    const passwordError = document.getElementById('password-error');
    const password = passwordInput.value;

    // 사용자가 입력을 시작했음을 표시
    passwordTouched = true;

    // 비밀번호가 비어있으면 검증하지 않음
    if (!password) {
        passwordInput.classList.remove('error', 'success');
        passwordError.classList.remove('show');
        isPasswordValid = false;
        updateSubmitButton();
        return;
    }

    if (password.length >= 8 && password.length <= 20) {
        passwordInput.classList.remove('error');
        passwordInput.classList.add('success');
        passwordError.classList.remove('show');
        isPasswordValid = true;
    } else {
        passwordInput.classList.remove('success');
        passwordInput.classList.add('error');
        passwordError.classList.add('show');
        isPasswordValid = false;
    }
    updateSubmitButton();
}

/**
 * 비밀번호 확인 입력 필드의 실시간 검증을 처리하는 함수
 * 비밀번호와 일치 여부를 검사하고 UI 상태를 업데이트
 */
function handleConfirmPasswordInput() {
    const passwordInput = document.getElementById('reg-password');
    const confirmPasswordInput = document.getElementById('reg-confirm-password');
    const confirmPasswordError = document.getElementById('confirm-password-error');
    const confirmPasswordSuccess = document.getElementById('confirm-password-success');
    const password = passwordInput.value;
    const confirmPassword = confirmPasswordInput.value;

    // 사용자가 입력을 시작했음을 표시
    confirmPasswordTouched = true;

    // 비밀번호 확인란이 비어있으면 검증하지 않음
    if (!confirmPassword) {
        confirmPasswordInput.classList.remove('error', 'success');
        confirmPasswordError.classList.remove('show');
        confirmPasswordSuccess.classList.remove('show');
        isConfirmPasswordValid = false;
        updateSubmitButton();
        return;
    }

    if (confirmPassword === password && password.length > 0) {
        confirmPasswordInput.classList.remove('error');
        confirmPasswordInput.classList.add('success');
        confirmPasswordError.classList.remove('show');
        confirmPasswordSuccess.classList.add('show');
        isConfirmPasswordValid = true;
    } else {
        confirmPasswordInput.classList.remove('success');
        confirmPasswordInput.classList.add('error');
        confirmPasswordError.classList.add('show');
        confirmPasswordSuccess.classList.remove('show');
        isConfirmPasswordValid = false;
    }
    updateSubmitButton();
}

/**
 * 약관 동의 체크박스 상태 변경을 처리하는 함수
 * 체크박스 상태에 따라 폼 유효성을 업데이트
 */
function handleTermsAgreement() {
    const termsCheckbox = document.getElementById('terms-agree');
    isTermsAgreed = termsCheckbox.checked;
    updateSubmitButton();
}

/**
 * 회원가입 폼의 제출 버튼 상태를 업데이트하는 함수
 * 모든 필수 필드가 유효한 경우에만 버튼을 활성화
 */
function updateSubmitButton() {
    const submitButton = document.getElementById('register-submit-btn');
    const isFormValid = isNicknameValid && isEmailValid && isPasswordValid && isConfirmPasswordValid && isTermsAgreed;
    
    if (isFormValid) {
        submitButton.disabled = false;
        submitButton.classList.remove('disabled');
    } else {
        submitButton.disabled = true;
        submitButton.classList.add('disabled');
    }
}

/**
 * 회원가입 폼 제출 시 최종 유효성 검사를 수행하는 함수
 * @param {Event} event - 폼 제출 이벤트
 * @returns {boolean} 모든 검증을 통과하면 true, 아니면 false
 */
function validateRegistrationForm(event) {
    console.log('validateRegistrationForm 호출됨');
    
    // 체크박스 상태 강제 확인
    const termsCheckbox = document.getElementById('terms-agree');
    isTermsAgreed = termsCheckbox.checked;
    
    console.log('현재 상태:', {
        isNicknameValid,
        isEmailValid,
        isPasswordValid,
        isConfirmPasswordValid,
        isTermsAgreed
    });
    
    // 폼 유효성 검사
    if (!isNicknameValid || !isEmailValid || !isPasswordValid || !isConfirmPasswordValid || !isTermsAgreed) {
        console.log('폼 유효성 검사 실패');
        event.preventDefault();
        alert('모든 필수 항목을 올바르게 입력해주세요.');
        return false;
    }

    // 폼이 유효하면 서버로 전송 허용
    console.log('회원가입 폼 제출: 모든 검증 통과');
    console.log('폼 데이터:', {
        userNickname: document.getElementById('reg-name').value,
        userEmail: document.getElementById('reg-email').value,
        userPassword: document.getElementById('reg-password').value,
        confirmPassword: document.getElementById('reg-confirm-password').value,
        userPhone: document.getElementById('reg-phone').value,
        termsAgreed: document.getElementById('terms-agree').checked
    });
    return true;
}

/**
 * 로그인 폼을 초기 상태로 리셋하는 함수
 * 모든 입력 필드를 비우고 에러 상태를 제거
 */
function resetLoginForm() {
    const loginForm = document.querySelector('#login-form-section form');
    if (loginForm) {
        loginForm.reset();
    }
}

/**
 * 회원가입 폼을 초기 상태로 리셋하는 함수
 * 모든 입력 필드, 상태 변수, 에러 메시지를 초기화
 */
function resetRegistrationForm() {
    // 모든 입력 필드 초기화
    const inputs = document.querySelectorAll('#registration-form input');
    inputs.forEach(input => {
        input.value = '';
        input.classList.remove('error', 'success');
    });

    // 모든 메시지 숨기기
    const messages = document.querySelectorAll('.error-message, .success-message');
    messages.forEach(message => {
        message.classList.remove('show');
    });

    // 상태 변수 초기화
    isNicknameValid = false;
    isEmailValid = false;
    isPasswordValid = false;
    isConfirmPasswordValid = false;
    isTermsAgreed = false;
    nicknameTouched = false;
    emailTouched = false;
    passwordTouched = false;
    confirmPasswordTouched = false;

    // 버튼 비활성화
    updateSubmitButton();
}

// 이벤트 리스너 등록
document.addEventListener('DOMContentLoaded', function() {
    initializeMainPage();
    
    // 로그인 폼 제출 이벤트 리스너
    const loginForm = document.querySelector('#login-form-section form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            // 폼 제출 후 즉시 로그인 상태로 설정 (서버 응답 대기 없이)
            setTimeout(() => {
                isLoggedIn = true;
                renderAuthButtons();
                hideForm('login');
            }, 500);
        });
    }
    
    // 회원가입 폼 이벤트 리스너
    const nicknameInput = document.getElementById('reg-name');
    const emailInput = document.getElementById('reg-email');
    const passwordInput = document.getElementById('reg-password');
    const confirmPasswordInput = document.getElementById('reg-confirm-password');
    const termsCheckbox = document.getElementById('terms-agree');
    
    if (nicknameInput) {
        nicknameInput.addEventListener('input', handleNicknameInput);
        nicknameInput.addEventListener('blur', handleNicknameInput); // 포커스 아웃 시에도 검증
    }
    
    if (emailInput) {
        emailInput.addEventListener('input', handleEmailInput);
        emailInput.addEventListener('blur', handleEmailInput); // 포커스 아웃 시에도 검증
    }
    
    if (passwordInput) {
        passwordInput.addEventListener('input', handlePasswordInput);
        passwordInput.addEventListener('blur', handlePasswordInput);
    }
    
    if (confirmPasswordInput) {
        confirmPasswordInput.addEventListener('input', handleConfirmPasswordInput);
        confirmPasswordInput.addEventListener('blur', handleConfirmPasswordInput);
    }
    
    if (termsCheckbox) {
        termsCheckbox.addEventListener('change', handleTermsAgreement);
    }
    
    // 회원가입 폼 제출 이벤트 리스너
    const registerForm = document.querySelector('#registration-form-section form');
    if (registerForm) {
        registerForm.addEventListener('submit', function(e) {
            // 폼 제출 후 즉시 로그인 상태로 설정 (서버 응답 대기 없이)
            setTimeout(() => {
                isLoggedIn = true;
                renderAuthButtons();
                hideForm('register');
            }, 500);
        });
    }
}); 