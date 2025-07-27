package com.example.backend.controller;

import com.example.backend.entity.User;
import com.example.backend.service.UserService;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

/**
 * API 엔드포인트를 제공하는 컨트롤러
 * 회원가입 시 중복 검사, 로그인 상태 확인 등의 API 기능을 처리
 */
@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
@Slf4j
public class ApiController {

    private final UserService userService;

    /**
     * 이메일 중복 검사 API
     * 회원가입 폼에서 실시간으로 이메일 중복 여부를 확인
     * 
     * @param email 검사할 이메일 주소
     * @return "true" (중복됨) 또는 "false" (사용 가능)
     */
    @PostMapping("/check-email")
    public String checkEmail(@RequestParam String email) {
        boolean isDuplicate = userService.isEmailDuplicate(email);
        return String.valueOf(isDuplicate);
    }

    /**
     * 닉네임 중복 검사 API
     * 회원가입 폼에서 실시간으로 닉네임 중복 여부를 확인
     * 
     * @param nickname 검사할 닉네임
     * @return "true" (중복됨) 또는 "false" (사용 가능)
     */
    @PostMapping("/check-nickname")
    public String checkNickname(@RequestParam String nickname) {
        boolean isDuplicate = userService.isNicknameDuplicate(nickname);
        return String.valueOf(isDuplicate);
    }

    /**
     * 로그인 상태 확인 API
     * 현재 세션에서 사용자의 로그인 상태를 확인
     * 클라이언트에서 페이지 로드 시 로그인 상태를 체크하는데 사용
     * 
     * @param session HTTP 세션 객체
     * @return "true" (로그인됨) 또는 "false" (로그아웃됨)
     */
    @PostMapping("/check-login-status")
    public String checkLoginStatus(HttpSession session) {
        log.info("로그인 상태 확인 요청 받음");
        try {
            // 세션에서 사용자 정보 확인
            User user = (User) session.getAttribute("user");
            boolean isLoggedIn = user != null && user.isActive();
            log.info("로그인 상태: {}, 사용자: {}", isLoggedIn, user != null ? user.getUserEmail() : "null");
            return String.valueOf(isLoggedIn);
        } catch (Exception e) {
            log.error("로그인 상태 확인 중 오류 발생", e);
            // 세션에서 사용자 정보를 가져올 때 오류가 발생하면 로그아웃 상태로 처리
            session.removeAttribute("user");
            return "false";
        }
    }

    /**
     * 현재 로그인한 사용자 정보 조회 API
     * 세션에서 사용자 정보를 JSON 형태로 반환
     * 
     * @param session HTTP 세션 객체
     * @return 사용자 정보 JSON 또는 null
     */
    @GetMapping("/current-user")
    public ResponseEntity<Map<String, Object>> getCurrentUser(HttpSession session) {
        log.info("현재 사용자 정보 조회 요청 받음");
        try {
            User user = (User) session.getAttribute("user");
            if (user != null && user.isActive()) {
                Map<String, Object> userInfo = new HashMap<>();
                userInfo.put("userId", user.getUserId());
                userInfo.put("userEmail", user.getUserEmail());
                userInfo.put("nickname", user.getUserNickname());
                userInfo.put("isActive", user.isActive());
                
                log.info("사용자 정보 반환: {}", userInfo);
                return ResponseEntity.ok(userInfo);
            } else {
                log.info("로그인된 사용자가 없음");
                return ResponseEntity.ok(null);
            }
        } catch (Exception e) {
            log.error("사용자 정보 조회 중 오류 발생", e);
            return ResponseEntity.ok(null);
        }
    }
} 