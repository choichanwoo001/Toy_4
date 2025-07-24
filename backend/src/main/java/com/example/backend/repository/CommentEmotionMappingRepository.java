package com.example.backend.repository;

import com.example.backend.entity.CommentEmotionMapping;
import com.example.backend.entity.DailyComment;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

// 주어진 일일 코멘트 목록에 해당하는 감정 매핑 정보를 조회
public interface CommentEmotionMappingRepository extends JpaRepository<CommentEmotionMapping, CommentEmotionMapping> {
    List<CommentEmotionMapping> findByDailyCommentIn(List<DailyComment> comments);
}
