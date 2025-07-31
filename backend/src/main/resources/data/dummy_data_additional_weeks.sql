-- Additional dummy data for other weeks to test navigation
-- This data should be inserted after the main dummy data

-- Insert dummy diaries for week 7/7 - 7/13 (weekOffset = 1)
INSERT INTO diary (diary_id, user_id, content, emotion, created_at) VALUES
(2001, 1, '새로운 주가 시작되었다. 이번 주도 잘 해보자!', '😊', '2024-07-07 09:00:00'),
(2002, 1, '오늘은 조금 바빴지만 보람찼다.', '😐', '2024-07-08 18:30:00'),
(2003, 1, '친구와 오랜만에 만났다. 정말 즐거웠다.', '😊', '2024-07-09 20:15:00'),
(2004, 1, '오늘은 조용히 쉬었다. 편안했다.', '😌', '2024-07-10 16:45:00'),
(2005, 1, '새로운 취미를 시작했다. 재미있다!', '😊', '2024-07-11 14:20:00'),
(2006, 1, '가족과 맛있는 저녁을 먹었다.', '😊', '2024-07-12 19:30:00'),
(2007, 1, '주말이 끝나간다. 내일 월요일이 걱정이다.', '😰', '2024-07-13 22:00:00');

-- Insert dummy daily comments for week 7/7 - 7/13
INSERT INTO daily_comment (daily_comment_id, user_id, diary_id, content, created_at) VALUES
(3001, 1, 2001, '새로운 주를 긍정적으로 시작하신 것 같아요! 좋은 마음가짐이네요.', '2024-07-07 09:05:00'),
(3002, 1, 2002, '바쁜 하루를 보내셨지만 보람찼다고 하니 다행이에요.', '2024-07-08 18:35:00'),
(3003, 1, 2003, '친구와의 만남이 즐거웠다니 좋네요. 소중한 시간이었을 것 같아요.', '2024-07-09 20:20:00'),
(3004, 1, 2004, '조용한 시간도 정말 소중해요. 휴식을 잘 취하셨네요.', '2024-07-10 16:50:00'),
(3005, 1, 2005, '새로운 취미를 시작하셨군요! 새로운 경험은 항상 즐거워요.', '2024-07-11 14:25:00'),
(3006, 1, 2006, '가족과의 시간이 행복했을 것 같아요. 소중한 순간이네요.', '2024-07-12 19:35:00'),
(3007, 1, 2007, '월요일이 걱정되시는군요. 하지만 새로운 한 주도 잘 해내실 거예요!', '2024-07-13 22:05:00');

-- Insert dummy weekly feedback for week 7/7 - 7/13 (weekOffset = 1)
INSERT INTO weekly_feedback (feedback_id, user_id, emotion_summary, week_offset, feedback_start, feedback_end, created_at) VALUES
(4002, 1, '이번 주는 전반적으로 긍정적인 감정이 많았어요. 새로운 취미를 시작하시고 친구와의 만남도 즐기셨네요. 가족과의 시간도 행복했고, 조용한 휴식 시간도 잘 보내셨답니다. 다만 주말 끝에 월요일에 대한 걱정이 있었지만, 이는 자연스러운 감정이에요.', 1, '2024-07-07', '2024-07-13', '2024-07-14 00:00:00');

-- Insert dummy feedback proof for week 7/7 - 7/13
INSERT INTO feedback_proof (proof_id, feedback_id, diary_id, proof_type, proof_detail, created_at) VALUES 
(4008, 4002, 2001, 'positive', '새로운 주가 시작되었다. 이번 주도 잘 해보자!', NOW()),
(4009, 4002, 2002, 'neutral', '오늘은 조금 바빴지만 보람찼다.', NOW()),
(4010, 4002, 2003, 'positive', '친구와 오랜만에 만났다. 정말 즐거웠다.', NOW()),
(4011, 4002, 2004, 'neutral', '오늘은 조용히 쉬었다. 편안했다.', NOW()),
(4012, 4002, 2005, 'positive', '새로운 취미를 시작했다. 재미있다!', NOW()),
(4013, 4002, 2006, 'positive', '가족과 맛있는 저녁을 먹었다.', NOW()),
(4014, 4002, 2007, 'negative', '주말이 끝나간다. 내일 월요일이 걱정이다.', NOW());

-- Insert dummy recommend activities for week 7/7 - 7/13
INSERT INTO recommend_activity (activity_id, feedback_id, diary_id, activity_title, activity_category, activity_detail, activity_order, created_at) VALUES 
(4004, 4002, 2005, '새로운 취미 계속하기', 'hobby', '새로운 취미를 즐기고 계시는군요! 이런 새로운 경험을 더 늘려보세요.', 1, NOW()),
(4005, 4002, 2007, '월요일 준비하기', 'planning', '월요일에 대한 걱정을 줄이기 위해 주말에 다음 주 계획을 세워보세요.', 2, NOW()),
(4006, 4002, 2004, '휴식 시간 활용', 'self_care', '조용한 시간을 잘 활용하고 계시네요. 이런 평온한 순간들을 더 늘려보세요.', 3, NOW());

