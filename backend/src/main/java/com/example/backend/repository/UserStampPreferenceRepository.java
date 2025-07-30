package com.example.backend.repository;

import com.example.backend.entity.UserStampPreference;
import com.example.backend.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface UserStampPreferenceRepository extends JpaRepository<UserStampPreference, Long> {
    Optional<UserStampPreference> findByUser(User user);
    Optional<UserStampPreference> findByUserUserId(Long userId);
    
    // ===================== NEW QUERY METHOD ADDED =====================
    // 2025-01-XX: 사용자 ID와 스탬프 이름으로 조회하는 메서드 추가
    // 현재 활성 스탬프를 찾기 위한 메서드
    Optional<UserStampPreference> findByUser_UserIdAndSelectedStampName(Long userId, String selectedStampName);
    // ===================== END NEW QUERY METHOD =====================
} 