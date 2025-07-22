package com.example.backend.service;

import com.example.backend.entity.TestEntity;
import com.example.backend.repository.TestRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

@Service
public class TestService {
    
    @Autowired
    private TestRepository testRepository;
    
    public String getHelloWorld() {
        return "Hello World from Spring Boot!";
    }
    
    public TestEntity saveTestMessage(String message) {
        String currentTime = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        TestEntity testEntity = new TestEntity(message, currentTime);
        return testRepository.save(testEntity);
    }
    
    public List<TestEntity> getAllTestMessages() {
        return testRepository.findAll();
    }
    
    public String testDatabaseConnection() {
        try {
            long count = testRepository.count();
            return "데이터베이스 연결 성공! 현재 테이블 레코드 수: " + count;
        } catch (Exception e) {
            return "데이터베이스 연결 실패: " + e.getMessage();
        }
    }
} 