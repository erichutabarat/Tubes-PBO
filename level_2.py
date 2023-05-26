import pygame
import sys
from pygame.locals import *
from imageloader import imageloader as imgres
from Player import Player
from Zombie import Zombies
from Deadshooter import Deadshooter
import os

class level2(pygame.sprite.Sprite):
    width = 850
    height = 500
    kemunculan = [3, 6, 9, 12, 15, 18, 21, 24, 27, 33, 36, 39, 42, 45, 48, 51, 54, 57, 63, 66, 69, 72, 75, 78, 81, 84, 87, 93, 96, 99, 102, 105, 108, 111, 114, 117, 123, 126, 129, 132, 135, 138, 141, 144, 147, 153, 156, 159, 162, 165, 168, 171, 174, 177]
    bonus = [20, 40, 60, 80, 100, 120, 140, 160, 180]
    level = "Level 2"
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("./assets/BG2.png").convert()
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.hp_zombie = 2
        self.score = 0

def play_level2():
    map_level2 = level2()
    player_level2 = Player()
    map_zombie = Zombies()
    game_level2 = Deadshooter(map_level2, player_level2, map_zombie)
    game_level2.run()