#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.menu import Menu
from code.player import Player

class Game:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.score = 0
        self.running = True
        self.win = False
        self.game_over = False
        self.time_limit = 15
        self.start_time = pygame.time.get_ticks()
        self.coins = [
            pygame.Rect(70, 300, 20, 20),
            pygame.Rect(180, 250, 20, 20),
            pygame.Rect(300, 200, 20, 20),
            pygame.Rect(420, 150, 20, 20),
            pygame.Rect(520, 220, 20, 20),
            pygame.Rect(200, 110, 20, 20),
            pygame.Rect(80, 350, 20, 20),
            pygame.Rect(260, 350, 20, 20),
            pygame.Rect(460, 350, 20, 20)
        ]
        self.enemies = []
        self.player = Player()
        self.platforms = [
            pygame.Rect(40, 330, 100, 20),
            pygame.Rect(150, 280, 90, 20),
            pygame.Rect(270, 230, 90, 20),
            pygame.Rect(390, 180, 90, 20),
            pygame.Rect(500, 250, 80, 20),
            pygame.Rect(180, 140, 80, 20)
        ]
        self.menu = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 400))
        self.grass_image = pygame.image.load('./asset/grama.png')
        self.grass_image = pygame.transform.scale(self.grass_image, (100, 20))

        self.coin_frames = [
            pygame.transform.scale(pygame.image.load('./asset/coin1.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin2.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin3.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin4.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin5.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin6.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin7.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin8.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin9.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin10.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin11.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin12.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin13.png'), (28, 28)),
            pygame.transform.scale(pygame.image.load('./asset/coin14.png'), (28, 28))
        ]

        self.coin_frame_index = 0
        self.coin_animation_timer = 0

        self.background = pygame.image.load('./asset/bg game.png')
        self.background = pygame.transform.scale(self.background, (600, 400))

        self.ground_image = pygame.image.load('./asset/grama2.png')
        self.ground_image = pygame.transform.scale(self.ground_image, (600, 80))

        self.coin_sound = pygame.mixer.Sound('./asset/coin sound.wav')

    def start(self):
        clock = pygame.time.Clock()

        menu = Menu(self.window)
        menu.show()

        while self.running:
            self.update()
            self.draw()
            clock.tick(60)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.on_ground:
                    self.player.velocity_y = self.player.jump_force
                    self.player.on_ground = False

        if self.game_over or self.win:
            return

        self.player.move()
        self.player.apply_gravity()


        player_rect = pygame.Rect(
            self.player.x,
            self.player.y,
            self.player.width,
            self.player.height
        )

        for platform in self.platforms:
            if player_rect.colliderect(platform) and self.player.velocity_y >= 0:
                if player_rect.bottom <= platform.top + 15:
                    self.player.y = platform.top - self.player.height
                    self.player.velocity_y = 0
                    self.player.on_ground = True

        for coin in self.coins[:]:
            if player_rect.colliderect(coin):
                self.coins.remove(coin)
                self.score += 1
                self.coin_sound.play()

        self.check_win()
        self.check_lose()

    def draw(self):
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.ground_image, (0, 390))

        # DESENHAR PLATAFORMAS
        for platform in self.platforms:
            grass = pygame.transform.scale(
                self.grass_image,
                (platform.width, platform.height)
            )
            self.window.blit(grass, (platform.x, platform.y))

        # ANIMAR MOEDAS (FORA do loop das plataformas)
        self.coin_animation_timer += 1

        if self.coin_animation_timer >= 4:
            self.coin_frame_index += 1
            self.coin_animation_timer = 0

        if self.coin_frame_index >= len(self.coin_frames):
            self.coin_frame_index = 0

        current_coin = self.coin_frames[self.coin_frame_index]

        # DESENHAR MOEDAS
        for coin in self.coins:
            self.window.blit(current_coin, (coin.x, coin.y))

        # PLAYER
        self.player.draw(self.window)

        # SCORE
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.window.blit(score_text, (20, 20))

        # TIMER
        elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
        remaining = max(0, int(self.time_limit - elapsed))
        timer_text = font.render(f"Time: {remaining}", True, (0, 0, 0))
        self.window.blit(timer_text, (450, 20))

        # WIN / LOSE
        if self.win:
            font = pygame.font.SysFont(None, 72)
            win_text = font.render("YOU WIN!", True, (255, 215, 0))
            text_rect = win_text.get_rect(center=(300, 200))
            self.window.blit(win_text, text_rect)

        elif self.game_over:
            font = pygame.font.SysFont(None, 72)
            lose_text = font.render("GAME OVER", True, (255, 0, 0))
            text_rect = lose_text.get_rect(center=(300, 200))
            self.window.blit(lose_text, text_rect)

        pygame.display.flip()



    def check_collision(self,):
        pass

    def check_win(self):
        if len(self.coins) == 0 and not self.game_over:
            self.win = True

    def check_lose(self):
        elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
        remaining = self.time_limit - elapsed

        if remaining <= 0 and not self.win:
            self.game_over = True
