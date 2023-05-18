import pygame
import sys
from pygame.locals import *
from imageloader import imageloader as imgres
from Player import Player
from Zombie import Zombie
from Deadshooter import Deadshooter
import os

class level2(pygame.sprite.Sprite):
    width = 850
    height = 500
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))

map_level2 = level2()
player_level2 = Player()
def play_level2():
    game_level2 = Deadshooter(map_level2, player_level2)
    game_level2.run()