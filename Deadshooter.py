from Player import Player
from Zombie import Zombie
from imageloader import imageloader
import pygame
import os, sys
class Deadshooter:
    velo = 10
    def __init__(self, map):
        self.mainClock = map.mainClock
        self.screen = map.screen
        self.font = pygame.font.SysFont(None, 20)
        pygame.display.set_caption(" Dead Shooter ")
        self.bg = pygame.image.load("./assets/BG.png").convert()
        self.bg = pygame.transform.scale(self.bg, (map.width, map.height))

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
            for x in range(0, 7):
                imageloader().show_tanah(self.screen, int(0+x*128))
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            pygame.display.update()
            self.mainClock.tick(60)