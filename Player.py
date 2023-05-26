import pygame
from imageloader import imageloader


class Player:
    vel_y = 0
    graf = 1
    peluru_velo = 15
    offsetx = 100
    offsety = 30
    def __init__(self):
        self.proyektil_peluru = []
        self.isjump = False
        self.hp = 100
        self.jumlah_peluru = 100
        self.coor = [100, 350]
    def dead(self):
        pass

    def show(self, target):
        posx, posy = self.coor[0], self.coor[1]
        imageloader().cleanimg(target, imageloader().soldier(), (posx, posy), 250)

        for bullet in self.proyektil_peluru:
            pygame.draw.circle(target, (255, 0, 0), (int(bullet[0]), int(bullet[1])), 2)

    def jump(self):
        self.vel_y = -15
        self.isjump = True

    def gravitasi(self):
        if self.coor[1]<361:
            self.vel_y += self.graf
            self.coor[1] += self.vel_y
        elif self.coor[1]==350:
            self.isjump = False
    # Fitur tembak() masih error, jumlah peluru tidak berkurang meskipun sudah menembak
    def tembak(self):
        if self.jumlah_peluru > 0:
            # menambahkan posisi proyektil ke dalam list bullets
            self.proyektil_peluru.append([self.coor[0] + self.offsetx, self.coor[1] + self.offsety])
            self.jumlah_peluru -= 1
        else:
            # print("Peluru habis")
            pass
    
    def pergerakan_peluru(self, zombie):
        # menggerakkan proyektil ke atas
        for bullet in self.proyektil_peluru:
            bullet[0] += self.peluru_velo
            # menghapus proyektil yang sudah keluar layar
            if bullet[0] > 800:
                self.proyektil_peluru.remove(bullet)
            for coor in zombie.data_zombie:
                if bullet[0]==coor[0]+20 and not (bullet[1]<coor[1]):
                    print("terkena damage")
                    self.proyektil_peluru.remove(bullet)
                    zombie.data_zombie.remove(coor)
                    break
        # print(f"Jumlah Zombie: {zombie.data_zombie}")