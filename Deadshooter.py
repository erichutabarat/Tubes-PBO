from Player import Player
from Zombie import Zombies
from imageloader import imageloader
import pygame
import os, sys
class Deadshooter:
    velo = 10
    def __init__(self, map, playerx, zombiex):
        self.mainClock = map.mainClock
        self.screen = map.screen
        self.font = pygame.font.SysFont(None, 20)
        pygame.display.set_caption(" Dead Shooter ")
        self.bg = pygame.image.load("./assets/BG.png").convert()
        self.bg = pygame.transform.scale(self.bg, (map.width, map.height))
        self.playerx = playerx
        self.zombiex = zombiex
        self.can_jump = True
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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.playerx.coor[1]>270 and self.can_jump:
                self.playerx.coor[1] -= self.velo*2
                self.playerx.jump()
                self.can_Jump = False
            #Note Terjadi kelewatan batas kalo gravitasi + tombol bawah
            # if keys[pygame.K_DOWN] and self.playerx.coor[1] < 350:
            #     self.playerx.coor[1] += self.velo*2
            if keys[pygame.K_LEFT] and self.playerx.coor[0] > 0:
                self.playerx.coor[0] -= self.velo
            if keys[pygame.K_RIGHT] and self.playerx.coor[0] < 500:
                self.playerx.coor[0] += self.velo
            if keys[pygame.K_SPACE]:
                if self.playerx.jumlah_peluru>0:
                    self.playerx.tembak()
                else:
                    print("Peluru habis")
                

            self.playerx.gravitasi()
            self.playerx.pergerakan_peluru(self.zombiex)
            
            if self.playerx.coor[1]==361:
                self.can_jump = True
            
            # Memunculkan zombie baru di layar
            self.zombiex.tambahzombie()
            self.zombiex.pergerakan_zombie()


            self.showobj(self.screen, self.playerx, self.zombiex)            
            pygame.display.update()
            self.mainClock.tick(30)
    
    def showobj(self,target, player, zombie):
        player.show(target)
        zombie.show(target)