package com.example.backend.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "test_table")
public class TestEntity {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "message")
    private String message;
    
    @Column(name = "created_at")
    private String createdAt;
    
    public TestEntity() {}
    
    public TestEntity(String message, String createdAt) {
        this.message = message;
        this.createdAt = createdAt;
    }
    
    public Long getId() {
        return id;
    }
    
    public void setId(Long id) {
        this.id = id;
    }
    
    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
    
    public String getCreatedAt() {
        return createdAt;
    }
    
    public void setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
    }
} 