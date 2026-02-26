package com.example.monolithicapp.user.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.monolithicapp.user.entity.User;

public interface UserRepository extends JpaRepository<User, Long> {
}