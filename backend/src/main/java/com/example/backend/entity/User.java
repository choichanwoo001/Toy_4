package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * 사용자 정보를 담는 JPA 엔티티 클래스
 * 사용자의 기본 정보, 인증 정보, 상태 정보를 관리
 */
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
    
    /**
     * 사용자가 활성 상태인지 확인하는 메서드
     * @return 활성 상태이면 true, 아니면 false
     */
    public boolean isActive() {
        return "active".equals(userStatus) && userDeletedAt == null;
    }
    
    /**
     * 사용자가 정지 상태인지 확인하는 메서드
     * @return 정지 상태이면 true, 아니면 false
     */
    public boolean isSuspended() {
        return "suspended".equals(userStatus);
    }
    
    /**
     * 로그인 실패 횟수를 증가시키는 메서드
     */
    public void incrementFailedLogin() {
        this.userFailedLogin++;
    }
    
    /**
     * 로그인 실패 횟수를 초기화하는 메서드
     */
    public void resetFailedLogin() {
        this.userFailedLogin = 0;
    }
    
    /**
     * 마지막 로그인 시간을 현재 시간으로 업데이트하는 메서드
     */
    public void updateLastLogin() {
        this.userLastLogin = LocalDateTime.now();
    }
    
    /**
     * 사용자를 소프트 삭제하는 메서드
     * 상태를 'deleted'로 변경하고 삭제 시간을 기록
     */
    public void softDelete() {
        this.userStatus = "deleted";
        this.userDeletedAt = LocalDateTime.now();
    }
    
    /**
     * 사용자에게 토큰을 추가하는 메서드
     * @param count 추가할 토큰 개수
     */
    public void addTokens(int count) {
        this.userTokenCount += count;
    }
    
    /**
     * 사용자의 토큰을 사용하는 메서드
     * @return 토큰 사용 성공 시 true, 토큰 부족 시 false
     */
    public boolean useToken() {
        if (this.userTokenCount > 0) {
            this.userTokenCount--;
            return true;
        }
        return false;
    }
    
    /**
     * 사용자에게 정책 동의 정보를 추가하는 메서드
     * @param agreement 추가할 정책 동의 정보
     */
    public void addPolicyAgreement(UserPolicyAgreement agreement) {
        this.policyAgreements.add(agreement);
        agreement.setUser(this);
    }
    
    /**
     * 사용자가 특정 정책에 동의했는지 확인하는 메서드
     * @param policyId 확인할 정책 ID
     * @return 동의했으면 true, 아니면 false
     */
    public boolean hasAgreedToPolicy(Long policyId) {
        return policyAgreements.stream()
                .anyMatch(agreement -> agreement.getPolicyId().equals(policyId) && agreement.isAgreed());
    }
} 