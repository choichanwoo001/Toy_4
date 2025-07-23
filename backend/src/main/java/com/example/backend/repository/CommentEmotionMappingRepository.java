package com.example.backend.repository;

import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import com.example.backend.entity.CommentEmotionMapping;
import com.example.backend.entity.DailyComment;

public interface CommentEmotionMappingRepository extends JpaRepository<CommentEmotionMapping, Long> {
    @Query("SELECT e.name FROM CommentEmotionMapping c JOIN c.emotionData e WHERE c.dailyComment = :dailyComment")
    List<String> findEmotionsByDailyComment(@Param("dailyComment") DailyComment dailyComment);
}