-- Insert dummy diaries for week 6/23 - 6/29 (weekOffset = 2)
INSERT INTO diary (diary_id, user_id, content, emotion, created_at) VALUES
(3001, 1, '이번 주도 잘 마무리했다. 다음 주도 힘내자!', '😊', '2024-06-23 21:00:00'),
(3002, 1, '오늘은 조금 피곤했다. 휴식을 취해야겠다.', '😐', '2024-06-24 19:30:00'),
(3003, 1, '새로운 영화를 봤다. 정말 재미있었다.', '😊', '2024-06-25 22:15:00'),
(3004, 1, '친구와 통화했다. 오랜만에 이야기해서 좋았다.', '😊', '2024-06-26 18:45:00'),
(3005, 1, '오늘은 조용히 책을 읽었다.', '😌', '2024-06-27 15:20:00'),
(3006, 1, '가족과 맛있는 점심을 먹었다.', '😊', '2024-06-28 13:30:00'),
(3007, 1, '주말을 잘 보냈다. 내일 월요일이 기대된다.', '😊', '2024-06-29 20:00:00');

-- Insert dummy daily comments for week 6/23 - 6/29
INSERT INTO daily_comment (daily_comment_id, user_id, diary_id, content, created_at) VALUES
(4001, 1, 3001, '한 주를 잘 마무리하셨네요! 다음 주도 긍정적인 마음가짐으로 시작하세요.', '2024-06-23 21:05:00'),
(4002, 1, 3002, '피곤하실 때는 충분한 휴식이 필요해요. 잘 쉬세요.', '2024-06-24 19:35:00'),
(4003, 1, 3003, '새로운 영화를 보시고 즐거웠다니 좋네요!', '2024-06-25 22:20:00'),
(4004, 1, 3004, '친구와의 통화가 즐거웠다니 다행이에요. 소중한 관계네요.', '2024-06-26 18:50:00'),
(4005, 1, 3005, '책 읽기를 좋아하시는군요. 독서는 마음을 치유해주는 좋은 활동이에요.', '2024-06-27 15:25:00'),
(4006, 1, 3006, '가족과의 시간이 행복했을 것 같아요.', '2024-06-28 13:35:00'),
(4007, 1, 3007, '월요일을 기대하신다니 좋네요! 긍정적인 마음가짐이에요.', '2024-06-29 20:05:00');

-- Insert dummy weekly feedback for week 6/23 - 6/29 (weekOffset = 2)
INSERT INTO weekly_feedback (feedback_id, user_id, emotion_summary, week_offset, feedback_start, feedback_end, created_at) VALUES
(4003, 1, '이번 주는 전반적으로 평온하고 긍정적인 감정이 많았어요. 새로운 영화를 보시고 친구와의 통화도 즐기셨네요. 가족과의 시간도 행복했고, 독서를 통한 조용한 시간도 잘 보내셨답니다. 월요일에 대한 긍정적인 기대감도 보이시네요.', 2, '2024-06-23', '2024-06-29', '2024-06-30 00:00:00');

-- Insert dummy feedback proof for week 6/23 - 6/29
INSERT INTO feedback_proof (proof_id, feedback_id, diary_id, proof_type, proof_detail, created_at) VALUES 
(4015, 4003, 3001, 'positive', '이번 주도 잘 마무리했다. 다음 주도 힘내자!', NOW()),
(4016, 4003, 3002, 'neutral', '오늘은 조금 피곤했다. 휴식을 취해야겠다.', NOW()),
(4017, 4003, 3003, 'positive', '새로운 영화를 봤다. 정말 재미있었다.', NOW()),
(4018, 4003, 3004, 'positive', '친구와 통화했다. 오랜만에 이야기해서 좋았다.', NOW()),
(4019, 4003, 3005, 'neutral', '오늘은 조용히 책을 읽었다.', NOW()),
(4020, 4003, 3006, 'positive', '가족과 맛있는 점심을 먹었다.', NOW()),
(4021, 4003, 3007, 'positive', '주말을 잘 보냈다. 내일 월요일이 기대된다.', NOW());

-- Insert dummy recommend activities for week 6/23 - 6/29
INSERT INTO recommend_activity (activity_id, feedback_id, diary_id, activity_title, activity_category, activity_detail, activity_order, created_at) VALUES 
(4007, 4003, 3003, '영화 감상 계속하기', 'hobby', '영화를 보는 것을 즐기고 계시는군요! 다양한 장르의 영화를 시도해보세요.', 1, NOW()),
(4008, 4003, 3005, '독서 시간 늘리기', 'hobby', '책 읽기를 좋아하시는군요! 더 많은 독서 시간을 가져보세요.', 2, NOW()),
(4009, 4003, 3004, '친구와의 소통', 'social', '친구와의 통화가 즐거웠다니 좋네요. 더 많은 친구들과 소통해보세요.', 3, NOW()); 