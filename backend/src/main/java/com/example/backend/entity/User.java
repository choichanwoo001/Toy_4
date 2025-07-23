package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "user")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "user_id")
    private Long userId;

    @Column(name = "user_email", nullable = false, length = 255)
    private String userEmail;

    @Column(name = "user_password", nullable = false, length = 255)
    private String userPassword;

    @Column(name = "user_nickname", nullable = false, length = 50)
    private String userNickname;

    @Column(name = "user_phone", nullable = false, length = 20)
    private String userPhone;

    @Column(name = "user_faild_login", nullable = false)
    private int userFaildLogin;

    @Column(name = "user_last_login", nullable = false)
    private LocalDateTime userLastLogin;

    @Column(name = "user_comment_time", nullable = false)
    private LocalDateTime userCommentTime;

    @Column(name = "user_token_count", nullable = false)
    private int userTokenCount;

    @Column(name = "user_created_at", nullable = false)
    private LocalDateTime userCreatedAt;

    @Column(name = "user_status", nullable = false, length = 20)
    private String userStatus;

    @Column(name = "user_deleted_at")
    private LocalDateTime userDeletedAt;

    @Column(name = "user_kakao_id", length = 100)
    private String userKakaoId;
}