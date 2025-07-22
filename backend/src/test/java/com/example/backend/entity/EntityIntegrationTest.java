package com.example.backend.entity;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase.Replace;
import org.springframework.test.annotation.Rollback;

import com.example.backend.repository.*;

import java.time.LocalDateTime;

import static org.assertj.core.api.Assertions.*;

@DataJpaTest
@AutoConfigureTestDatabase(replace = Replace.NONE)
@Rollback(false) // 실제 DB 반영 확인용
public class EntityIntegrationTest {
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private DiaryRepository diaryRepository;
    @Autowired
    private StampRepository stampRepository;

    @Test
    void userEntitySaveAndFind() {
        User user = new User();
        user.setUserEmail("test2@example.com");
        user.setUserPassword("pw");
        user.setUserNickname("테스트2");
        user.setUserPhone("010-0000-0000");
        user.setUserStatus("active");
        User saved = userRepository.save(user);
        User found = userRepository.findById(saved.getUserId()).orElse(null);
        assertThat(found).isNotNull();
        assertThat(found.getUserEmail()).isEqualTo("test2@example.com");
    }

    @Test
    void stampEntitySaveAndFind() {
        Stamp stamp = new Stamp();
        stamp.setName("테스트스탬프");
        stamp.setImage("/images/test.png");
        stamp.setPrice(100);
        stamp.setDescription("설명");
        stamp.setStatus("판매중");
        stamp.setSalesAt(LocalDateTime.now());
        Stamp saved = stampRepository.save(stamp);
        Stamp found = stampRepository.findById(saved.getStampId()).orElse(null);
        assertThat(found).isNotNull();
        assertThat(found.getName()).isEqualTo("테스트스탬프");
    }

    @Test
    void diaryEntitySaveAndFind() {
        User user = userRepository.findAll().stream().findFirst().orElse(null);
        assertThat(user).isNotNull();
        Diary diary = new Diary();
        diary.setUser(user);
        diary.setCreatedAt(LocalDateTime.now());
        diary.setContent("오늘의 일기");
        diary.setAppliedStamp("기본 스탬프");
        Diary saved = diaryRepository.save(diary);
        Diary found = diaryRepository.findById(saved.getDiaryId()).orElse(null);
        assertThat(found).isNotNull();
        assertThat(found.getContent()).isEqualTo("오늘의 일기");
    }
} 