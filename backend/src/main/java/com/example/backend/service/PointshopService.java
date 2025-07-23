package com.example.backend.service;

import com.example.backend.dto.StampDto;
import com.example.backend.dto.UserStampDto;
import java.util.List;
import org.springframework.stereotype.Service;

@Service
public class PointshopService {
    // 1. 사용자 포인트 조회
    public int getUserPoint(Long userId) {
        // TODO: 사용자 포인트 조회 로직
        return 0;
    }

    // 2. 구매 가능한 도장 목록 조회
    public List<StampDto> getAvailableStamps(Long userId) {
        // TODO: 구매 가능한 도장 목록 반환
        return null;
    }

    // 3. 도장 상세 정보 조회
    public StampDto getStampDetail(Long stampId, Long userId) {
        // TODO: 도장 상세 정보 반환
        return null;
    }

    // 4. 카테고리별 도장 목록 조회
    public List<StampDto> getStampsByCategory(String category, Long userId) {
        // TODO: 카테고리별 도장 목록 반환
        return null;
    }

    // 5. 도장 구매
    public boolean purchaseStamp(Long userId, Long stampId) {
        // TODO: 도장 구매 처리
        return false;
    }

    // 6. 보유 도장 적용
    public boolean applyStamp(Long userId, Long userStampId) {
        // TODO: 도장 적용 처리
        return false;
    }

    // 7. 현재 적용중인 도장 조회
    public UserStampDto getActiveStamp(Long userId) {
        // TODO: 현재 적용중인 도장 반환
        return null;
    }

    // 8. 내가 보유한 도장 목록 조회
    public List<UserStampDto> getMyStamps(Long userId) {
        // TODO: 사용자가 보유한 도장 목록 반환
        return null;
    }
} 