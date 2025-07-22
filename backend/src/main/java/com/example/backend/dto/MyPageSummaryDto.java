package com.example.backend.dto;

import java.time.LocalDate;
import java.util.List;

public class MyPageSummaryDto {
    private String nickname;
    private String email;
    private LocalDate joinDate;
    private int totalDiaryCount;
    private int consecutiveDiaryDays;
    private List<String> mainEmotions;
    private String recentAiComment;
    private String recentStampImage;

    public MyPageSummaryDto() {}

    public String getNickname() { return nickname; }
    public void setNickname(String nickname) { this.nickname = nickname; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public LocalDate getJoinDate() { return joinDate; }
    public void setJoinDate(LocalDate joinDate) { this.joinDate = joinDate; }

    public int getTotalDiaryCount() { return totalDiaryCount; }
    public void setTotalDiaryCount(int totalDiaryCount) { this.totalDiaryCount = totalDiaryCount; }

    public int getConsecutiveDiaryDays() { return consecutiveDiaryDays; }
    public void setConsecutiveDiaryDays(int consecutiveDiaryDays) { this.consecutiveDiaryDays = consecutiveDiaryDays; }

    public List<String> getMainEmotions() { return mainEmotions; }
    public void setMainEmotions(List<String> mainEmotions) { this.mainEmotions = mainEmotions; }

    public String getRecentAiComment() { return recentAiComment; }
    public void setRecentAiComment(String recentAiComment) { this.recentAiComment = recentAiComment; }

    public String getRecentStampImage() { return recentStampImage; }
    public void setRecentStampImage(String recentStampImage) { this.recentStampImage = recentStampImage; }
} 