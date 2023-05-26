import pygame
import sys
from pygame.locals import *
from imageloader import imageloader as imgres
from Player import Player
from Zombie import Zombies
from Deadshooter import Deadshooter
import os

class level3(pygame.sprite.Sprite):
    width = 850
    height = 500
    kemunculan = [2, 4, 8, 14, 16, 22, 26, 28, 32, 34, 38, 44, 46, 52, 56, 58, 62, 64, 68, 74, 76, 82, 86, 88, 92, 94, 98, 104, 106, 112, 116, 118, 122, 124, 128, 134, 136, 142, 146, 148, 152, 154, 158, 164, 166, 172, 176, 178, 182, 184, 188, 194, 196, 202, 206, 208, 212, 214, 218, 224, 226, 232, 236, 238]
    bonus = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240]
    level = "Level 3"
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("./assets/BG3.png").convert()
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.hp_zombie = 5
        self.score = 0

def play_level3():
    map_level3 = level3()
    player_level3 = Player()
    map_zombie = Zombies()
    game_level3 = Deadshooter(map_level3, player_level3, map_zombie)
    game_level3.run()