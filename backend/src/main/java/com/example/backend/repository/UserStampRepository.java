package com.example.backend.repository;

import com.example.backend.entity.UserStamp;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface UserStampRepository extends JpaRepository<UserStamp, Long> {
    UserStamp findByUserIdAndStampId(Long userId, Long stampId);
    List<UserStamp> findByUserId(Long userId);
    UserStamp findByUserIdAndIsActive(Long userId, String isActive);
} 