import pygame
import sys
from pygame.locals import *


class SecondLevel:
    def __init__(self):
        self.mainClock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 20)
        self.click = False
        self.screen = pygame.display.set_mode((850, 500))
   

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

    def run(self):
        running = True
        while running:
            #self.screen.blit(self.bg, (0, 0))

            self.draw_text("level 2", (255, 255, 255), 20, 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        #print("left klik at", mx, my)
                        self.click = True

            pygame.display.update()
            self.mainClock.tick(60)
