package com.example.backend.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping
public class WeeklyReportPageController {

    // "/report" 경로로 GET 요청이 오면 감정 리포트 페이지 뷰를 반환
    @GetMapping("/report")
    public String showReportPage(Model model) {
        model.addAttribute("contentPath", "report");
//        return "layout/base";
        return "page/report";
    }
}