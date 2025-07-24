package com.example.backend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.backend.entity.DailyComment;
import com.example.backend.entity.Diary;
import com.example.backend.entity.User;

public interface DailyCommentRepository extends JpaRepository<DailyComment, Long> {
    DailyComment findByDiary(Diary diary);
    DailyComment findTopByUserOrderByCreatedAtDesc(User user);
}
