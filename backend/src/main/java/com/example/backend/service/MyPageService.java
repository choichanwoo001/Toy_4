package com.example.backend.service;

import com.example.backend.dto.MyPageSummaryDto;
import org.springframework.stereotype.Service;
import java.time.LocalDate;
import java.util.Arrays;

@Service
public class MyPageService {

    public MyPageSummaryDto getMyPageSummary(Long userId) {
        // 실제 구현 시 DB에서 userId로 데이터 조회
        MyPageSummaryDto dto = new MyPageSummaryDto();
        dto.setNickname("홍길동");
        dto.setEmail("hong@email.com");
        dto.setJoinDate(LocalDate.of(2023, 1, 1));
        dto.setTotalDiaryCount(123);
        dto.setConsecutiveDiaryDays(7);
        dto.setMainEmotions(Arrays.asList("#기쁨", "#평온", "#성장"));
        dto.setRecentAiComment("제자님, 오늘도 하루를 잘 기록했네요! 작은 노력이 큰 변화를 만든답니다.");
        dto.setRecentStampImage("참잘했어요.jpg");
        dto.setPoint(1000); // TODO: 실제 포인트 값으로 변경 필요
        return dto;
    }
}
