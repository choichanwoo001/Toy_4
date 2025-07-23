package com.example.backend.service;

import com.example.backend.dto.MyPageSummaryDto;
import com.example.backend.entity.DailyComment;
import com.example.backend.entity.Diary;
import com.example.backend.entity.User;
import com.example.backend.repository.CommentEmotionMappingRepository;
import com.example.backend.repository.DailyCommentRepository;
import com.example.backend.repository.DiaryRepository;
import com.example.backend.repository.UserRepository;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
@RequiredArgsConstructor
public class MyPageService {
    private final UserRepository userRepository;
    private final DiaryRepository diaryRepository;
    private final DailyCommentRepository dailyCommentRepository;
    private final CommentEmotionMappingRepository commentEmotionMappingRepository;

    @Transactional
    public MyPageSummaryDto getMyPageSummary(Long userId) {
        User user = userRepository.findById(userId)
            .orElseThrow(() -> new RuntimeException("User not found"));
        int totalDiaryCount = diaryRepository.countByUser(user);
        int consecutiveDiaryDays = calculateConsecutiveDiaryDays(user);
        DailyComment recentComment = dailyCommentRepository.findTopByUserOrderByCreatedAtDesc(user);
        List<String> mainEmotions = List.of();
        String recentAiComment = null;
        String recentStampImage = null;
        if (recentComment != null) {
            mainEmotions = commentEmotionMappingRepository.findEmotionsByDailyComment(recentComment);
            recentAiComment = recentComment.getContent();
            if (recentComment.getDiary() != null) {
                recentStampImage = recentComment.getDiary().getAppliedStamp();
            }
        }
        // mainEmotions를 '#행복 #피로' 형식의 1개 문자열 리스트로 가공
        String mainEmotionsStr = mainEmotions.stream()
            .map(e -> "#" + e)
            .reduce((a, b) -> a + " " + b)
            .orElse("");
        
        MyPageSummaryDto dto = new MyPageSummaryDto();
        dto.setNickname(user.getUserNickname());
        dto.setEmail(user.getUserEmail());
        dto.setJoinDate(user.getUserCreatedAt().toLocalDate());
        dto.setTotalDiaryCount(totalDiaryCount);
        dto.setConsecutiveDiaryDays(consecutiveDiaryDays);
        dto.setMainEmotions(List.of(mainEmotionsStr));
        dto.setRecentAiComment(recentAiComment != null ? recentAiComment : "AI 코멘트가 없습니다.");
        dto.setRecentStampImage(recentStampImage != null ? recentStampImage : "default_stamp.png");
        return dto;
    }

    // 어제까지 연속 일기 작성 일수 계산
    private int calculateConsecutiveDiaryDays(User user) {
        List<Diary> diaries = diaryRepository.findByUserOrderByCreatedAtDesc(user);
        if (diaries.isEmpty()) {
            return 0;
        }
        java.time.LocalDate yesterday = java.time.LocalDate.now().minusDays(1);
        int streak = 0;
        for (com.example.backend.entity.Diary diary : diaries) {
            java.time.LocalDate diaryDate = diary.getCreatedAt().toLocalDate();
            if (diaryDate.equals(yesterday.minusDays(streak))) {
                streak++;
            } else if (diaryDate.isBefore(yesterday.minusDays(streak))) {
                break;
            }
        }
        return streak;
    }
}
