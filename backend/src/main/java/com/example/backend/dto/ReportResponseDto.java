package com.example.backend.dto;

import lombok.Builder;
import lombok.Getter;

import java.util.List;

@Getter
@Builder
public class ReportResponseDto {
    private String week; // 2025년 7월 2주차
    private String emotionSummary;
    private String keywords;
    private List<String> evidenceSentences;
    private List<RecommendationDto> recommendations;
    private List<String> dayLabels;
    private List<EmotionChartDto> emotionCharts;

    @Getter
    @Builder
    public static class RecommendationDto {
        private String title;
        private String description;
    }
}
