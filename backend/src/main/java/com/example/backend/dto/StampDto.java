package com.example.backend.dto;

import java.time.LocalDateTime;

public class StampDto {
    private Long stampId;
    private String name;
    private String image;
    private String qualification;
    private int price;
    private String description;
    private String status;
    private LocalDateTime salesAt;
    private LocalDateTime salesEnd;

    // Getter & Setter
    public Long getStampId() { return stampId; }
    public void setStampId(Long stampId) { this.stampId = stampId; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getImage() { return image; }
    public void setImage(String image) { this.image = image; }
    public String getQualification() { return qualification; }
    public void setQualification(String qualification) { this.qualification = qualification; }
    public int getPrice() { return price; }
    public void setPrice(int price) { this.price = price; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public LocalDateTime getSalesAt() { return salesAt; }
    public void setSalesAt(LocalDateTime salesAt) { this.salesAt = salesAt; }
    public LocalDateTime getSalesEnd() { return salesEnd; }
    public void setSalesEnd(LocalDateTime salesEnd) { this.salesEnd = salesEnd; }
} 