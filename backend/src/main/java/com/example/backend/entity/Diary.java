package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "diary")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Diary {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "diary_id")
    private Long diaryId;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @Column(name = "created_at", nullable = false)
    private LocalDateTime createdAt;

    @Column(name = "content", nullable = false, columnDefinition = "TEXT")
    private String content;

    @Column(name = "applied_stamp", nullable = false, length = 50)
    private String appliedStamp;

    // ===================== NEW ENTITY FIELD ADDED =====================
    // 2025-01-XX: 감정 표현 기능 추가를 위한 emotion 필드 추가
    // 사용자가 일기 작성 시 선택한 감정 이모지를 저장
    // 예시: 😊(행복), 😢(슬픔), 😡(화남), 😌(평온), 🤔(고민), 😴(피곤), 😍(사랑), 😤(스트레스)
    @Column(length = 10)
    private String emotion; // 감정 이모지 저장 (예: 😊, 😢, 😡 등)
    // ===================== END NEW ENTITY FIELD =====================

    // getter/setter
    public Long getDiaryId() { return diaryId; }
    public void setDiaryId(Long diaryId) { this.diaryId = diaryId; }
    public User getUser() { return user; }
    public void setUser(User user) { this.user = user; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    public String getContent() { return content; }
    public void setContent(String content) { this.content = content; }
    public String getAppliedStamp() { return appliedStamp; }
    public void setAppliedStamp(String appliedStamp) { this.appliedStamp = appliedStamp; }

    // ===================== NEW GETTER/SETTER ADDED =====================
    // 2025-01-XX: emotion 필드에 대한 getter/setter 추가
    public String getEmotion() { return emotion; }
    public void setEmotion(String emotion) { this.emotion = emotion; }
    // ===================== END NEW GETTER/SETTER =====================
}