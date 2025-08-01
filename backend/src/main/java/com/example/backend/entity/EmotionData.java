package com.example.backend.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;


import java.time.LocalDateTime;

@Entity
@Table(name = "emotion_data")
@Getter
@Setter
@NoArgsConstructor
public class EmotionData {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "emotion_id")
    private Long id;

    private String name;

    @Column(name = "created_at")
    private LocalDateTime createdAt;
}

