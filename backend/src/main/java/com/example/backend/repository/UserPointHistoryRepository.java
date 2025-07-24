package com.example.backend.repository;

import com.example.backend.entity.UserPointHistory;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserPointHistoryRepository extends JpaRepository<UserPointHistory, Long> {
    UserPointHistory findTopByUserIdOrderByCreatedAtDesc(Long userId);
} 