#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

class Player:
    def __init__(self):
        self.x = 50
        self.y = 300

        self.width = 40
        self.height = 40

        self.speed = 3

        self.velocity_y = 0
        self.jump_force = -12
        self.gravity = 0.5
        self.on_ground = False
        self.facing_right = True

        self.idle_frames = [
            pygame.transform.scale(pygame.image.load('./asset/idle1.png'), (40, 40)),
            pygame.transform.scale(pygame.image.load('./asset/idle2.png'), (40, 40)),
            pygame.transform.scale(pygame.image.load('./asset/idle3.png'), (40, 40)),
            pygame.transform.scale(pygame.image.load('./asset/idle4.png'), (40, 40))
        ]

        self.run_frames = [
            pygame.transform.scale(pygame.image.load('./asset/run1.png'), (40, 40)),
            pygame.transform.scale(pygame.image.load('./asset/run2.png'), (40, 40)),
            pygame.transform.scale(pygame.image.load('./asset/run3.png'), (40, 40)),
            pygame.transform.scale(pygame.image.load('./asset/run4.png'), (40, 40))
        ]

        self.jump_frames = [
            pygame.transform.scale(pygame.image.load('./asset/jump1.png'), (40, 40)),
            pygame.transform.scale(pygame.image.load('./asset/jump2.png'), (40, 40))
        ]

        self.animation_index = 0
        self.animation_timer = 0
        self.current_frames = self.idle_frames

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.facing_right = False

        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.facing_right = True

        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.current_frames = self.run_frames
        else:
            self.current_frames = self.idle_frames


    def apply_gravity(self):
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        if self.y + self.height >= 400:
            self.y = 400 - self.height
            self.velocity_y = 0
            self.on_ground = True

    def draw(self, window):
        self.animation_timer += 1

        if self.animation_timer >= 10:
            self.animation_index += 1
            self.animation_timer = 0

        if self.animation_index >= len(self.current_frames):
            self.animation_index = 0

        image_to_draw = self.current_frames[self.animation_index]

        if not self.facing_right:
            image_to_draw = pygame.transform.flip(image_to_draw, True, False)

        window.blit(image_to_draw, (self.x, self.y))
