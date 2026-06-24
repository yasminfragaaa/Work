#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.score = 0
        self.running = True
        self.coins = []
        self.enemies = []
        self.player = None
        self.menu = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 400))

    def start(self):

        while True:
            menu = Menu(self.window)
            menu.show()
            pass
            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

    def update(self,):
        pass

    def draw(self,):
        pass

    def check_collision(self,):
        pass

    def check_win(self,):
        pass

    def check_lose(self, ):
        pass
