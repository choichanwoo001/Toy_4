package com.example.backend.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "user")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;

    @Column(nullable = false, length = 255)
    private String userEmail;

    @Column(nullable = false, length = 255)
    private String userPassword;

    @Column(nullable = false, length = 50)
    private String userNickname;

    @Column(nullable = false, length = 20)
    private String userPhone;

    @Column(nullable = false)
    private int userFailedLogin = 0;

    @Column(nullable = false)
    private LocalDateTime userLastLogin = LocalDateTime.now();

    @Column(nullable = false)
    private int userCommentTime = 6;

    @Column(nullable = false)
    private int userTokenCount = 0;

    @Column(nullable = false)
    private LocalDateTime userCreatedAt = LocalDateTime.now();

    @Column(nullable = false, length = 20)
    private String userStatus = "active";

    private LocalDateTime userDeletedAt;

    @Column(length = 100)
    private String userKakaoId;

    public User() {}

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