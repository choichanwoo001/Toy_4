package com.example.backend.repository;

import com.example.backend.entity.Diary;
import com.example.backend.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;

@Repository
public interface DiaryRepository extends JpaRepository<Diary, Long> {
    List<Diary> findByUserAndCreatedAtBetween(User user, LocalDateTime start, LocalDateTime end);
    int countByUser(User user);
    Diary findTopByUserOrderByCreatedAtDesc(User user);
    List<Diary> findByUserOrderByCreatedAtDesc(User user);
} 