-- ===================== DATABASE SCHEMA UPDATE =====================
-- 2025-01-XX: 감정 표현 기능 추가를 위한 데이터베이스 스키마 업데이트
-- Diary 테이블에 emotion 컬럼 추가
-- 사용자가 일기 작성 시 선택한 감정 이모지를 저장하기 위한 필드
-- ===================== END DATABASE SCHEMA UPDATE =====================

-- Diary 테이블에 emotion 컬럼 추가
ALTER TABLE diary ADD COLUMN emotion VARCHAR(10);

-- 기존 데이터에 대한 기본값 설정 (선택사항)
-- UPDATE diary SET emotion = NULL WHERE emotion IS NULL;

-- 컬럼 설명 추가
COMMENT ON COLUMN diary.emotion IS '감정 이모지 저장 (예: 😊, 😢, 😡 등)';

-- ===================== UPDATE COMPLETED =====================
-- 2025-01-XX: 감정 표현 기능을 위한 데이터베이스 스키마 업데이트 완료
-- 이제 Diary 엔티티에서 emotion 필드를 사용할 수 있습니다.
-- ===================== END UPDATE =====================

-- Diary 테이블에서 applied_stamp 컬럼 제거 (2025-01-XX)
-- 일기와 스탬프의 관심사 분리를 위한 스키마 업데이트

ALTER TABLE diary DROP COLUMN applied_stamp;

-- 기존 데이터 확인 (선택사항)
-- SELECT diary_id, content, emotion FROM diary LIMIT 10;

-- ===================== WEEKLY REPORT TABLES =====================
-- 2025-01-XX: 주간 리포트 기능을 위한 테이블들 생성

-- 감정 데이터 테이블
CREATE TABLE IF NOT EXISTS emotion_data (
    emotion_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- 일일 코멘트 테이블
CREATE TABLE IF NOT EXISTS daily_comment (
    comment_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    diary_date DATETIME NOT NULL,
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- 코멘트-감정 매핑 테이블
CREATE TABLE IF NOT EXISTS comment_emotion_mapping (
    mapping_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    comment_id BIGINT NOT NULL,
    emotion_id BIGINT NOT NULL,
    FOREIGN KEY (comment_id) REFERENCES daily_comment(comment_id),
    FOREIGN KEY (emotion_id) REFERENCES emotion_data(emotion_id)
);

-- 주간 피드백 테이블
CREATE TABLE IF NOT EXISTS weekly_feedback (
    feedback_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    is_qualified VARCHAR(1) DEFAULT 'N',
    emotion_summary TEXT,
    week_offset INT NOT NULL,
    feedback_start VARCHAR(10),
    feedback_end VARCHAR(10),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- 피드백 근거 테이블
CREATE TABLE IF NOT EXISTS feedback_proof (
    proof_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    feedback_id BIGINT NOT NULL,
    detail TEXT,
    FOREIGN KEY (feedback_id) REFERENCES weekly_feedback(feedback_id)
);

-- 추천 활동 테이블
CREATE TABLE IF NOT EXISTS recommend_activity (
    activity_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    feedback_id BIGINT NOT NULL,
    title VARCHAR(200),
    detail TEXT,
    FOREIGN KEY (feedback_id) REFERENCES weekly_feedback(feedback_id)
);

-- ===================== END WEEKLY REPORT TABLES ===================== 