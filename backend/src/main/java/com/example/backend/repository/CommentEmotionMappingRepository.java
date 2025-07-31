package com.example.backend.repository;

import com.example.backend.entity.CommentEmotionMapping;
import com.example.backend.entity.CommentEmotionId;
import com.example.backend.entity.DailyComment;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CommentEmotionMappingRepository extends JpaRepository<CommentEmotionMapping, CommentEmotionId> {
    List<CommentEmotionMapping> findByDailyCommentIn(List<DailyComment> comments);
    List<CommentEmotionMapping> findByDailyComment(DailyComment dailyComment);
}
