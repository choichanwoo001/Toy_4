package com.example.backend.dto;

import java.time.LocalDateTime;

public class PointDto {
    private Long pointId;
    private String pointName;
    private int pointAmount;
    private String reason;
    private LocalDateTime createdAt;

    // Getter & Setter
    public Long getPointId() { return pointId; }
    public void setPointId(Long pointId) { this.pointId = pointId; }
    public String getPointName() { return pointName; }
    public void setPointName(String pointName) { this.pointName = pointName; }
    public int getPointAmount() { return pointAmount; }
    public void setPointAmount(int pointAmount) { this.pointAmount = pointAmount; }
    public String getReason() { return reason; }
    public void setReason(String reason) { this.reason = reason; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
} 