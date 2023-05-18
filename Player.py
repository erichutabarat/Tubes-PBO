import pygame
from imageloader import imageloader


class Player:
    hp = 100
    vel_y = 0
    graf = 1
    peluru_velo = 10
    offsetx = 100
    offsety = 30
    jumlah_peluru = 10
    def __init__(self):
        self.proyektil_peluru = []
        self.isjump = False
        self.jumlah_peluru = 10
        self.coor = [100, 361]
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
        elif self.coor[1]==361:
            self.isjump = False
    # Fitur tembak() masih error, jumlah peluru tidak berkurang meskipun sudah menembak
    def tembak(self):
        if self.jumlah_peluru>0:
            # menambahkan posisi proyektil ke dalam list bullets
            self.proyektil_peluru.append([self.coor[0]+self.offsetx, self.coor[1]+self.offsety])
            print(self.jumlah_peluru)
            self.jumlah_peluru = self.jumlah_peluru - 1
            self.jumlah_peluru = len(self.proyektil_peluru)
        else:
            print("Peluru habis")
    
    def pergerakan_peluru(self):
        # menggerakkan proyektil ke atas
        for bullet in self.proyektil_peluru:
            bullet[0] += self.peluru_velo
            # menghapus proyektil yang sudah keluar layar
            if bullet[0] > 800:
                self.proyektil_peluru.remove(bullet)