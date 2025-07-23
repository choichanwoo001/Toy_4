package com.example.backend.dto;

import java.time.LocalDateTime;

public class UserPointHistoryDto {
    private Long userPointHistoryId;
    private Long userId;
    private int beforePoint;
    private int amount;
    private int afterPoint;
    private String reason;
    private LocalDateTime createdAt;

    // Getter & Setter
    public Long getUserPointHistoryId() { return userPointHistoryId; }
    public void setUserPointHistoryId(Long userPointHistoryId) { this.userPointHistoryId = userPointHistoryId; }
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    public int getBeforePoint() { return beforePoint; }
    public void setBeforePoint(int beforePoint) { this.beforePoint = beforePoint; }
    public int getAmount() { return amount; }
    public void setAmount(int amount) { this.amount = amount; }
    public int getAfterPoint() { return afterPoint; }
    public void setAfterPoint(int afterPoint) { this.afterPoint = afterPoint; }
    public String getReason() { return reason; }
    public void setReason(String reason) { this.reason = reason; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
} 