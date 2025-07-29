package com.example.backend.service;

import com.example.backend.dto.EmotionChartDto;
import com.example.backend.dto.ReportResponseDto;
import com.example.backend.entity.Diary;
import com.example.backend.entity.WeeklyFeedback;
import com.example.backend.repository.DiaryRepository;
import com.example.backend.repository.WeeklyFeedbackRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.TemporalAdjusters;
import java.util.*;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class WeeklyReportService {

    private final WeeklyFeedbackRepository feedbackRepository;
    private final DiaryRepository diaryRepository;

    // 주차별 감정 리포트 weekOffset: 현재로부터 몇 주 전인지(0=이번주)
    @Transactional(readOnly = true)
    public ReportResponseDto getWeeklyReport(Long userId, int weekOffset) {
        System.out.println("🔍 getWeeklyReport 호출 - userId: " + userId + ", weekOffset: " + weekOffset);
        
        // 해당 주차의 시작일과 종료일 계산
        LocalDate targetDate = LocalDate.now().plusWeeks(-weekOffset);
        LocalDate monday = targetDate.with(TemporalAdjusters.previousOrSame(DayOfWeek.MONDAY));
        LocalDate sunday = monday.plusDays(6);
        
        System.out.println("📅 주차 계산 - monday: " + monday + ", sunday: " + sunday);

        // 해당 주차의 일기 데이터 조회
        List<Diary> diaries = diaryRepository.findByUser_UserIdAndCreatedAtBetween(
            userId, 
            monday.atStartOfDay(), 
            sunday.atTime(23, 59, 59)
        );
        
        System.out.println("📝 조회된 일기 개수: " + diaries.size());
        for (Diary diary : diaries) {
            System.out.println("  - 일기: " + diary.getContent() + " (감정: " + diary.getEmotion() + ")");
        }

        // 주간 피드백 데이터 조회 (있는 경우)
        Optional<WeeklyFeedback> optional = feedbackRepository.findByUser_UserIdAndWeekOffset(userId, weekOffset);

        // 감정 차트 데이터 생성
        List<EmotionChartDto> emotionCharts = getEmotionChartsFromDiaries(diaries);

        // 기본 리포트 데이터 생성
        var builder = ReportResponseDto.builder()
                .week(formatWeekString(monday))
                .dayLabels(List.of("월", "화", "수", "목", "금", "토", "일"))
                .emotionCharts(emotionCharts);

        // 주간 피드백이 있는 경우 추가 데이터 설정
        if (optional.isPresent()) {
            WeeklyFeedback feedback = optional.get();
            builder.emotionSummary(feedback.getEmotionSummary())
                    .evidenceSentences(feedback.getFeedbackProofs().stream()
                            .map(fp -> fp.getDetail())
                            .toList())
                    .recommendations(feedback.getRecommendActivities().stream()
                            .map(a -> ReportResponseDto.RecommendationDto.builder()
                                    .title(a.getTitle())
                                    .description(a.getDetail())
                                    .build())
                            .toList());
        } else {
            // 피드백이 없는 경우 기본값 설정
            builder.emotionSummary("이번 주 감정 분석이 준비되지 않았습니다.")
                    .evidenceSentences(List.of())
                    .recommendations(List.of());
        }

        return builder.build();
    }

    // 주차 문자열 생성 유틸
    public String formatWeekString(LocalDate monday) {
        LocalDate sunday = monday.plusDays(6);
        return String.format(
                "%d년 %d월 %d일 ~ %d월 %d일",
                monday.getYear(), monday.getMonthValue(), monday.getDayOfMonth(),
                sunday.getMonthValue(), sunday.getDayOfMonth()
        );
    }

    // 일기 데이터에서 감정 차트 데이터 생성
    private List<EmotionChartDto> getEmotionChartsFromDiaries(List<Diary> diaries) {
        System.out.println("🎨 감정 차트 데이터 생성 시작 - 일기 개수: " + diaries.size());
        
        // 1. 감정별 요일 카운트 계산
        Map<String, int[]> emotionCounts = new HashMap<>();
        
        for (Diary diary : diaries) {
            if (diary.getEmotion() != null && !diary.getEmotion().trim().isEmpty()) {
                String emotion = diary.getEmotion();
                LocalDate diaryDate = diary.getCreatedAt().toLocalDate();
                int dayIndex = diaryDate.getDayOfWeek().getValue() - 1; // 월요일=0, 일요일=6
                
                emotionCounts.putIfAbsent(emotion, new int[7]);
                emotionCounts.get(emotion)[dayIndex]++;
                
                System.out.println("  📊 감정: " + emotion + ", 요일: " + diaryDate.getDayOfWeek() + ", 인덱스: " + dayIndex);
            }
        }

        System.out.println("📈 감정별 카운트: " + emotionCounts);

        // 2. 감정별 총합으로 정렬 후 상위 4개만 추출
        List<Map.Entry<String, int[]>> topEmotions = emotionCounts.entrySet().stream()
                .sorted((e1, e2) -> {
                    int sum1 = Arrays.stream(e1.getValue()).sum();
                    int sum2 = Arrays.stream(e2.getValue()).sum();
                    return Integer.compare(sum2, sum1); // 내림차순
                })
                .limit(4)
                .toList();

        // 3. 색상 배정
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

        // 디버깅용 로그
        System.out.println("✅ 생성된 감정 차트 개수: " + result.size());
        for (EmotionChartDto chart : result) {
            System.out.println("  📊 감정: " + chart.getEmotionLabel() + ", 데이터: " + chart.getEmotionData());
        }

        return result;
    }

    // 모든 주간 피드백 반환
    @Transactional(readOnly = true)
    public List<WeeklyFeedback> getAllFeedbacks(Long userId) {
        return feedbackRepository.findAllByUser_UserId(userId);
    }
}
