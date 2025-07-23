package com.example.backend.repository;

import com.example.backend.entity.UserStampHistory;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserStampHistoryRepository extends JpaRepository<UserStampHistory, Long> {
} 