package com.example.backend.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Embeddable;
import lombok.*;

import java.io.Serializable;

@Embeddable
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode
public class CommentEmotionId implements Serializable {

    @Column(name = "daily_comment_id")
    private Long dailyCommentId;

    @Column(name = "emotion_id")
    private Long emotionId;
}

