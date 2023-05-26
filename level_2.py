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
    kemunculan = [3, 5, 10, 15, 25, 30]
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("./assets/BG2.png").convert()
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

map_level2 = level2()
player_level2 = Player()
map_zombie = Zombies()
def play_level2():
    game_level2 = Deadshooter(map_level2, player_level2, map_zombie)
    game_level2.run()