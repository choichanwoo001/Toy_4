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
        int points = history != null ? history.getAfterPoint() : 0;
        System.out.println("=== 포인트 조회 ===");
        System.out.println("사용자 ID: " + userId);
        System.out.println("최신 기록: " + (history != null ? history.getReason() : "없음"));
        System.out.println("기록 시간: " + (history != null ? history.getCreatedAt() : "없음"));
        System.out.println("현재 포인트: " + points);
        return points;
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

        System.out.println("=== 구매 시도 ===");
        System.out.println("사용자 ID: " + userId);
        System.out.println("도장 ID: " + stampId);
        System.out.println("현재 포인트: " + currentPoint);
        System.out.println("도장 가격: " + price);

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
        history.setCreatedAt(java.time.LocalDateTime.now().plusSeconds(1)); // 1초 추가하여 최신 기록 보장
        
        UserPointHistory savedHistory = userPointHistoryRepository.save(history);
        
        System.out.println("=== 구매 완료 ===");
        System.out.println("차감 후 포인트: " + (currentPoint - price));
        System.out.println("기록 저장됨: " + savedHistory.getReason());
        System.out.println("저장된 기록 ID: " + savedHistory.getUserPointHistoryId());
        
        // 저장 후 포인트 재확인
        int updatedPoint = getUserPoint(userId);
        System.out.println("저장 후 조회된 포인트: " + updatedPoint);

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
        // 기존 코드 (주석처리)
        // TODO: 현재 적용중인 도장 반환
        // return null;
        
        // 새로운 구현: 스탬프 상세 정보 포함
        List<UserStamp> userStamps = userStampRepository.findByUserId(userId);
        for (UserStamp us : userStamps) {
            if ("Y".equals(us.getIsActive())) {
                // 스탬프 정보 조회
                Stamp stamp = stampRepository.findById(us.getStampId()).orElse(null);
                if (stamp != null) {
                    UserStampDto dto = new UserStampDto();
                    dto.setUserStampId(us.getUserStampId());
                    dto.setUserId(us.getUserId());
                    dto.setStampId(us.getStampId());
                    dto.setIsActive(us.getIsActive());
                    dto.setCreatedAt(us.getCreatedAt());
                    dto.setUpdatedAt(us.getUpdatedAt());
                    
                    // 스탬프 정보 설정
                    dto.setStampName(stamp.getName());
                    dto.setStampImage(stamp.getImage());
                    dto.setStampDescription(stamp.getDescription());
                    dto.setStampPrice(stamp.getPrice());
                    
                    return dto;
                }
            }
        }
        return null; // 적용된 스탬프가 없음
    }

    // 8. 내가 보유한 도장 목록 조회
    public List<UserStampDto> getMyStamps(Long userId) {
        List<UserStamp> userStamps = userStampRepository.findByUserId(userId);
        List<UserStampDto> result = new ArrayList<>();
        for (UserStamp us : userStamps) {
            // 기존 코드 (주석처리)
            // UserStampDto dto = new UserStampDto();
            // dto.setUserStampId(us.getUserStampId());
            // dto.setUserId(us.getUserId());
            // dto.setStampId(us.getStampId());
            // dto.setIsActive(us.getIsActive());
            // dto.setCreatedAt(us.getCreatedAt());
            // dto.setUpdatedAt(us.getUpdatedAt());
            // result.add(dto);
            
            // 새로운 구현: 스탬프 상세 정보 포함
            Stamp stamp = stampRepository.findById(us.getStampId()).orElse(null);
            if (stamp != null) {
                UserStampDto dto = new UserStampDto();
                dto.setUserStampId(us.getUserStampId());
                dto.setUserId(us.getUserId());
                dto.setStampId(us.getStampId());
                dto.setIsActive(us.getIsActive());
                dto.setCreatedAt(us.getCreatedAt());
                dto.setUpdatedAt(us.getUpdatedAt());
                
                // 스탬프 정보 설정
                dto.setStampName(stamp.getName());
                dto.setStampImage(stamp.getImage());
                dto.setStampDescription(stamp.getDescription());
                dto.setStampPrice(stamp.getPrice());
                
                result.add(dto);
            }
        }
        return result;
    }
} 