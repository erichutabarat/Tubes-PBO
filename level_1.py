import pygame
import sys
from pygame.locals import *
from imageloader import imageloader as imgres
from Player import Player
from Zombie import Zombie
from Deadshooter import Deadshooter
import os

class level1(pygame.sprite.Sprite):
    width = 850
    height = 500
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))

map_level1 = level1()

def play_level1():
    game_level1 = Deadshooter(map_level1)
    game_level1.run()