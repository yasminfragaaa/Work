#!/usr/bin/python
# -*- coding: utf-8 -*-

from Game import Game
from Game import Game
from Game import Game
from Game import Game
from Player import Player
from Coin import Coin
from Enemy import Enemy


class Game(Game, Game, Game, Game, Player, Coin, Enemy):
    def __init__(self):
        self.screen_width = None
        self.screen_height = None
        self.score = None
        self.running = None
        self.coins = None
        self.enemies = None
        self.player = None
        self.menu = None

    def start(self, ):
        pass

    def update(self, ):
        pass

    def draw(self, ):
        pass

    def check_collision(self, ):
        pass

    def check_win(self, ):
        pass

    def check_lose(self, ):
        pass
