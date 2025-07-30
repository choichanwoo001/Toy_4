package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Entity
@Table(name = "daily_comment")
@Getter
@NoArgsConstructor(access = AccessLevel.PUBLIC)
public class DailyComment {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "daily_comment_id")
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id")
    private User user;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "diary_id")
    private Diary diary;

    @Column(name = "diary_date")
    private LocalDateTime diaryDate;

    @Column(name = "content", columnDefinition = "TEXT")
    private String content;

    @Column(name = "created_at")
    private LocalDateTime createdAt;

    // ===================== NEW ENTITY FIELD ADDED =====================
    // 2025-01-XX: 코멘트 작성 시 적용된 스탬프 정보 추가
    // 코멘트 제출 시 현재 적용중인 스탬프의 user_stamp_id를 저장
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_stamp_id")
    private UserStamp userStamp;
    // ===================== END NEW ENTITY FIELD =====================

    // getter/setter
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public User getUser() { return user; }
    public void setUser(User user) { this.user = user; }
    public Diary getDiary() { return diary; }
    public void setDiary(Diary diary) { this.diary = diary; }
    public LocalDateTime getDiaryDate() { return diaryDate; }
    public void setDiaryDate(LocalDateTime diaryDate) { this.diaryDate = diaryDate; }
    public String getContent() { return content; }
    public void setContent(String content) { this.content = content; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }

    // ===================== NEW GETTER/SETTER ADDED =====================
    // 2025-01-XX: userStamp 필드에 대한 getter/setter 추가
    public UserStamp getUserStamp() { return userStamp; }
    public void setUserStamp(UserStamp userStamp) { this.userStamp = userStamp; }
    // ===================== END NEW GETTER/SETTER =====================
}