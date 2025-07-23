package com.example.backend.service;

import com.example.backend.dto.EmotionChartDto;
import com.example.backend.dto.ReportResponseDto;
import com.example.backend.entity.WeeklyFeedback;
import com.example.backend.repository.WeeklyFeedbackRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalAdjusters;
import java.time.temporal.WeekFields;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class WeeklyReportService {

    private final WeeklyFeedbackRepository feedbackRepository;

    public ReportResponseDto getWeeklyReport(Long userId, int weekOffset) {
        // ✅ JS 기준 맞춤: offset 방향 통일
        LocalDate targetDate = LocalDate.now().plusWeeks(-weekOffset);
        Optional<WeeklyFeedback> optional = feedbackRepository.findByUser_UserIdAndWeekOffset(userId, weekOffset);

        if (optional.isEmpty()) {
            return new ReportResponseDto(); // 빈 DTO 반환
        };

        WeeklyFeedback feedback = optional.get();

        return ReportResponseDto.builder()
                .week(formatWeekString(LocalDate.parse(feedback.getFeedbackStart())))
                .emotionSummary(feedback.getEmotionSummary())
                .keywords("#감정키워드")
                .evidenceSentences(feedback.getFeedbackProofs().stream().map(fp -> fp.getDetail()).toList())
                .recommendations(feedback.getRecommendActivities().stream()
                        .map(a -> ReportResponseDto.RecommendationDto.builder()
                                .title(a.getTitle())
                                .description(a.getDetail())
                                .build())
                        .toList())
                .dayLabels(List.of("월", "화", "수", "목", "금", "토", "일"))
                .emotionCharts(getDummyChart())
                .build();
    }

    // 주차 문자열 생성 유틸
    public String formatWeekString(LocalDate monday) {
        YearMonth ym = YearMonth.of(monday.getYear(), monday.getMonthValue());

        // 이번 달의 첫 번째 월요일
        LocalDate firstMonday = monday.withDayOfMonth(1).with(TemporalAdjusters.nextOrSame(DayOfWeek.MONDAY));

        // 몇 번째 주인지 계산
        long weekOfMonth = ChronoUnit.WEEKS.between(firstMonday, monday) + 1;

        LocalDate sunday = monday.with(DayOfWeek.SUNDAY);

        return String.format(
                "%d년 %d월 %d주차 (%d월 %d일 ~ %d월 %d일)",
                monday.getYear(), monday.getMonthValue(), weekOfMonth,
                monday.getMonthValue(), monday.getDayOfMonth(),
                sunday.getMonthValue(), sunday.getDayOfMonth()
        );
    }

    // 차트는 아직 미구현 -> 임시 데이터
    private List<EmotionChartDto> getDummyChart() {
        return List.of(
                new EmotionChartDto("기쁨", List.of(4, 5, 6, 4, 5, 6, 5), "#DA983C", "rgba(218, 152, 60, 0.2)"),
                new EmotionChartDto("불안", List.of(1, 2, 1, 1, 2, 1, 1), "#B87B5C", "rgba(184, 123, 92, 0.2)")
        );
    }

    public List<WeeklyFeedback> getAllFeedbacks(Long userId) {
        return feedbackRepository.findAllByUser_UserId(userId);
    }
}
