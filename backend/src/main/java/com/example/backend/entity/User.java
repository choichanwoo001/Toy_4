package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

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
    
    @Column(name = "user_failed_login", nullable = false)
    @Builder.Default
    private Integer userFailedLogin = 0;
    
    @Column(name = "user_last_login", nullable = false)
    @Builder.Default
    private LocalDateTime userLastLogin = LocalDateTime.now();
    
    @Column(name = "user_comment_time", nullable = false)
    @Builder.Default
    private Integer userCommentTime = 6;
    
    @Column(name = "user_token_count", nullable = false)
    @Builder.Default
    private Integer userTokenCount = 0;
    
    @CreationTimestamp
    @Column(name = "user_created_at", nullable = false, updatable = false)
    private LocalDateTime userCreatedAt;
    
    @Column(name = "user_status", nullable = false, length = 20)
    @Builder.Default
    private String userStatus = "active";
    
    @Column(name = "user_deleted_at")
    private LocalDateTime userDeletedAt;
    
    @Column(name = "user_kakao_id", length = 100)
    private String userKakaoId;
    
    @UpdateTimestamp
    @Column(name = "user_updated_at")
    private LocalDateTime userUpdatedAt;
    
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    @Builder.Default
    private List<UserPolicyAgreement> policyAgreements = new ArrayList<>();
    
    // 비즈니스 메서드들
    public boolean isActive() {
        return "active".equals(userStatus) && userDeletedAt == null;
    }
    
    public boolean isSuspended() {
        return "suspended".equals(userStatus);
    }
    
    public void incrementFailedLogin() {
        this.userFailedLogin++;
    }
    
    public void resetFailedLogin() {
        this.userFailedLogin = 0;
    }
    
    public void updateLastLogin() {
        this.userLastLogin = LocalDateTime.now();
    }
    
    public void softDelete() {
        this.userStatus = "deleted";
        this.userDeletedAt = LocalDateTime.now();
    }
    
    public void addTokens(int count) {
        this.userTokenCount += count;
    }
    
    public boolean useToken() {
        if (this.userTokenCount > 0) {
            this.userTokenCount--;
            return true;
        }
        return false;
    }
    
    // 정책 동의 관련 메서드들
    public void addPolicyAgreement(UserPolicyAgreement agreement) {
        this.policyAgreements.add(agreement);
        agreement.setUser(this);
    }
    
    public boolean hasAgreedToPolicy(Long policyId) {
        return policyAgreements.stream()
                .anyMatch(agreement -> agreement.getPolicyId().equals(policyId) && agreement.isAgreed());
    }
} 