package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Entity
@Table(name = "comment_emotion_mapping")
@Getter
@NoArgsConstructor
public class CommentEmotionMapping {

    @EmbeddedId
    private CommentEmotionId id;

    @ManyToOne(fetch = FetchType.LAZY)
    @MapsId("dailyCommentId")
    @JoinColumn(name = "daily_comment_id")
    private DailyComment dailyComment;

    @ManyToOne(fetch = FetchType.LAZY)
    @MapsId("emotionId")
    @JoinColumn(name = "emotion_id")
    private EmotionData emotionData; // 👈 이 필드가 있어야 getEmotionData() 가능
}
