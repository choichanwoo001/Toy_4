package com.example.backend.controller;


import com.example.backend.service.MyPageService;
import com.example.backend.dto.MyPageSummaryDto;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@RequiredArgsConstructor
@Controller
@RequestMapping("/mypage")
public class MyPageController {
    private final MyPageService myPageService;

    // 마이페이지 매핑
    @GetMapping
    public String myPage(Model model) {
        model.addAttribute("title", "마이페이지");
        model.addAttribute("contentPath", "myPage");
        // 실제 구현 시 로그인 사용자 ID 사용
        MyPageSummaryDto summary = myPageService.getMyPageSummary(1L);
        model.addAttribute("summary", summary);
        return "layout/base";
    }
}