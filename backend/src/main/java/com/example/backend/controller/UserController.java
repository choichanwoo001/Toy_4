package com.example.backend.controller;

import com.example.backend.dto.UserRegistrationDto;
import com.example.backend.entity.User;
import com.example.backend.service.UserService;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@Controller
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @PostMapping("/register")
    public String register(@ModelAttribute UserRegistrationDto registrationDto, HttpSession session) {
        try {
            User registeredUser = userService.registerUser(registrationDto);
            // 회원가입 성공 시 세션에 사용자 정보 저장
            session.setAttribute("user", registeredUser);
            return "redirect:/?registered=true";
        } catch (Exception e) {
            return "redirect:/?error=" + e.getMessage();
        }
    }

    @PostMapping("/login")
    public String login(@RequestParam String email, 
                       @RequestParam String password, 
                       HttpSession session) {
        try {
            User user = userService.login(email, password);
            // 로그인 성공 시 세션에 사용자 정보 저장
            session.setAttribute("user", user);
            return "redirect:/?login=true";
        } catch (Exception e) {
            return "redirect:/?error=" + e.getMessage();
        }
    }

    @PostMapping("/logout")
    public String logout(HttpSession session) {
        // 세션에서 사용자 정보 제거
        session.removeAttribute("user");
        session.invalidate();
        return "redirect:/?logout=true";
    }

    @PostMapping("/api/check-email")
    @ResponseBody
    public String checkEmail(@RequestParam String email) {
        boolean isDuplicate = userService.isEmailDuplicate(email);
        return String.valueOf(isDuplicate);
    }

    @PostMapping("/api/check-nickname")
    @ResponseBody
    public String checkNickname(@RequestParam String nickname) {
        boolean isDuplicate = userService.isNicknameDuplicate(nickname);
        return String.valueOf(isDuplicate);
    }
} 