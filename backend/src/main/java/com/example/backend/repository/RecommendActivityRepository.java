package com.example.backend.repository;

import com.example.backend.entity.RecommendActivity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RecommendActivityRepository extends JpaRepository<RecommendActivity, Long> {
} 