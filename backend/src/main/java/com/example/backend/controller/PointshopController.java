package com.example.backend.controller;

import com.example.backend.dto.StampDto;
import com.example.backend.dto.UserStampDto;
import com.example.backend.service.PointshopService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.ui.Model;

import java.security.Principal;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;
import java.util.stream.Collectors;

@Controller
@RequestMapping("/pointshop")
public class PointshopController {

    private final PointshopService pointshopService;

    @Autowired
    public PointshopController(PointshopService pointshopService) {
        this.pointshopService = pointshopService;
    }

    // 1. 포인트샵 메인 페이지 렌더링
    @GetMapping
    public String pointshopPage(Model model, Principal principal) {
        // Long userId = getUserIdFromPrincipal(principal);
        Long userId = 1L; // 임시 하드코딩 (테스트용)
        int userPoint = pointshopService.getUserPoint(userId);
        model.addAttribute("userPoint", userPoint);
        return "page/pointshop";
    }

    // 2. 사용자 포인트 조회 (AJAX)
    @GetMapping("/api/points")
    @ResponseBody
    public int getUserPoints(Principal principal) {
        Long userId = getUserIdFromPrincipal(principal);
        return pointshopService.getUserPoint(userId);
    }

    // 3. 상점 도장 목록 조회 (AJAX)
    @GetMapping("/api/stamps")
    @ResponseBody
    public List<Map<String, Object>> getAvailableStamps(
        @RequestParam(value = "filter", required = false, defaultValue = "all") String filter,
        Principal principal
    ) {
        Long userId = 1L; // 임시
        int userPoint = pointshopService.getUserPoint(userId);
        List<StampDto> stamps = pointshopService.getAvailableStamps(userId);
        List<UserStampDto> myStamps = pointshopService.getMyStamps(userId);

        Set<Long> ownedStampIds = myStamps.stream().map(UserStampDto::getStampId).collect(Collectors.toSet());

        List<Map<String, Object>> result = new ArrayList<>();
        for (StampDto stamp : stamps) {
            String status;
            if (ownedStampIds.contains(stamp.getStampId())) {
                status = "owned";
            } else if (userPoint < stamp.getPrice()) {
                status = "insufficient";
            } else {
                status = "buyable";
            }
            // 필터 적용
            if (filter.equals("all") || filter.equals(status) ||
                (filter.equals("notowned") && !ownedStampIds.contains(stamp.getStampId()))) {
                Map<String, Object> map = new HashMap<>();
                map.put("stamp", stamp);
                map.put("status", status);
                result.add(map);
            }
        }
        return result;
    }

    // 4. 내가 보유한 도장 목록 조회 (AJAX)
    @GetMapping("/api/my-stamps")
    @ResponseBody
    public List<UserStampDto> getMyStamps(Principal principal) {
        Long userId = getUserIdFromPrincipal(principal);
        return pointshopService.getMyStamps(userId);
    }

    // 5. 도장 구매
    @PostMapping("/api/buy")
    @ResponseBody
    public boolean buyStamp(@RequestParam Long stampId, Principal principal) {
        Long userId = getUserIdFromPrincipal(principal);
        return pointshopService.purchaseStamp(userId, stampId);
    }

    // 6. 도장 적용
    @PostMapping("/api/apply")
    @ResponseBody
    public boolean applyStamp(@RequestParam Long userStampId, Principal principal) {
        Long userId = getUserIdFromPrincipal(principal);
        return pointshopService.applyStamp(userId, userStampId);
    }

    // (유틸) Principal에서 userId 추출 (실제 구현에 맞게 수정)
    private Long getUserIdFromPrincipal(Principal principal) {
        // 예시: principal.getName()을 userId로 변환
        return Long.valueOf(principal.getName());
    }
} 