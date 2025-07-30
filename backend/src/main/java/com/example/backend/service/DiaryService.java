package com.example.backend.service;

import com.example.backend.entity.Diary;
import com.example.backend.entity.User;
import com.example.backend.entity.DailyComment;
import com.example.backend.entity.UserStampPreference;
import com.example.backend.dto.UserStampDto;
import com.example.backend.repository.DiaryRepository;
import com.example.backend.repository.UserRepository;
import com.example.backend.repository.DailyCommentRepository;
import com.example.backend.repository.UserStampPreferenceRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.YearMonth;
import java.util.*;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class DiaryService {
    private final DiaryRepository diaryRepository;
    private final UserRepository userRepository;
    private final DailyCommentRepository dailyCommentRepository;
    private final UserStampPreferenceRepository userStampPreferenceRepository;
    private final PointshopService pointshopService;

    // ===================== NEW METHOD ADDED =====================
    // 2025-01-XX: 감정 표현 기능 추가를 위한 새로운 일기 저장 메서드
    // 일기 저장 (감정 포함)
    @Transactional
    public Diary saveDiary(Long userId, String content, String emotion) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        Diary diary = new Diary();
        diary.setUser(user);
        diary.setCreatedAt(LocalDateTime.now());
        diary.setContent(content);
        diary.setEmotion(emotion); // 새로운 emotion 필드 설정
        return diaryRepository.save(diary);
    }
    // ===================== END NEW METHOD =====================

    // ===================== COMPATIBILITY METHOD =====================
    // 2025-01-XX: 기존 코드 호환성을 위한 오버로드 메서드 추가
    // 기존 saveDiary 메서드 호출 시 emotion은 null로 설정됨
    @Transactional
    public Diary saveDiary(Long userId, String content) {
        return saveDiary(userId, content, null);
    }
    // ===================== END COMPATIBILITY METHOD =====================

    // ===================== UPDATED DAILY COMMENT METHOD =====================
    // 2025-01-XX: 일별 코멘트 저장 기능 수정
    // 코멘트 저장 시 현재 적용중인 스탬프 선호도 정보도 함께 저장
    @Transactional
    public DailyComment saveDailyComment(Long userId, String content, LocalDateTime diaryDate) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        
        // 현재 적용중인 스탬프 선호도 정보 가져오기
        UserStampDto activeStamp = pointshopService.getActiveStamp(userId);
        UserStampPreference userStampPreference = null;
        
        if (activeStamp != null) {
            // UserStampPreference에서 해당 사용자의 현재 활성 스탬프 찾기
            userStampPreference = userStampPreferenceRepository.findByUser_UserIdAndSelectedStampName(
                userId, activeStamp.getStampName()
            ).orElse(null);
        }
        
        DailyComment comment = new DailyComment();
        comment.setUser(user);
        comment.setContent(content);
        comment.setDiaryDate(diaryDate);
        comment.setCreatedAt(LocalDateTime.now());
        comment.setUserStampPreference(userStampPreference); // 현재 적용중인 스탬프 선호도 설정
        
        return dailyCommentRepository.save(comment);
    }
    // ===================== END UPDATED DAILY COMMENT METHOD =====================

    // ===================== UPDATED CALENDAR DATA METHOD =====================
    // 2025-01-XX: 달력 조회를 위한 통합 데이터 조회 메서드 수정
    // 일기와 코멘트(UserStampPreference 포함) 정보를 함께 조회
    @Transactional(readOnly = true)
    public Map<String, Object> getCalendarData(Long userId, int year, int month) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        
        // 월별 일기 조회
        List<Diary> diaries = getDiariesByUserAndMonth(userId, year, month);
        
        // 월별 코멘트 조회 (UserStampPreference 정보 포함)
        List<DailyComment> comments = dailyCommentRepository.findByUserAndYearMonthWithStampPreference(userId, year, month);
        
        // 기존 코멘트들에 기본 스탬프 정보 추가
        for (DailyComment comment : comments) {
            if (comment.getUserStampPreference() == null) {
                // 기본 스탬프 정보 설정
                UserStampPreference defaultStamp = new UserStampPreference();
                defaultStamp.setPreferenceId(-1L);
                defaultStamp.setUser(userRepository.findById(1L).orElse(null));
                defaultStamp.setSelectedStampName("참잘했어요");
                defaultStamp.setSelectedStampImage("image/default_stamp.png");
                defaultStamp.setCreatedAt(LocalDateTime.now());
                defaultStamp.setUpdatedAt(LocalDateTime.now());
                comment.setUserStampPreference(defaultStamp);
            }
        }
        
        // 결과 맵 생성
        Map<String, Object> result = new HashMap<>();
        result.put("diaries", diaries);
        result.put("comments", comments);
        result.put("year", year);
        result.put("month", month);
        
        return result;
    }
    // ===================== END UPDATED CALENDAR DATA METHOD =====================



    // ===================== DEBUG METHOD =====================
    // 2025-01-XX: 디버깅을 위한 모든 코멘트 조회 메서드 추가
    @Transactional(readOnly = true)
    public List<Map<String, Object>> getAllCommentsForDebug(Long userId) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        List<DailyComment> comments = dailyCommentRepository.findByUser_UserIdAndDiaryDateBetween(
            userId, 
            LocalDateTime.of(2020, 1, 1, 0, 0), 
            LocalDateTime.of(2030, 12, 31, 23, 59)
        );
        
        List<Map<String, Object>> result = new ArrayList<>();
        for (DailyComment comment : comments) {
            Map<String, Object> commentData = new HashMap<>();
            commentData.put("id", comment.getId());
            commentData.put("content", comment.getContent());
            commentData.put("diaryDate", comment.getDiaryDate());
            commentData.put("createdAt", comment.getCreatedAt());
            commentData.put("userStampPreference", comment.getUserStampPreference());
            result.add(commentData);
        }
        
        return result;
    }
    // ===================== END DEBUG METHOD =====================



    // 유저별, 월별 일기 목록 조회
    @Transactional(readOnly = true)
    public List<Diary> getDiariesByUserAndMonth(Long userId, int year, int month) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        LocalDate start = YearMonth.of(year, month).atDay(1);
        LocalDate end = YearMonth.of(year, month).atEndOfMonth();
        LocalDateTime startDateTime = start.atStartOfDay();
        LocalDateTime endDateTime = end.atTime(23,59,59);
        return diaryRepository.findByUserAndCreatedAtBetween(user, startDateTime, endDateTime);
    }

    // ===================== NEW EMOTION STATS METHOD =====================
    // 2025-01-XX: 월별 감정 통계 기능 추가
    // 유저별, 월별 감정 통계 조회 - 상위 3개 감정 반환
    @Transactional(readOnly = true)
    public Map<String, Object> getEmotionStatsByUserAndMonth(Long userId, int year, int month) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        LocalDate start = YearMonth.of(year, month).atDay(1);
        LocalDate end = YearMonth.of(year, month).atEndOfMonth();
        LocalDateTime startDateTime = start.atStartOfDay();
        LocalDateTime endDateTime = end.atTime(23,59,59);
        
        List<Diary> diaries = diaryRepository.findByUserAndCreatedAtBetween(user, startDateTime, endDateTime);
        
        // 감정별 카운트 계산
        Map<String, Long> emotionCounts = diaries.stream()
                .filter(diary -> diary.getEmotion() != null && !diary.getEmotion().trim().isEmpty())
                .collect(Collectors.groupingBy(
                    Diary::getEmotion,
                    Collectors.counting()
                ));
        
        // 상위 3개 감정 추출
        List<Map<String, Object>> topEmotions = emotionCounts.entrySet().stream()
                .sorted(Map.Entry.<String, Long>comparingByValue().reversed())
                .limit(3)
                .map(entry -> {
                    Map<String, Object> emotionData = new HashMap<>();
                    emotionData.put("emotion", entry.getKey());
                    emotionData.put("count", entry.getValue());
                    return emotionData;
                })
                .collect(Collectors.toList());
        
        // 결과 맵 생성
        Map<String, Object> result = new HashMap<>();
        result.put("topEmotions", topEmotions);
        result.put("totalEmotions", emotionCounts.size());
        result.put("totalDiaries", diaries.size());
        result.put("year", year);
        result.put("month", month);
        
        return result;
    }
    // ===================== END NEW EMOTION STATS METHOD =====================

    // ===================== NEW METHOD ADDED =====================
    // 2025-01-XX: 오늘의 모든 기록을 가져오는 메서드 추가
    // 오늘의 모든 기록 조회
    @Transactional(readOnly = true)
    public List<Diary> getTodayDiaries(Long userId) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        
        // 오늘 날짜의 시작과 끝 시간 설정
        LocalDate today = LocalDate.now();
        LocalDateTime startOfDay = today.atStartOfDay();
        LocalDateTime endOfDay = today.atTime(23, 59, 59);
        
        return diaryRepository.findByUserAndCreatedAtBetween(user, startOfDay, endOfDay);
    }
    // ===================== END NEW METHOD =====================

    // 일기 상세 조회
    @Transactional(readOnly = true)
    public Optional<Diary> getDiaryById(Long diaryId) {
        return diaryRepository.findById(diaryId);
    }

    // ===================== NEW DAILY COMMENT BY DATE METHOD =====================
    // 2025-01-XX: 특정 날짜의 DailyComment 조회 기능 추가
    // 과거 날짜의 AI 코멘트를 조회하기 위한 메서드
    @Transactional(readOnly = true)
    public Optional<DailyComment> getDailyCommentByDate(Long userId, int year, int month, int day) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        
        // 해당 날짜의 시작과 끝 시간 설정
        LocalDateTime startOfDay = LocalDateTime.of(year, month, day, 0, 0, 0);
        LocalDateTime endOfDay = LocalDateTime.of(year, month, day, 23, 59, 59);
        
        // 해당 날짜의 DailyComment 조회
        List<DailyComment> comments = dailyCommentRepository.findByUser_UserIdAndDiaryDateBetween(
            userId, startOfDay, endOfDay
        );
        
        // 가장 최근 코멘트 반환 (여러 개가 있을 경우)
        return comments.stream()
                .max(Comparator.comparing(DailyComment::getCreatedAt));
    }
    // ===================== END NEW DAILY COMMENT BY DATE METHOD =====================
} 