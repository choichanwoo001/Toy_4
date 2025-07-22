package com.example.backend.controller;

import com.example.backend.dto.ReportResponseDto;
import com.example.backend.service.WeeklyReportService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/report")
@RequiredArgsConstructor
public class WeeklyReportController {

    private final WeeklyReportService weeklyReportService;

    // report api
    @GetMapping
    public ResponseEntity<ReportResponseDto> getWeeklyReport(
            @RequestParam Long userId,
            @RequestParam(defaultValue = "0") int weekOffset
    ) {
        ReportResponseDto responseDto = weeklyReportService.getWeeklyReport(userId, weekOffset);
        return ResponseEntity.ok(responseDto);
    }
}
