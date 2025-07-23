package com.example.backend.repository;

import com.example.backend.entity.DailyComment;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDateTime;
import java.util.List;

public interface DailyCommentRepository extends JpaRepository<DailyComment, Long> {
    List<DailyComment> findByUser_UserIdAndDiaryDateBetween(Long userId, LocalDateTime start, LocalDateTime end);
}
