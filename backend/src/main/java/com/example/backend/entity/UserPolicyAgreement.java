package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;

import java.time.LocalDateTime;

@Entity
@Table(name = "user_policy_agreement")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class UserPolicyAgreement {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "agreement_id")
    private Long agreementId;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "policy_id", nullable = false)
    private Policy policy;
    
    @CreationTimestamp
    @Column(name = "agreement_agreed_at", nullable = false, updatable = false)
    private LocalDateTime agreementAgreedAt;
    
    @Column(name = "agreement_is_agreed", nullable = false, length = 1)
    @Builder.Default
    private String agreementIsAgreed = "N";
    
    // 비즈니스 메서드들
    public boolean isAgreed() {
        return "Y".equals(agreementIsAgreed);
    }
    
    public void agree() {
        this.agreementIsAgreed = "Y";
        this.agreementAgreedAt = LocalDateTime.now();
    }
    
    public void disagree() {
        this.agreementIsAgreed = "N";
    }
    
    public Long getUserId() {
        return user != null ? user.getUserId() : null;
    }
    
    public Long getPolicyId() {
        return policy != null ? policy.getPolicyId() : null;
    }
} 