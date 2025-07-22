package com.example.backend.service;

import com.example.backend.dto.UserRegistrationDto;
import com.example.backend.entity.User;
import com.example.backend.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@Transactional
@Slf4j
public class UserService {
    
    private final UserRepository userRepository;
    
    /**
     * 비밀번호 암호화
     */
    private String encodePassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hashedBytes = md.digest(password.getBytes());
            return Base64.getEncoder().encodeToString(hashedBytes);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("비밀번호 암호화 중 오류가 발생했습니다.", e);
        }
    }
    
    /**
     * 비밀번호 확인
     */
    private boolean matchesPassword(String rawPassword, String encodedPassword) {
        String encodedRawPassword = encodePassword(rawPassword);
        return encodedRawPassword.equals(encodedPassword);
    }
    
    /**
     * 회원가입 처리
     */
    public User registerUser(UserRegistrationDto registrationDto) {
        // 이메일 중복 확인
        if (userRepository.existsByUserEmail(registrationDto.getUserEmail())) {
            throw new IllegalArgumentException("이미 등록된 이메일입니다.");
        }
        
        // 닉네임 중복 확인
        if (userRepository.existsByUserNickname(registrationDto.getUserNickname())) {
            throw new IllegalArgumentException("이미 사용 중인 닉네임입니다.");
        }
        
        // 비밀번호 확인
        if (!registrationDto.isPasswordMatching()) {
            throw new IllegalArgumentException("비밀번호가 일치하지 않습니다.");
        }
        
        // 약관 동의 확인
        if (!registrationDto.isTermsAgreed()) {
            throw new IllegalArgumentException("약관에 동의해야 합니다.");
        }
        
        // User 엔티티 생성
        String encodedPassword = encodePassword(registrationDto.getUserPassword());
        
        User user = User.builder()
                .userEmail(registrationDto.getUserEmail())
                .userPassword(encodedPassword)
                .userNickname(registrationDto.getUserNickname())
                .userPhone(registrationDto.getUserPhone())
                .userStatus("active")
                .userFailedLogin(0)
                .userCommentTime(6)
                .userTokenCount(0)
                .build();
        
        // DB에 저장
        return userRepository.save(user);
    }
    
    /**
     * 이메일로 사용자 찾기
     */
    @Transactional(readOnly = true)
    public Optional<User> findByEmail(String email) {
        return userRepository.findActiveUserByEmail(email);
    }
    
    /**
     * 이메일 중복 확인
     */
    @Transactional(readOnly = true)
    public boolean isEmailDuplicate(String email) {
        return userRepository.existsByUserEmail(email);
    }
    
    /**
     * 닉네임 중복 확인
     */
    @Transactional(readOnly = true)
    public boolean isNicknameDuplicate(String nickname) {
        return userRepository.existsByUserNickname(nickname);
    }
    
    /**
     * 로그인 처리
     */
    public User login(String email, String password) {
        Optional<User> userOpt = userRepository.findActiveUserByEmail(email);
        
        if (userOpt.isEmpty()) {
            throw new IllegalArgumentException("존재하지 않는 사용자입니다.");
        }
        
        User user = userOpt.get();
        
        // 비밀번호 확인
        if (!matchesPassword(password, user.getUserPassword())) {
            user.incrementFailedLogin();
            userRepository.save(user);
            throw new IllegalArgumentException("비밀번호가 일치하지 않습니다.");
        }
        
        // 로그인 성공 시 실패 횟수 초기화 및 마지막 로그인 시간 업데이트
        user.resetFailedLogin();
        user.updateLastLogin();
        
        return userRepository.save(user);
    }
    
    /**
     * 사용자 삭제 (소프트 삭제)
     */
    public void deleteUser(Long userId) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new IllegalArgumentException("존재하지 않는 사용자입니다."));
        
        user.softDelete();
        userRepository.save(user);
    }
    
    /**
     * 토큰 추가
     */
    public void addTokens(Long userId, int count) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new IllegalArgumentException("존재하지 않는 사용자입니다."));
        
        user.addTokens(count);
        userRepository.save(user);
    }
    
    /**
     * 토큰 사용
     */
    public boolean useToken(Long userId) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new IllegalArgumentException("존재하지 않는 사용자입니다."));
        
        boolean used = user.useToken();
        if (used) {
            userRepository.save(user);
        }
        
        return used;
    }
} 