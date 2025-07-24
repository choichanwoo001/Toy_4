package com.example.backend.service;

import com.example.backend.dto.StampDto;
import com.example.backend.dto.UserStampDto;
import com.example.backend.entity.Stamp;
import com.example.backend.repository.StampRepository;
import com.example.backend.repository.UserPointHistoryRepository;
import com.example.backend.repository.UserStampRepository;
import com.example.backend.entity.UserStamp;
import com.example.backend.entity.UserPointHistory;
import java.util.ArrayList;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class PointshopService {
    @Autowired
    private UserPointHistoryRepository userPointHistoryRepository;
    @Autowired
    private StampRepository stampRepository;
    @Autowired
    private UserStampRepository userStampRepository;

    // 1. 사용자 포인트 조회
    public int getUserPoint(Long userId) {
        var history = userPointHistoryRepository.findTopByUserIdOrderByCreatedAtDesc(userId);
        return history != null ? history.getAfterPoint() : 0;
    }

    // 2. 구매 가능한 도장 목록 조회
    public List<StampDto> getAvailableStamps(Long userId) {
        List<Stamp> stamps = stampRepository.findAll();
        List<StampDto> result = new ArrayList<>();
        for (Stamp stamp : stamps) {
            StampDto dto = new StampDto();
            dto.setStampId(stamp.getStampId());
            dto.setName(stamp.getName());
            dto.setImage(stamp.getImage());
            dto.setQualification(stamp.getQualification());
            dto.setPrice(stamp.getPrice());
            dto.setDescription(stamp.getDescription());
            dto.setStatus(stamp.getStatus());
            dto.setSalesAt(stamp.getSalesAt());
            dto.setSalesEnd(stamp.getSalesEnd());
            result.add(dto);
        }
        return result;
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

    @Transactional
    public boolean purchaseStamp(Long userId, Long stampId) {
        // 1. 이미 보유한 도장인지 확인
        UserStamp owned = userStampRepository.findByUserIdAndStampId(userId, stampId);
        if (owned != null) return false;

        // 2. 포인트 및 도장 가격 조회
        int currentPoint = getUserPoint(userId);
        Stamp stamp = stampRepository.findById(stampId).orElse(null);
        if (stamp == null) return false;
        int price = stamp.getPrice();

        // 3. 포인트 부족 시
        if (currentPoint < price) return false;

        // 4. user_stamp에 추가
        UserStamp userStamp = new UserStamp();
        userStamp.setUserId(userId);
        userStamp.setStampId(stampId);
        userStamp.setIsActive("N");
        userStamp.setCreatedAt(java.time.LocalDateTime.now());
        userStampRepository.save(userStamp);

        // 5. 포인트 차감 기록
        UserPointHistory history = new UserPointHistory();
        history.setUserId(userId);
        history.setBeforePoint(currentPoint);
        history.setAmount(-price);
        history.setAfterPoint(currentPoint - price);
        history.setReason("도장 구매: " + stamp.getName());
        history.setCreatedAt(java.time.LocalDateTime.now());
        userPointHistoryRepository.save(history);

        return true;
    }

    @Transactional
    public boolean applyStamp(Long userId, Long userStampId) {
        // 1. 모든 도장 isActive="N"으로
        List<UserStamp> userStamps = userStampRepository.findByUserId(userId);
        for (UserStamp us : userStamps) {
            us.setIsActive("N");
        }
        userStampRepository.saveAll(userStamps);

        // 2. 선택한 도장만 isActive="Y"로
        UserStamp toActivate = userStampRepository.findById(userStampId).orElse(null);
        if (toActivate != null && toActivate.getUserId().equals(userId)) {
            toActivate.setIsActive("Y");
            userStampRepository.save(toActivate);
            return true;
        }
        return false;
    }

    // 7. 현재 적용중인 도장 조회
    public UserStampDto getActiveStamp(Long userId) {
        // TODO: 현재 적용중인 도장 반환
        return null;
    }

    // 8. 내가 보유한 도장 목록 조회
    public List<UserStampDto> getMyStamps(Long userId) {
        List<UserStamp> userStamps = userStampRepository.findByUserId(userId);
        List<UserStampDto> result = new ArrayList<>();
        for (UserStamp us : userStamps) {
            UserStampDto dto = new UserStampDto();
            dto.setUserStampId(us.getUserStampId());
            dto.setUserId(us.getUserId());
            dto.setStampId(us.getStampId());
            dto.setIsActive(us.getIsActive());
            dto.setCreatedAt(us.getCreatedAt());
            dto.setUpdatedAt(us.getUpdatedAt());
            result.add(dto);
        }
        return result;
    }
} 