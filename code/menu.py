#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.examples.grid import WINDOW_WIDTH
from pygame.font import Font


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/menusky.png')
        self.surf = pygame.transform.scale(self.surf, (600,400))
        self.rect = self.surf.get_rect(left=0, top = 0)

    def show(self):
        pygame.mixer.music.load('./asset/menu music.wav')
        pygame.mixer.music.play(-1)

        MENU_OPTION = ("START", "EXIT")
        selected_option = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(50, "Collect", (255, 253, 85), ((600 / 2), 70))
            self.menu_text(50, "Coins", (255, 253, 85), ((600 / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == selected_option:
                    cor = (255, 253, 85)  # amarelo
                else:
                    cor = (255, 255, 255)  # branco

                self.menu_text(
                    30,
                    MENU_OPTION[i],
                    cor,
                    ((600 / 2), 250 + 40 * i)
                )

                self.menu_text(18, "Controles:", (255, 255, 255), ((600 / 2), 330))
                self.menu_text(16, "Setas - mover", (255, 255, 255), ((600 / 2), 350))
                self.menu_text(16, "SPACE - pular", (255, 255, 255), ((600 / 2), 370))
                self.menu_text(16, "ESC - sair", (255, 255, 255), ((600 / 2), 390))

            pygame.display.flip()

            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        selected_option += 1
                        if selected_option >= len(MENU_OPTION):
                            selected_option = 0

                    if event.key == pygame.K_UP:
                        selected_option -= 1
                        if selected_option < 0:
                            selected_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        if selected_option == 0:
                            return

                        elif selected_option == 1:
                            pygame.quit()
                            quit()





    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name = "Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def show_game_over(self, ):
        pass

    def show_win(self, ):
        pass
