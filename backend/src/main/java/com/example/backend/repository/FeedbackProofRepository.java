package com.example.backend.repository;

import com.example.backend.entity.FeedbackProof;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FeedbackProofRepository extends JpaRepository<FeedbackProof, Long> {
} 