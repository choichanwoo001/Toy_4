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