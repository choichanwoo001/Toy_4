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
} 