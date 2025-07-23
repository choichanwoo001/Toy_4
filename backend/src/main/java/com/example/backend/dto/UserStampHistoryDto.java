package com.example.backend.dto;

import java.time.LocalDateTime;

public class UserStampHistoryDto {
    private Long userStampHistoryId;
    private Long userId;
    private Long prevStampId;
    private Long newStampId;
    private LocalDateTime createdAt;

    // Getter & Setter
    public Long getUserStampHistoryId() { return userStampHistoryId; }
    public void setUserStampHistoryId(Long userStampHistoryId) { this.userStampHistoryId = userStampHistoryId; }
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    public Long getPrevStampId() { return prevStampId; }
    public void setPrevStampId(Long prevStampId) { this.prevStampId = prevStampId; }
    public Long getNewStampId() { return newStampId; }
    public void setNewStampId(Long newStampId) { this.newStampId = newStampId; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
} 