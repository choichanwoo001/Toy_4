package com.example.backend.repository;

import com.example.backend.entity.*;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDateTime;
import java.util.List;

// 지정된 날짜 범위(start ~ end)에 작성된 일일 코멘트를 조회
public interface DailyCommentRepository extends JpaRepository<DailyComment, Long> {
    List<DailyComment> findByUser_UserIdAndDiaryDateBetween(Long userId, LocalDateTime start, LocalDateTime end);
    DailyComment findByDiary(Diary diary);
    DailyComment findTopByUserOrderByCreatedAtDesc(User user);
}
