package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;


@Entity
@Table(name = "comment_emotion_mapping")
@Getter
@Setter
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
