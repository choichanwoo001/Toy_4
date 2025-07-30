package com.example.backend.service;

import com.example.backend.entity.Diary;
import com.example.backend.entity.User;
import com.example.backend.entity.DailyComment;
import com.example.backend.entity.UserStamp;
import com.example.backend.dto.UserStampDto;
import com.example.backend.repository.DiaryRepository;
import com.example.backend.repository.UserRepository;
import com.example.backend.repository.DailyCommentRepository;
import com.example.backend.repository.UserStampRepository;
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
    private final UserStampRepository userStampRepository;
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

    // ===================== NEW DAILY COMMENT METHOD =====================
    // 2025-01-XX: 일별 코멘트 저장 기능 추가
    // 코멘트 저장 시 현재 적용중인 스탬프 정보도 함께 저장
    @Transactional
    public DailyComment saveDailyComment(Long userId, String content, LocalDateTime diaryDate) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        
        // 현재 적용중인 스탬프 정보 가져오기
        UserStampDto activeStamp = pointshopService.getActiveStamp(userId);
        UserStamp userStamp = null;
        
        if (activeStamp != null) {
            userStamp = userStampRepository.findById(activeStamp.getUserStampId()).orElse(null);
        }
        
        DailyComment comment = new DailyComment();
        comment.setUser(user);
        comment.setContent(content);
        comment.setDiaryDate(diaryDate);
        comment.setCreatedAt(LocalDateTime.now());
        comment.setUserStamp(userStamp); // 현재 적용중인 스탬프 설정
        
        return dailyCommentRepository.save(comment);
    }
    // ===================== END NEW DAILY COMMENT METHOD =====================

    // ===================== NEW CALENDAR DATA METHOD =====================
    // 2025-01-XX: 달력 조회를 위한 통합 데이터 조회 메서드 추가
    // 일기와 코멘트(스탬프 포함) 정보를 함께 조회
    @Transactional(readOnly = true)
    public Map<String, Object> getCalendarData(Long userId, int year, int month) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        
        // 월별 일기 조회
        List<Diary> diaries = getDiariesByUserAndMonth(userId, year, month);
        
        // 월별 코멘트 조회 (스탬프 정보 포함)
        List<DailyComment> comments = dailyCommentRepository.findByUserAndYearMonthWithStamp(userId, year, month);
        
        // 기존 코멘트들에 기본 스탬프 정보 추가
        for (DailyComment comment : comments) {
            if (comment.getUserStamp() == null) {
                // 기본 스탬프 더미 데이터 생성
                UserStamp defaultStamp = createDefaultStamp();
                comment.setUserStamp(defaultStamp);
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
    // ===================== END NEW CALENDAR DATA METHOD =====================

    // ===================== NEW DEFAULT STAMP METHOD =====================
    // 2025-01-XX: 기본 스탬프 더미 데이터 생성 메서드 추가
    // 기존 코멘트들에 기본 스탬프 정보를 제공하기 위한 메서드
    private UserStamp createDefaultStamp() {
        UserStamp defaultStamp = new UserStamp();
        defaultStamp.setUserStampId(-1L); // 더미 ID
        defaultStamp.setUserId(1L); // 더미 사용자 ID
        defaultStamp.setStampId(1L); // 기본 스탬프 ID
        defaultStamp.setIsActive("Y");
        defaultStamp.setCreatedAt(LocalDateTime.now());
        defaultStamp.setUpdatedAt(LocalDateTime.now());
        
        // Stamp 엔티티 정보도 설정 (프론트엔드에서 사용)
        try {
            // Stamp 정보를 가져오기 위해 StampRepository 주입이 필요하지만,
            // 현재는 더미 데이터로 처리
            // 실제로는 Stamp 엔티티를 별도로 생성하거나 다른 방법 사용
        } catch (Exception e) {
            // 더미 데이터이므로 예외 무시
        }
        
        return defaultStamp;
    }
    // ===================== END NEW DEFAULT STAMP METHOD =====================

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
            commentData.put("userStamp", comment.getUserStamp());
            result.add(commentData);
        }
        
        return result;
    }
    // ===================== END DEBUG METHOD =====================

    // ===================== DUMMY DATA METHOD =====================
    // 2025-01-XX: 테스트를 위한 더미 데이터 생성 메서드 추가
    @Transactional
    public Map<String, Object> createDummyData(Long userId) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        
        // 2024년 12월 26, 27, 28, 29일에 AI 코멘트만 생성 (스탬프 포함)
        List<DailyComment> createdComments = new ArrayList<>();
        for (int day = 26; day <= 29; day++) {
            // 임시 일기 생성 (DailyComment에 연결하기 위해)
            Diary tempDiary = new Diary();
            tempDiary.setUser(user);
            tempDiary.setCreatedAt(LocalDateTime.of(2024, 12, day, 10, 0));
            tempDiary.setContent("2024년 12월 " + day + "일의 임시 일기입니다.");
            tempDiary.setEmotion("😊");
            tempDiary.setAppliedStamp(null); // 임시 필드
            Diary savedDiary = diaryRepository.save(tempDiary);
            
            // AI 코멘트 생성
            DailyComment comment = new DailyComment();
            comment.setUser(user);
            comment.setDiary(savedDiary); // 일기 연결
            comment.setDiaryDate(LocalDateTime.of(2024, 12, day, 15, 0));
            comment.setContent("2024년 12월 " + day + "일의 AI 코멘트입니다. 정말 잘하셨어요!");
            comment.setCreatedAt(LocalDateTime.of(2024, 12, day, 15, 0));
            
            // 기본 스탬프 설정 (더미)
            UserStamp dummyStamp = createDefaultStamp();
            comment.setUserStamp(dummyStamp);
            
            createdComments.add(dailyCommentRepository.save(comment));
        }
        
        Map<String, Object> result = new HashMap<>();
        result.put("comments", createdComments.size());
        result.put("message", "daily_comment 테이블에 더미 데이터가 성공적으로 생성되었습니다.");
        
        return result;
    }
    // ===================== END DUMMY DATA METHOD =====================

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
} 