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
    
    Optional<WeeklyFeedback> findByUser_UserIdAndWeekOffset(Long userId, int weekOffset);
    
    // MultipleBagFetchException 해결을 위해 기본 쿼리로 변경
    @Query("SELECT w FROM WeeklyFeedback w " +
           "WHERE w.user.userId = :userId AND w.weekOffset = :weekOffset")
    Optional<WeeklyFeedback> findByUser_UserIdAndWeekOffsetWithDetails(@Param("userId") Long userId, @Param("weekOffset") int weekOffset);

    List<WeeklyFeedback> findAllByUser_UserId(Long userId);
}
