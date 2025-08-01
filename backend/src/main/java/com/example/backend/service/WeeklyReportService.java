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
import java.time.temporal.WeekFields;
import java.util.*;
import java.util.stream.Collectors;
import com.example.backend.entity.FeedbackProof;
import com.example.backend.entity.RecommendActivity;
import java.time.temporal.ChronoUnit;

@Service
@RequiredArgsConstructor
public class WeeklyReportService {

    private final WeeklyFeedbackRepository feedbackRepository;
    private final DiaryRepository diaryRepository;

    // 주차별 감정 리포트 weekOffset: 현재로부터 몇 주 전인지(0=이번주)
    @Transactional(readOnly = true)
    public ReportResponseDto getWeeklyReport(Long userId, int weekOffset) {
        try {
            System.out.println("🔍 getWeeklyReport 호출 - userId: " + userId + ", weekOffset: " + weekOffset);

        /* 단계 1: 주간 피드백 먼저 조회해서 날짜 범위를 확정 */
        Optional<WeeklyFeedback> optionalFeedback = feedbackRepository.findByUser_UserIdAndWeekOffsetWithDetails(userId, weekOffset);

        LocalDate monday;
        LocalDate sunday;

        if (optionalFeedback.isPresent()) {
            // 주간 피드백의 시작/종료일(yyyy-MM-dd 형태)을 기준으로 범위를 계산
            WeeklyFeedback feedback = optionalFeedback.get();
            monday = LocalDate.parse(feedback.getFeedbackStart());
            sunday = LocalDate.parse(feedback.getFeedbackEnd());
            System.out.println("📅 주간 피드백 기준 날짜 사용 - monday: " + monday + ", sunday: " + sunday);
        } else {
            // 피드백이 없는 경우 기존 로직 유지 (현재 날짜 기준)
            LocalDate targetDate;
            if (weekOffset >= 0) {
                // 과거 날짜 (현재로부터 몇 주 전)
                targetDate = LocalDate.now().plusWeeks(-weekOffset);
            } else {
                // 미래 날짜 (현재로부터 몇 주 후)
                targetDate = LocalDate.now().plusWeeks(Math.abs(weekOffset));
            }
            monday = targetDate.with(TemporalAdjusters.previousOrSame(DayOfWeek.MONDAY));
            sunday = monday.plusDays(6);
            System.out.println("📅 피드백 없음, 기본 날짜 계산 - monday: " + monday + ", sunday: " + sunday);
        }

        /* 단계 2: 기간에 해당하는 일기 조회 */
        List<Diary> diaries = diaryRepository.findByUser_UserIdAndCreatedAtBetween(
                userId,
                monday.atStartOfDay(),
                sunday.atTime(23, 59, 59)
        );
        System.out.println("📝 조회된 일기 개수: " + diaries.size());

        /* 단계 3: 감정 차트 생성 */
        List<EmotionChartDto> emotionCharts = getEmotionChartsFromDiaries(diaries);

        /* 단계 4: 응답 빌드 */
        var builder = ReportResponseDto.builder()
                .dayLabels(List.of("월", "화", "수", "목", "금", "토", "일"))
                .emotionCharts(emotionCharts);

            if (optionalFeedback.isPresent()) {
                WeeklyFeedback feedback = optionalFeedback.get();
                
                // MultipleBagFetchException 해결을 위해 별도 쿼리로 컬렉션 로드
                Optional<WeeklyFeedback> feedbackWithProofs = feedbackRepository.findWithFeedbackProofs(userId, weekOffset);
                Optional<WeeklyFeedback> feedbackWithActivities = feedbackRepository.findWithRecommendActivities(userId, weekOffset);
                
                // 컬렉션 데이터를 기본 feedback 객체에 설정 (중복 제거)
                if (feedbackWithProofs.isPresent()) {
                    // 기존 데이터와 새 데이터를 합치고 중복 제거
                    Set<FeedbackProof> uniqueProofs = new LinkedHashSet<>(feedback.getFeedbackProofs());
                    uniqueProofs.addAll(feedbackWithProofs.get().getFeedbackProofs());
                    feedback.getFeedbackProofs().clear();
                    feedback.getFeedbackProofs().addAll(uniqueProofs);
                }
                if (feedbackWithActivities.isPresent()) {
                    // 기존 데이터와 새 데이터를 합치고 중복 제거
                    Set<RecommendActivity> uniqueActivities = new LinkedHashSet<>(feedback.getRecommendActivities());
                    uniqueActivities.addAll(feedbackWithActivities.get().getRecommendActivities());
                    feedback.getRecommendActivities().clear();
                    feedback.getRecommendActivities().addAll(uniqueActivities);
                }
                
                System.out.println("🔍 FeedbackProof 개수: " + feedback.getFeedbackProofs().size());
                System.out.println("🔍 RecommendActivity 개수: " + feedback.getRecommendActivities().size());
                
                // 피드백이 있을 때는 피드백의 실제 날짜를 사용하여 주차 문자열 생성
                LocalDate feedbackMonday = LocalDate.parse(feedback.getFeedbackStart());
                builder.week(formatWeekString(feedbackMonday))
                        .emotionSummary(feedback.getEmotionSummary())
                        .evidenceSentences(feedback.getFeedbackProofs().stream()
                                .map(FeedbackProof::getDetail)
                                .toList())
                        .recommendations(feedback.getRecommendActivities().stream()
                                .map(a -> ReportResponseDto.RecommendationDto.builder()
                                        .title(a.getTitle())
                                        .description(a.getDetail())
                                        .build())
                                .toList());
            } else {
                // 피드백이 없을 때만 계산된 날짜 사용
                builder.week(formatWeekString(monday))
                        .emotionSummary("이번 주 감정 분석이 준비되지 않았습니다.")
                        .evidenceSentences(List.of())
                        .recommendations(List.of());
            }

            return builder.build();
        } catch (Exception e) {
            System.err.println("❌ getWeeklyReport 에러: " + e.getMessage());
            e.printStackTrace();
            throw e;
        }
    }

    // 주차 문자열 생성 유틸
    private String formatWeekString(LocalDate monday) {
        LocalDate sunday = monday.plusDays(6);
        
        // 목요일 기준으로 주차가 속한 월 결정 (ISO 8601)
        LocalDate thursday = monday.plusDays(3);
        
        // 한국 기준 주차 계산 (월요일 시작)
        WeekFields weekFields = WeekFields.of(DayOfWeek.MONDAY, 4);
        int weekOfMonth = thursday.get(weekFields.weekOfMonth());
        int year = thursday.getYear();
        int month = thursday.getMonthValue();
        
        return String.format("%d년 %d월 %d주차 (%d월 %d일 ~ %d월 %d일)",
                year,
                month,
                weekOfMonth,
                monday.getMonthValue(),
                monday.getDayOfMonth(),
                sunday.getMonthValue(),
                sunday.getDayOfMonth());
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
