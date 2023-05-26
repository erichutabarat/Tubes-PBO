import pygame
import sys
from pygame.locals import *
from imageloader import imageloader as imgres
from Player import Player
from Zombie import Zombies
from Deadshooter import Deadshooter
import os

class level1(pygame.sprite.Sprite):
    width = 850
    height = 500
    kemunculan = [4, 8, 12, 16, 24, 28, 32, 36, 44, 48, 52, 56, 64, 68, 72, 76, 84, 88, 92, 96, 104, 108, 112, 116, 124, 128, 132, 136, 144, 148, 152, 156, 164, 168, 172, 176]
    bonus = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]
    level = "Level 1"
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("./assets/BG1.png").convert()
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.hp_zombie = 1
        self.score = 0

def play_level1():
    map_level1 = level1()
    player_level1 = Player()
    map_zombie = Zombies()
    game_level1 = Deadshooter(map_level1, player_level1, map_zombie)
    game_level1.run()