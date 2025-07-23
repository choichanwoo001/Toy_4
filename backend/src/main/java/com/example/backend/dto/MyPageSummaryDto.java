package com.example.backend.dto;

import java.time.LocalDate;
import java.util.List;
import lombok.Data;

@Data
public class MyPageSummaryDto {
    private String nickname;
    private String email;
    private LocalDate joinDate;
    private int totalDiaryCount;
    private int consecutiveDiaryDays;
    private List<String> mainEmotions;
    private String recentAiComment;
    private String recentStampImage;
    private int commentTime;
} 