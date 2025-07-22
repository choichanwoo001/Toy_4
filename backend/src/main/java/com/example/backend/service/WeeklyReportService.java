package com.example.backend.service;

import com.example.backend.dto.EmotionChartDto;
import com.example.backend.dto.ReportResponseDto;
import com.example.backend.entity.WeeklyFeedback;
import com.example.backend.repository.WeeklyFeedbackRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.WeekFields;
import java.util.List;
import java.util.Locale;

@Service
@RequiredArgsConstructor
public class WeeklyReportService {

    private final WeeklyFeedbackRepository feedbackRepository;

    public ReportResponseDto getWeeklyReport(Long userId, int weekOffset) {
        // weekOffset 기반 몇주차인지 계산
        LocalDate today = LocalDate.now().minusWeeks(weekOffset);
        LocalDate monday = today.with(DayOfWeek.MONDAY);
        LocalDate sunday = today.with(DayOfWeek.SUNDAY);

        String start = monday.toString();
        String end = sunday.toString();

        // DB 조회
        WeeklyFeedback feedback = feedbackRepository
                .findByUser_UserIdAndFeedbackStartAndFeedbackEnd(userId, start, end)
                .orElseThrow(() -> new RuntimeException("해당 주차의 리포트가 없습니다."));

        // 연관 데이터 포함한 dto 생성
        return ReportResponseDto.builder()
                .week(formatWeekString(monday))
                .emotionSummary(feedback.getEmotionSummary())
                .keywords("#감정키워드") // ToDo: 감정 키워드 넣기
                .evidenceSentences(
                        feedback.getFeedbackProofs().stream()
                                .map(fp -> fp.getDetail())
                                .toList()
                )
                .recommendations(
                        feedback.getRecommendActivities().stream()
                                .map(a -> ReportResponseDto.RecommendationDto.builder()
                                        .title(a.getTitle())
                                        .description(a.getDetail())
                                        .build())
                                .toList()
                )
                .dayLabels(List.of("월", "화", "수", "목", "금", "토", "일"))
                .emotionCharts(getDummyChart())
                .build();
    }

    // 주차 문자열 생성 유틸
    private String formatWeekString(LocalDate monday) {
        int weekOfMoth = monday.get(WeekFields.of(Locale.KOREA).weekOfMonth());
        return String.format("%d년 %d월 %d주차", monday.getYear(), monday.getMonthValue(), weekOfMoth);
    }

    // 차트는 아직 미구현 -> 임시 데이터
    private List<EmotionChartDto> getDummyChart() {
        return List.of(
                new EmotionChartDto("기쁨", List.of(4, 5, 6, 4, 5, 6, 5), "#DA983C", "rgba(218, 152, 60, 0.2)"),
                new EmotionChartDto("불안", List.of(1, 2, 1, 1, 2, 1, 1), "#B87B5C", "rgba(184, 123, 92, 0.2)")
        );
    }
}
