package com.example.backend.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "user")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId; // Primary Key

    @Column(nullable = false, length = 255)
    private String userEmail; // 이메일 주소

    @Column(nullable = false, length = 255)
    private String userPassword; // 해시된 비밀번호

    @Column(nullable = false, length = 50)
    private String userNickname; // 사용자 표시 이름

    @Column(nullable = false, length = 20)
    private String userPhone; // 미포함

    @Column(nullable = false)
    private int userFailedLogin = 0; // 로그인 실패 누적 횟수

    @Column(nullable = false)
    private LocalDateTime userLastLogin = LocalDateTime.now(); // 마지막 로그인 시간

    @Column(nullable = false)
    private int userCommentTime = 6; // AI 코멘트 받을 시간

    @Column(nullable = false)
    private int userTokenCount = 0; // 잔여 토큰 수

    @Column(nullable = false)
    private LocalDateTime userCreatedAt = LocalDateTime.now(); // 가입일

    @Column(nullable = false, length = 20)
    private String userStatus = "active"; // 상태 코드

    private LocalDateTime userDeletedAt; // 탈퇴한 시점 (NULL이면 활성 회원)

    @Column(length = 100)
    private String userKakaoId; // 카카오 연동용 사용자 식별자

    // getter/setter
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
    public String getUserEmail() { return userEmail; }
    public void setUserEmail(String userEmail) { this.userEmail = userEmail; }
    public String getUserPassword() { return userPassword; }
    public void setUserPassword(String userPassword) { this.userPassword = userPassword; }
    public String getUserNickname() { return userNickname; }
    public void setUserNickname(String userNickname) { this.userNickname = userNickname; }
    public String getUserPhone() { return userPhone; }
    public void setUserPhone(String userPhone) { this.userPhone = userPhone; }
    public int getUserFailedLogin() { return userFailedLogin; }
    public void setUserFailedLogin(int userFailedLogin) { this.userFailedLogin = userFailedLogin; }
    public LocalDateTime getUserLastLogin() { return userLastLogin; }
    public void setUserLastLogin(LocalDateTime userLastLogin) { this.userLastLogin = userLastLogin; }
    public int getUserCommentTime() { return userCommentTime; }
    public void setUserCommentTime(int userCommentTime) { this.userCommentTime = userCommentTime; }
    public int getUserTokenCount() { return userTokenCount; }
    public void setUserTokenCount(int userTokenCount) { this.userTokenCount = userTokenCount; }
    public LocalDateTime getUserCreatedAt() { return userCreatedAt; }
    public void setUserCreatedAt(LocalDateTime userCreatedAt) { this.userCreatedAt = userCreatedAt; }
    public String getUserStatus() { return userStatus; }
    public void setUserStatus(String userStatus) { this.userStatus = userStatus; }
    public LocalDateTime getUserDeletedAt() { return userDeletedAt; }
    public void setUserDeletedAt(LocalDateTime userDeletedAt) { this.userDeletedAt = userDeletedAt; }
    public String getUserKakaoId() { return userKakaoId; }
    public void setUserKakaoId(String userKakaoId) { this.userKakaoId = userKakaoId; }
} 