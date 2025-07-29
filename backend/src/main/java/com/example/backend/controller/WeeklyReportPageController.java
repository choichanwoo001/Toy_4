package com.example.backend.controller;

import com.example.backend.entity.User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
<<<<<<< HEAD
import org.springframework.web.bind.annotation.RequestParam;
=======
import jakarta.servlet.http.HttpSession;
>>>>>>> bfaa47858efb982e3f3d55bafc70ff315a7e031c

@Controller
@RequestMapping
public class WeeklyReportPageController {

    // "/report" 경로로 GET 요청이 오면 감정 리포트 페이지 뷰를 반환
    @GetMapping("/report")
<<<<<<< HEAD
    public String showReportPage(@RequestParam(required = false) Long userId,
                                 @RequestParam(required = false) Integer weekOffset,
                                 @RequestParam(required = false) Integer year,
                                 @RequestParam(required = false) Integer month,
                                 Model model) {
=======
    public String showReportPage(Model model, HttpSession session) {
        User user = (User) session.getAttribute("user");
        if (user == null) {
            return "redirect:/?loginRequired=true";
        }
        model.addAttribute("user", user);
>>>>>>> bfaa47858efb982e3f3d55bafc70ff315a7e031c
        model.addAttribute("contentPath", "report");
        model.addAttribute("userId", userId);
        model.addAttribute("weekOffset", weekOffset);
        model.addAttribute("year", year);
        model.addAttribute("month", month);
        return "layout/base";
    }
}