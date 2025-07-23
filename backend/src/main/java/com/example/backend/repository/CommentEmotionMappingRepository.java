package com.example.backend.repository;

import com.example.backend.entity.CommentEmotionMapping;
import com.example.backend.entity.DailyComment;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface CommentEmotionMappingRepository extends JpaRepository<CommentEmotionMapping, CommentEmotionMapping> {
    List<CommentEmotionMapping> findByDailyCommentIn(List<DailyComment> comments);
}
