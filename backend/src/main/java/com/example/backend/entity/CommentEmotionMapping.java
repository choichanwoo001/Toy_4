package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "comment_emotion_mapping")
@Data
public class CommentEmotionMapping {
    @EmbeddedId
    private CommentEmotionMappingId id;

    @ManyToOne(fetch = FetchType.LAZY)
    @MapsId("dailyCommentId")
    @JoinColumn(name = "daily_comment_id", nullable = false)
    private DailyComment dailyComment;

    @ManyToOne(fetch = FetchType.LAZY)
    @MapsId("emotionId")
    @JoinColumn(name = "emotion_id", nullable = false)
    private EmotionData emotionData;
}

@Embeddable
@Data
class CommentEmotionMappingId implements java.io.Serializable {
    private Long dailyCommentId;
    private Long emotionId;
} 