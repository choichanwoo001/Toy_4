package com.example.backend.repository;

import com.example.backend.entity.UserStamp;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserStampRepository extends JpaRepository<UserStamp, Long> {
} 