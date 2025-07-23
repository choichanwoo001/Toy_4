package com.example.backend.controller;

import com.example.backend.dto.ReportResponseDto;
import com.example.backend.entity.WeeklyFeedback;
import com.example.backend.service.WeeklyReportService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Comparator;
import java.util.List;

@RestController
@RequestMapping("/api/report")
@RequiredArgsConstructor
public class WeeklyReportController {

    private final WeeklyReportService weeklyReportService;

    // report api
    @GetMapping
    public ResponseEntity<ReportResponseDto> getWeeklyReport(
            @RequestParam Long userId,
            @RequestParam int weekOffset
    ) {
        ReportResponseDto responseDto = weeklyReportService.getWeeklyReport(userId, weekOffset);
        return ResponseEntity.ok(responseDto);
    }

    @GetMapping("/weeks")
    public ResponseEntity<List<Integer>> getAvailableOffsets(@RequestParam Long userId) {
        List<WeeklyFeedback> feedbacks = weeklyReportService.getAllFeedbacks(userId);
        List<Integer> offsets = feedbacks.stream()
                .map(WeeklyFeedback::getWeekOffset)
                .sorted(Comparator.reverseOrder()) // 최신 주차부터
                .toList();
        return ResponseEntity.ok(offsets);
    }
}