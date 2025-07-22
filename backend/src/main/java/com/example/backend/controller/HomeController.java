package com.example.backend.controller;

import com.example.backend.entity.TestEntity;
import com.example.backend.service.TestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
public class HomeController {

    @Autowired
    private TestService testService;

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("message", "Spring Boot + Thymeleaf + MySQL 프로젝트가 성공적으로 실행되었습니다!");
        model.addAttribute("helloWorld", testService.getHelloWorld());
        model.addAttribute("dbStatus", testService.testDatabaseConnection());
        
        List<TestEntity> messages = testService.getAllTestMessages();
        model.addAttribute("messages", messages);
        
        return "home";
    }
    
    @PostMapping("/save-message")
    public String saveMessage(@RequestParam String message, Model model) {
        testService.saveTestMessage(message);
        return "redirect:/";
    }

    @GetMapping("/diary-calendar")
    public String diaryCalendar() {
        return "diary_calendar";
    }
} 