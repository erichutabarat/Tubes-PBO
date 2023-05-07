import pygame
import sys
from pygame.locals import *


class LevelSelection:
    def __init__(self):
        self.mainClock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 20)
        self.click = False
        self.screen = pygame.display.set_mode((850, 500))
        self.bg = pygame.image.load("./assets/level.png").convert()

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

    def run(self):
        running = True
        while running:
            self.screen.blit(self.bg, (0, 0))

            self.draw_text("Level", (255, 255, 255), 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            pygame.display.update()
            self.mainClock.tick(60)
