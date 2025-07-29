package com.example.backend.service;

import com.example.backend.entity.Diary;
import com.example.backend.entity.User;
import com.example.backend.repository.DiaryRepository;
import com.example.backend.repository.UserRepository;
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

    // ===================== NEW METHOD ADDED =====================
    // 2025-01-XX: 감정 표현 기능 추가를 위한 새로운 일기 저장 메서드
    // 기존 saveDiary 메서드를 확장하여 emotion 파라미터를 추가로 받음
    // 일기 저장 (감정 포함)
    @Transactional
    public Diary saveDiary(Long userId, String content, String appliedStamp, String emotion) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        Diary diary = new Diary();
        diary.setUser(user);
        diary.setCreatedAt(LocalDateTime.now());
        diary.setContent(content);
        diary.setAppliedStamp(appliedStamp);
        diary.setEmotion(emotion); // 새로운 emotion 필드 설정
        return diaryRepository.save(diary);
    }
    // ===================== END NEW METHOD =====================

    // ===================== COMPATIBILITY METHOD =====================
    // 2025-01-XX: 기존 코드 호환성을 위한 오버로드 메서드 추가
    // 기존 saveDiary 메서드 호출 시 emotion은 null로 설정됨
    @Transactional
    public Diary saveDiary(Long userId, String content, String appliedStamp) {
        return saveDiary(userId, content, appliedStamp, null);
    }
    // ===================== END COMPATIBILITY METHOD =====================

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