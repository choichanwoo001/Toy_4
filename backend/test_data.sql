-- ===================== TEST DATA CREATION =====================
-- 2025-01-XX: 감정 표현 기능 테스트를 위한 샘플 데이터 생성
-- 새로운 emotion 필드를 포함한 테스트 데이터 추가
-- ===================== END TEST DATA CREATION =====================

-- 테스트용 사용자 데이터 생성
INSERT INTO user (user_email, user_password, user_nickname, user_phone, user_failed_login, user_last_login, user_comment_time, user_token_count, user_created_at, user_status) 
VALUES 
('test@example.com', 'password123', '테스트사용자', '010-1234-5678', 0, NOW(), 6, 100, NOW(), 'active'),
('user2@example.com', 'password123', '사용자2', '010-2345-6789', 0, NOW(), 6, 50, NOW(), 'active');

-- ===================== NEW FIELD TEST DATA =====================
-- 2025-01-XX: emotion 필드를 포함한 테스트용 일기 데이터 생성
-- 다양한 감정 이모지를 사용하여 기능 테스트 가능
-- 테스트용 일기 데이터 생성 (감정 포함)
INSERT INTO diary (user_id, created_at, content, applied_stamp, emotion) 
VALUES 
(1, NOW() - INTERVAL 1 DAY, '오늘은 정말 좋은 하루였어요!', '참잘했어요', '😊'),
(1, NOW() - INTERVAL 2 DAY, '조금 피곤하지만 괜찮아요.', '참잘했어요', '😴'),
(1, NOW() - INTERVAL 3 DAY, '새로운 프로젝트를 시작했는데 기대돼요!', '참잘했어요', '😍'),
(1, NOW() - INTERVAL 5 DAY, '친구와 오랜만에 만나서 수다를 떨어요.', '참잘했어요', '😊'),
(1, NOW() - INTERVAL 7 DAY, '오늘은 조금 스트레스가 있었지만 잘 해냈어요.', '참잘했어요', '😤'),
(2, NOW() - INTERVAL 1 DAY, '새로운 책을 읽기 시작했어요.', '참잘했어요', '🤔'),
(2, NOW() - INTERVAL 3 DAY, '운동을 시작했는데 몸이 좋아지는 것 같아요.', '참잘했어요', '😌');
-- ===================== END NEW FIELD TEST DATA =====================

-- ===================== TEST DATA COMPLETED =====================
-- 2025-01-XX: 감정 표현 기능 테스트를 위한 샘플 데이터 생성 완료
-- 이제 emotion 필드가 포함된 일기 데이터로 기능을 테스트할 수 있습니다.
-- ===================== END TEST DATA ===================== 