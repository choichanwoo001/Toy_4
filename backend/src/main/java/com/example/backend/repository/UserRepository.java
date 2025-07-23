package com.example.backend.repository;

import com.example.backend.entity.User;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
<<<<<<< HEAD
    Optional<User> findById(Long userId);
=======
    
    // 이메일로 사용자 찾기
    Optional<User> findByUserEmail(String userEmail);
    
    // 이메일 중복 확인
    boolean existsByUserEmail(String userEmail);
    
    // 카카오 ID로 사용자 찾기
    Optional<User> findByUserKakaoId(String userKakaoId);
    
    // 활성 사용자만 찾기
    @Query("SELECT u FROM User u WHERE u.userEmail = :email AND u.userStatus = 'active' AND u.userDeletedAt IS NULL")
    Optional<User> findActiveUserByEmail(@Param("email") String email);
    
    // 닉네임으로 사용자 찾기
    Optional<User> findByUserNickname(String userNickname);
    
    // 닉네임 중복 확인
    boolean existsByUserNickname(String userNickname);
>>>>>>> 2c3cad3b95ba29e203fe11274a75f45e2c7a702f
} 