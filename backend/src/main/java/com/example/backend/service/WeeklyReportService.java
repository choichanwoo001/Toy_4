package com.example.backend.service;

import com.example.backend.dto.EmotionChartDto;
import com.example.backend.dto.ReportResponseDto;
import com.example.backend.entity.CommentEmotionMapping;
import com.example.backend.entity.DailyComment;
import com.example.backend.entity.WeeklyFeedback;
import com.example.backend.repository.CommentEmotionMappingRepository;
import com.example.backend.repository.DailyCommentRepository;
import com.example.backend.repository.WeeklyFeedbackRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalAdjusters;
import java.util.*;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class WeeklyReportService {

    private final WeeklyFeedbackRepository feedbackRepository;
    private final DailyCommentRepository commentRepo;
    private final CommentEmotionMappingRepository mappingRepo;

    // 주차별 감정 리포트 weekOffset: 현재로부터 몇 주 전인지(0=이번주)
    @Transactional(readOnly = true)
    public ReportResponseDto getWeeklyReport(Long userId, int weekOffset) {
        //  JS 기준 맞춤: offset 방향 통일
        LocalDate targetDate = LocalDate.now().plusWeeks(-weekOffset);
        Optional<WeeklyFeedback> optional = feedbackRepository.findByUser_UserIdAndWeekOffset(userId, weekOffset);

        if (optional.isEmpty()) {
            return new ReportResponseDto(); // 빈 DTO 반환
        };

        WeeklyFeedback feedback = optional.get();

        LocalDate monday = LocalDate.parse(feedback.getFeedbackStart());
        LocalDate sunday = LocalDate.parse(feedback.getFeedbackEnd());

        List<DailyComment> comments = commentRepo
                .findByUser_UserIdAndDiaryDateBetween(userId, monday.atStartOfDay(), sunday.atStartOfDay());

        List<CommentEmotionMapping> mappings = mappingRepo.findByDailyCommentIn(comments);

        return ReportResponseDto.builder()
                .week(formatWeekString(LocalDate.parse(feedback.getFeedbackStart())))
                .emotionSummary(feedback.getEmotionSummary())
                .keywords(extractTopEmotionKeywords(mappings, 3)) // 3개만 출력
                .evidenceSentences(feedback.getFeedbackProofs().stream().map(fp -> fp.getDetail()).toList())
                .recommendations(feedback.getRecommendActivities().stream()
                        .map(a -> ReportResponseDto.RecommendationDto.builder()
                                .title(a.getTitle())
                                .description(a.getDetail())
                                .build())
                        .toList())
                .dayLabels(List.of("월", "화", "수", "목", "금", "토", "일"))
                .emotionCharts(getEmotionCharts(mappings))
                .build();
    }

    // 주차 문자열 생성 유틸
    public String formatWeekString(LocalDate monday) {
        // 기준이 되는 일요일을 계산
        LocalDate sunday = monday.with(DayOfWeek.SUNDAY);

        // 해당 달의 첫 일요일
        LocalDate firstSunday = sunday.withDayOfMonth(1).with(TemporalAdjusters.nextOrSame(DayOfWeek.SUNDAY));

        // 몇 번째 주인지 계산 (일요일 기준)
        long weekOfMonth = ChronoUnit.WEEKS.between(firstSunday, sunday) + 1;

        return String.format(
                "%d년 %d월 %d주차 (%d월 %d일 ~ %d월 %d일)",
                sunday.getYear(), sunday.getMonthValue(), weekOfMonth,
                monday.getMonthValue(), monday.getDayOfMonth(),
                sunday.getMonthValue(), sunday.getDayOfMonth()
        );
    }

    // 감정 키워드 추출 (상위 n개)
    private String extractTopEmotionKeywords(List<CommentEmotionMapping> mappings, int topN) {
        Map<String, Integer> emotionCount = new HashMap<>();

        for (CommentEmotionMapping m : mappings) {
            String emotion = m.getEmotionData().getName();
            emotionCount.put(emotion, emotionCount.getOrDefault(emotion, 0) + 1);
        }

        return emotionCount.entrySet().stream()
                .sorted((e1, e2) -> Integer.compare(e2.getValue(), e1.getValue())) // 내림차순 정렬
                .limit(topN)
                .map(e -> "#" + e.getKey())
                .collect(Collectors.joining(" "));
    }

    // 감정 데이터를 요일별로 추출하여 차트용 데이터 구성
    private List<EmotionChartDto> getEmotionCharts(List<CommentEmotionMapping> mappings) {
        // 1. Map<감정, int[7]> : 요일별 카운트
        Map<String, int[]> countMap = new HashMap<>();
        for (CommentEmotionMapping m : mappings) {
            String emotion = m.getEmotionData().getName();
            LocalDate date = m.getDailyComment().getDiaryDate().toLocalDate();
            int dayIndex = date.getDayOfWeek().getValue() - 1;

            countMap.putIfAbsent(emotion, new int[7]);
            countMap.get(emotion)[dayIndex]++;
        }

        // 2. 감정별 총합으로 정렬 후 상위 4개만 추출
        List<Map.Entry<String, int[]>> topEmotions = countMap.entrySet().stream()
                .sorted((e1, e2) -> {
                    int sum1 = Arrays.stream(e1.getValue()).sum();
                    int sum2 = Arrays.stream(e2.getValue()).sum();
                    return Integer.compare(sum2, sum1); // 내림차순
                })
                .limit(4)
                .toList();

        // 3. 동적으로 색상 배정
        List<String> borderColors = List.of("#DA983C", "#B87B5C", "#8F9562", "#6B7280");
        List<String> backgroundColors = List.of(
                "rgba(218, 152, 60, 0.2)",
                "rgba(184, 123, 92, 0.2)",
                "rgba(143, 149, 98, 0.2)",
                "rgba(107, 114, 128, 0.2)"
        );

        List<EmotionChartDto> result = new ArrayList<>();
        for (int i = 0; i < topEmotions.size(); i++) {
            String emotion = topEmotions.get(i).getKey();
            List<Integer> data = Arrays.stream(topEmotions.get(i).getValue()).boxed().toList();
            result.add(new EmotionChartDto(
                    emotion,
                    data,
                    borderColors.get(i % borderColors.size()),
                    backgroundColors.get(i % backgroundColors.size())
            ));
        }

        return result;
    }

    // 모든 주간 피드백 반환
    @Transactional(readOnly = true)
    public List<WeeklyFeedback> getAllFeedbacks(Long userId) {
        return feedbackRepository.findAllByUser_UserId(userId);
    }
}
