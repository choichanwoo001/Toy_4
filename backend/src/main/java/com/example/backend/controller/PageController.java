package com.example.backend.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class PageController {

    // 일기 달력 페이지 매핑 (헤더 링크용)
    @GetMapping("/diary")
    public String diary() {
        return "redirect:/diary-calendar";
    }

    // AI와 채팅하는 페이지 매핑
    // 아직 채팅 기능은 없음
    @GetMapping("/chat")
    public String chat(Model model) {
        // 채팅 페이지
        model.addAttribute("title", "선생님과 채팅");
        model.addAttribute("contentPath", "chat");
        return "layout/base";
    }
}
