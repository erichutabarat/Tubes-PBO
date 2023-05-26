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
    kemunculan = [3, 5, 10, 15, 25, 30]
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load("./assets/BG3.png").convert()
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

map_level3 = level3()
player_level3 = Player()
map_zombie = Zombies()
def play_level3():
    game_level3 = Deadshooter(map_level3, player_level3, map_zombie)
    game_level3.run()