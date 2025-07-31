package com.example.backend.repository;

import com.example.backend.entity.WeeklyFeedback;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface WeeklyFeedbackRepository extends JpaRepository<WeeklyFeedback, Long> {
    
    @Query("SELECT wf FROM WeeklyFeedback wf " +
           "LEFT JOIN FETCH wf.feedbackProofs " +
           "LEFT JOIN FETCH wf.recommendActivities " +
           "WHERE wf.user.userId = :userId AND wf.weekOffset = :weekOffset")
    Optional<WeeklyFeedback> findByUser_UserIdAndWeekOffsetWithDetails(@Param("userId") Long userId, @Param("weekOffset") int weekOffset);
    
    List<WeeklyFeedback> findAllByUser_UserId(Long userId);
}
