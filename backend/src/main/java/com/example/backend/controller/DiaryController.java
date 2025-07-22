package com.example.backend.controller;

import com.example.backend.entity.Diary;
import com.example.backend.service.DiaryService;
import com.example.backend.dto.ApiResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@Controller
public class DiaryController {
    @Autowired
    private DiaryService diaryService;

    // ===================== REST API =====================

    // 일기 저장 (REST)
    @PostMapping("/api/diaries")
    @ResponseBody
    public ResponseEntity<ApiResponse<Diary>> saveDiary(@RequestParam Long userId,
                                           @RequestParam String content,
                                           @RequestParam String appliedStamp) {
        Diary saved = diaryService.saveDiary(userId, content, appliedStamp);
        return ResponseEntity.ok(new ApiResponse<>(true, "일기 저장 성공", saved));
    }

    // 유저별, 월별 일기 목록 조회 (REST)
    @GetMapping("/api/diaries")
    @ResponseBody
    public ResponseEntity<ApiResponse<List<Diary>>> getDiariesByUserAndMonth(@RequestParam Long userId,
                                                                @RequestParam int year,
                                                                @RequestParam int month) {
        List<Diary> diaries = diaryService.getDiariesByUserAndMonth(userId, year, month);
        return ResponseEntity.ok(new ApiResponse<>(true, "일기 목록 조회 성공", diaries));
    }

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
    @GetMapping("/diary-calendar")
    public String diaryCalendarPage(Model model) {
        // 필요시 model에 데이터 추가
        return "diary_calendar";
    }

    // (옵션) 폼 기반 일기 저장 (Thymeleaf)
    @PostMapping("/diary")
    public String saveDiaryForm(@RequestParam Long userId,
                                @RequestParam String content,
                                @RequestParam String appliedStamp,
                                Model model) {
        diaryService.saveDiary(userId, content, appliedStamp);
        return "redirect:/diary-calendar";
    }
} 