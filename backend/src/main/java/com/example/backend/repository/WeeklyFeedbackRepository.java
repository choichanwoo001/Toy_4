package com.example.backend.repository;

import com.example.backend.entity.WeeklyFeedback;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface WeeklyFeedbackRepository extends JpaRepository<WeeklyFeedback, Long> {
    // @Query("SELECT w FROM WeeklyFeedback w WHERE w.user.userId = :userId AND w.feedbackStart = :start AND w.feedbackEnd = :end")
    //Optional<WeeklyFeedback> findFeedback(@Param("userId") Long userId,
    //                                       @Param("start") String feedbackStart,
    //                                       @Param("end") String feedbackEnd);
    // 아래와 같은 코드
    Optional<WeeklyFeedback> findByUser_UserIdAndFeedbackStartAndFeedbackEnd(Long userId, String start, String end);
}
