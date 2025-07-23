package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * 정책 정보를 담는 JPA 엔티티 클래스
 * 시스템의 다양한 정책(이용약관, 개인정보처리방침 등)을 관리
 */
@Entity
@Table(name = "policy")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Policy {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "policy_id")
    private Long policyId;
    
    @Column(name = "policy_name", nullable = false, length = 100)
    private String policyName;
    
    @Column(name = "policy_description", columnDefinition = "TEXT")
    private String policyDescription;
    
    @Column(name = "policy_prev_description", columnDefinition = "TEXT")
    private String policyPrevDescription;
    
    @Column(name = "policy_changed_content", columnDefinition = "TEXT")
    private String policyChangedContent;
    
    @Column(name = "policy_updated_at")
    private LocalDateTime policyUpdatedAt;
    
    @CreationTimestamp
    @Column(name = "policy_created_at", nullable = false, updatable = false)
    private LocalDateTime policyCreatedAt;
    
    @OneToMany(mappedBy = "policy", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    @Builder.Default
    private List<UserPolicyAgreement> userAgreements = new ArrayList<>();
    
    /**
     * 정책 내용을 업데이트하는 메서드
     * 기존 설명을 이전 설명으로 저장하고 새로운 설명과 변경 내용을 설정
     * @param newDescription 새로운 정책 설명
     * @param changedContent 변경된 내용
     */
    public void updatePolicy(String newDescription, String changedContent) {
        this.policyPrevDescription = this.policyDescription;
        this.policyDescription = newDescription;
        this.policyChangedContent = changedContent;
        this.policyUpdatedAt = LocalDateTime.now();
    }
    
    /**
     * 정책에 변경된 내용이 있는지 확인하는 메서드
     * @return 변경된 내용이 있으면 true, 없으면 false
     */
    public boolean hasChangedContent() {
        return policyChangedContent != null && !policyChangedContent.trim().isEmpty();
    }
    
    /**
     * 정책에 사용자 동의 정보를 추가하는 메서드
     * 양방향 관계를 설정하여 정책과 사용자 동의를 연결
     * @param agreement 추가할 사용자 정책 동의 정보
     */
    public void addUserAgreement(UserPolicyAgreement agreement) {
        this.userAgreements.add(agreement);
        agreement.setPolicy(this);
    }
    
    /**
     * 이 정책에 동의한 사용자 수를 반환하는 메서드
     * @return 동의한 사용자 수
     */
    public long getAgreementCount() {
        return userAgreements.stream()
                .filter(UserPolicyAgreement::isAgreed)
                .count();
    }
} 