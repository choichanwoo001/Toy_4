package com.example.backend.controller;

import com.example.backend.entity.Diary;
import com.example.backend.service.DiaryService;
import com.example.backend.dto.ApiResponse;
import com.example.backend.entity.User;
import com.example.backend.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import jakarta.servlet.http.HttpSession;

@Controller
public class DiaryController {
    @Autowired
    private DiaryService diaryService;
    @Autowired
    private UserRepository userRepository;

    // ===================== REST API =====================

    // ===================== UPDATED API ENDPOINT =====================
    // 2025-01-XX: 감정 표현 기능 추가를 위한 API 엔드포인트 수정
    // 기존 일기 저장 API에 emotion 파라미터 추가 (선택사항)
    // 일기 저장 (REST) - 감정 포함
    @PostMapping("/api/diaries")
    @ResponseBody
    public ResponseEntity<ApiResponse<Diary>> saveDiary(@RequestParam Long userId,
                                           @RequestParam String content,
                                           @RequestParam String appliedStamp,
                                           @RequestParam(required = false) String emotion) {
        System.out.println("=== Diary Save API Called ===");
        System.out.println("userId: " + userId);
        System.out.println("content: " + content);
        System.out.println("appliedStamp: " + appliedStamp);
        System.out.println("emotion: " + emotion);
        
        try {
            Diary saved = diaryService.saveDiary(userId, content, appliedStamp, emotion);
            System.out.println("Diary saved successfully with ID: " + saved.getDiaryId());
            
            // 간단한 응답 형태로 변경 (디버깅용)
            ApiResponse<Diary> response = new ApiResponse<>(true, "일기 저장 성공", saved);
            System.out.println("API Response: " + response.isSuccess() + ", " + response.getMessage());
            
            // 응답을 Map으로 변환하여 디버깅
            java.util.Map<String, Object> debugResponse = new java.util.HashMap<>();
            debugResponse.put("success", true);
            debugResponse.put("message", "일기 저장 성공");
            debugResponse.put("data", saved);
            debugResponse.put("diaryId", saved.getDiaryId());
            
            System.out.println("Debug Response: " + debugResponse);
            
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            System.err.println("Error saving diary: " + e.getMessage());
            e.printStackTrace();
            return ResponseEntity.ok(new ApiResponse<>(false, "일기 저장 실패: " + e.getMessage(), null));
        }
    }
    // ===================== END UPDATED API ENDPOINT =====================

    // 유저별, 월별 일기 목록 조회 (REST)
    @GetMapping("/api/diaries")
    @ResponseBody
    public ResponseEntity<ApiResponse<List<Diary>>> getDiariesByUserAndMonth(@RequestParam Long userId,
                                                                @RequestParam int year,
                                                                @RequestParam int month) {
        List<Diary> diaries = diaryService.getDiariesByUserAndMonth(userId, year, month);
        return ResponseEntity.ok(new ApiResponse<>(true, "일기 목록 조회 성공", diaries));
    }

    // ===================== NEW API ENDPOINT =====================
    // 2025-01-XX: 월별 감정 통계 기능 추가
    // 유저별, 월별 감정 통계 조회 (REST)
    @GetMapping("/api/diaries/emotions")
    @ResponseBody
    public ResponseEntity<ApiResponse<Map<String, Object>>> getEmotionStatsByUserAndMonth(@RequestParam Long userId,
                                                                                          @RequestParam int year,
                                                                                          @RequestParam int month) {
        Map<String, Object> emotionStats = diaryService.getEmotionStatsByUserAndMonth(userId, year, month);
        return ResponseEntity.ok(new ApiResponse<>(true, "감정 통계 조회 성공", emotionStats));
    }
    // ===================== END NEW API ENDPOINT =====================

    // 일기 상세 조회 (REST)
    @GetMapping("/api/diaries/{id}")
    @ResponseBody
    public ResponseEntity<ApiResponse<Diary>> getDiaryById(@PathVariable Long id) {
        Optional<Diary> diary = diaryService.getDiaryById(id);
        if (diary.isPresent()) {
            return ResponseEntity.ok(new ApiResponse<>(true, "일기 조회 성공", diary.get()));
        } else {
            return ResponseEntity.ok(new ApiResponse<>(false, "일기를 찾을 수 없습니다", null));
        }
    }

    // ===================== Thymeleaf =====================

    // 달력/일기 페이지 렌더링 (Thymeleaf)
    /**
     * userId 파라미터로 유저 닉네임을 보여주는 것은 테스트용입니다.
     * 실제 서비스에서는 로그인/세션 기반으로 user 정보를 전달합니다.
     */
    @GetMapping("/diary-calendar")
    public String diaryCalendarPage(@RequestParam(required = false) Long userId, Model model, HttpSession session) {
        User user = null;
        if (userId != null) { // 테스트용: 쿼리 파라미터로 유저 정보 전달
            user = userRepository.findById(userId).orElse(null);
        } else { // 실제 서비스: 세션에서 유저 정보 전달
            user = (User) session.getAttribute("user");
        }
        model.addAttribute("user", user);
        return "diary_calendar";
    }

    // ===================== UPDATED FORM ENDPOINT =====================
    // 2025-01-XX: 감정 표현 기능 추가를 위한 폼 기반 일기 저장 엔드포인트 수정
    // 기존 폼 기반 일기 저장에 emotion 파라미터 추가 (선택사항)
    // (옵션) 폼 기반 일기 저장 (Thymeleaf) - 감정 포함
    @PostMapping("/diary")
    public String saveDiaryForm(@RequestParam Long userId,
                                @RequestParam String content,
                                @RequestParam String appliedStamp,
                                @RequestParam(required = false) String emotion,
                                Model model) {
        diaryService.saveDiary(userId, content, appliedStamp, emotion);
        return "redirect:/diary-calendar";
    }
    // ===================== END UPDATED FORM ENDPOINT =====================
} 