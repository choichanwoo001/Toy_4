package com.example.backend.dto;

import java.time.LocalDateTime;

public class UserStampDto {
    private Long userStampId;
    private Long userId;
    private Long stampId;
    private String isActive; // "Y" or "N"
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    // Getter & Setter
    public Long getUserStampId() { return userStampId; }
    public void setUserStampId(Long userStampId) { this.userStampId = userStampId; }
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    public Long getStampId() { return stampId; }
    public void setStampId(Long stampId) { this.stampId = stampId; }
    public String getIsActive() { return isActive; }
    public void setIsActive(String isActive) { this.isActive = isActive; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
} 