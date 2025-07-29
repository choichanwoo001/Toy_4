package com.example.backend.service;

import com.example.backend.entity.Diary;
import com.example.backend.entity.User;
import com.example.backend.entity.UserStampPreference;
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
    private final com.example.backend.repository.UserStampPreferenceRepository userStampPreferenceRepository;

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

    // ===================== NEW METHOD ADDED =====================
    // 2025-01-XX: 일기 스탬프 업데이트 기능 추가
    // 기존 일기의 스탬프만 업데이트하는 메서드
    @Transactional
    public Diary updateDiaryStamp(Long diaryId, String appliedStamp) {
        Diary diary = diaryRepository.findById(diaryId)
            .orElseThrow(() -> new IllegalArgumentException("일기를 찾을 수 없습니다."));
        
        diary.setAppliedStamp(appliedStamp);
        return diaryRepository.save(diary);
    }
    // ===================== END NEW METHOD =====================

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

    // 일기 상세 조회
    @Transactional(readOnly = true)
    public Optional<Diary> getDiaryById(Long diaryId) {
        return diaryRepository.findById(diaryId);
    }

    // ===================== STAMP PREFERENCE METHODS =====================
    // 사용자 스탬프 선택 저장/업데이트
    @Transactional
    public UserStampPreference saveUserStampPreference(Long userId, String stampName, String stampImage) {
        User user = userRepository.findById(userId).orElseThrow(() -> new IllegalArgumentException("User not found"));
        
        // 기존 선택이 있는지 확인
        Optional<UserStampPreference> existingPreference = userStampPreferenceRepository.findByUser(user);
        
        if (existingPreference.isPresent()) {
            // 기존 선택 업데이트
            UserStampPreference preference = existingPreference.get();
            preference.setSelectedStampName(stampName);
            preference.setSelectedStampImage(stampImage);
            return userStampPreferenceRepository.save(preference);
        } else {
            // 새로운 선택 생성
            UserStampPreference newPreference = UserStampPreference.builder()
                .user(user)
                .selectedStampName(stampName)
                .selectedStampImage(stampImage)
                .build();
            return userStampPreferenceRepository.save(newPreference);
        }
    }

    // 사용자 스탬프 선택 조회
    @Transactional(readOnly = true)
    public Optional<UserStampPreference> getUserStampPreference(Long userId) {
        return userStampPreferenceRepository.findByUserUserId(userId);
    }

    // 사용자 스탬프 선택 삭제 (기록 저장 후)
    @Transactional
    public void deleteUserStampPreference(Long userId) {
        Optional<UserStampPreference> preference = userStampPreferenceRepository.findByUserUserId(userId);
        preference.ifPresent(userStampPreferenceRepository::delete);
    }
    // ===================== END STAMP PREFERENCE METHODS =====================
} 