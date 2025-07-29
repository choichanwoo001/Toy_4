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
(2, NOW() - INTERVAL 2 DAY, '오늘은 정말 좋은 하루였어요!', '참잘했어요', '😊'),
(2, NOW() - INTERVAL 3 DAY, '운동을 시작했는데 몸이 좋아지는 것 같아요.', '참잘했어요', '😌'),
(2, NOW() - INTERVAL 4 DAY, '친구와 오랜만에 만났어요.', '참잘했어요', '😍'),
(2, NOW() - INTERVAL 5 DAY, '조금 피곤하지만 괜찮아요.', '참잘했어요', '😴'),
(2, NOW() - INTERVAL 6 DAY, '새로운 프로젝트를 시작했어요.', '참잘했어요', '😊'),
(2, NOW() - INTERVAL 7 DAY, '오늘은 조금 스트레스가 있었지만 잘 해냈어요.', '참잘했어요', '😤'),
(2, NOW() - INTERVAL 8 DAY, '주말에 푹 쉬었어요.', '참잘했어요', '😌'),
(2, NOW() - INTERVAL 9 DAY, '새로운 취미를 시작했어요.', '참잘했어요', '😊'),
(2, NOW() - INTERVAL 10 DAY, '오늘은 조금 우울했어요.', '참잘했어요', '😢'),
(2, NOW() - INTERVAL 11 DAY, '친구와 놀러갔어요!', '참잘했어요', '😍'),
(2, NOW() - INTERVAL 12 DAY, '공부를 열심히 했어요.', '참잘했어요', '😤'),
(2, NOW() - INTERVAL 13 DAY, '가족과 함께 저녁을 먹었어요.', '참잘했어요', '😊'),
(2, NOW() - INTERVAL 14 DAY, '새로운 영화를 봤어요.', '참잘했어요', '😌');
-- ===================== END NEW FIELD TEST DATA =====================

-- ===================== WEEKLY REPORT TEST DATA =====================
-- 2025-01-XX: 주간 리포트 테스트를 위한 샘플 데이터 생성

-- 주간 피드백 데이터 생성
INSERT INTO weekly_feedback (user_id, is_qualified, emotion_summary, week_offset, feedback_start, feedback_end, created_at) 
VALUES 
(2, 'Y', '이번 주는 다양한 감정을 경험하셨네요. 새로운 책 읽기와 운동으로 자기계발에 집중하시는 모습이 인상적입니다.', 0, '2025-01-13', '2025-01-19', NOW()),
(2, 'Y', '지난 주는 친구들과의 만남과 새로운 프로젝트로 인한 기쁨이 많았습니다. 스트레스도 있었지만 잘 극복하셨네요.', 1, '2025-01-06', '2025-01-12', NOW());

-- 추천 활동 데이터 생성
INSERT INTO recommend_activity (feedback_id, title, detail) 
VALUES 
(1, '새로운 취미 시작하기', '새로운 책 읽기에 대한 관심이 높으시니, 다른 취미도 시도해보세요.'),
(1, '운동 루틴 만들기', '운동을 시작하셨으니, 꾸준한 루틴을 만들어보세요.'),
(2, '친구들과 더 자주 만나기', '친구와의 만남이 기쁨을 주셨으니, 더 자주 만나보세요.');

-- 피드백 근거 데이터 생성
INSERT INTO feedback_proof (feedback_id, detail) 
VALUES 
(1, '새로운 책 읽기에 대한 관심이 표현되었습니다.'),
(1, '운동을 통해 자기계발에 집중하시는 모습이 나타났습니다.'),
(2, '친구들과의 만남으로 인한 기쁨이 표현되었습니다.');
-- ===================== END WEEKLY REPORT TEST DATA =====================

-- ===================== TEST DATA COMPLETED =====================
-- 2025-01-XX: 감정 표현 기능 테스트를 위한 샘플 데이터 생성 완료
-- 이제 emotion 필드가 포함된 일기 데이터로 기능을 테스트할 수 있습니다.
-- ===================== END TEST DATA ===================== 