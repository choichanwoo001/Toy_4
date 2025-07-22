package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

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
    
    // 비즈니스 메서드들
    public void updatePolicy(String newDescription, String changedContent) {
        this.policyPrevDescription = this.policyDescription;
        this.policyDescription = newDescription;
        this.policyChangedContent = changedContent;
        this.policyUpdatedAt = LocalDateTime.now();
    }
    
    public boolean hasChangedContent() {
        return policyChangedContent != null && !policyChangedContent.trim().isEmpty();
    }
    
    public void addUserAgreement(UserPolicyAgreement agreement) {
        this.userAgreements.add(agreement);
        agreement.setPolicy(this);
    }
    
    public long getAgreementCount() {
        return userAgreements.stream()
                .filter(UserPolicyAgreement::isAgreed)
                .count();
    }
} 