package com.example.backend.repository;

import com.example.backend.entity.WeeklyFeedback;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface WeeklyFeedbackRepository extends JpaRepository<WeeklyFeedback, Long> {

    // 시작일, 종료일이 일치하는 주간 피드백 조회
    // @Query("SELECT w FROM WeeklyFeedback w WHERE w.user.userId = :userId AND w.feedbackStart = :start AND w.feedbackEnd = :end")
    //Optional<WeeklyFeedback> findFeedback(@Param("userId") Long userId,
    //                                       @Param("start") String feedbackStart,
    //                                       @Param("end") String feedbackEnd);
    // 아래와 같은 코드
    Optional<WeeklyFeedback> findByUser_UserIdAndFeedbackStartAndFeedbackEnd(Long userId, String start, String end);

    // 전체 주간 피드백 목록 조회
    List<WeeklyFeedback> findAllByUser_UserId(Long userId);

    // 주차 오프셋(weekOffset)에 해당하는 주간 피드백 조회
    Optional<WeeklyFeedback> findByUser_UserIdAndWeekOffset(Long userId, int weekOffset);
}
