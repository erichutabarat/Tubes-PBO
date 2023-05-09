import pygame
import sys
from pygame.locals import *
from imageloader import imageloader as imgres
from Player import Player
from Zombie import Zombie
import os


class Deadshooter:
    width = 850
    height = 500
    velo = 10
    def __init__(self):
        pygame.init()
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont(None, 20)
        pygame.display.set_caption(" Dead Shooter ")
        self.bg = pygame.image.load("./assets/BG.png").convert()
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

    def run(self):
        running = True
        while running:
            pygame.time.delay(10)
            self.screen.blit(self.bg, (0, 0))
            self.draw_text("< esc", (255, 255, 255), 20, 20)

            # Event Keyboard
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and Player().coor[1] > 280 and Player().isjump==False:
                Player().coor[1] -= self.velo*2
                Player().jump()
            #Note Terjadi kelewatan batas kalo gravitasi + tombol bawah
            # if keys[pygame.K_DOWN] and Player().coor[1] < 350:
            #     Player().coor[1] += self.velo*2
            if keys[pygame.K_LEFT] and Player().coor[0] > 0:
                Player().coor[0] -= self.velo
            if keys[pygame.K_RIGHT] and Player().coor[0] < 500:
                Player().coor[0] += self.velo
            if keys[pygame.K_SPACE]:
                if Player().jumlah_peluru>0:
                    Player().tembak()
                else:
                    print("Peluru habis")
                

            # Hide sementara (fokus ke player)
            # Zombie().coor[0] -= self.velo-7
            Player().gravitasi()
            Player().pergerakan_peluru()
            Player().show(self.screen)
            # Hide sementara (fokus ke player)
            # Zombie().show(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            
            pygame.display.update()
            self.mainClock.tick(60)

if __name__ == "__main__":
    level_1 = Deadshooter()
    level_1.run()      