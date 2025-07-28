package com.example.backend.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping
public class WeeklyReportPageController {

    // "/report" 경로로 GET 요청이 오면 감정 리포트 페이지 뷰를 반환
    @GetMapping("/report")
    public String showReportPage(@RequestParam(required = false) Long userId,
                                 @RequestParam(required = false) Integer weekOffset,
                                 @RequestParam(required = false) Integer year,
                                 @RequestParam(required = false) Integer month,
                                 Model model) {
        model.addAttribute("contentPath", "report");
        model.addAttribute("userId", userId);
        model.addAttribute("weekOffset", weekOffset);
        model.addAttribute("year", year);
        model.addAttribute("month", month);
        return "layout/base";
    }
}