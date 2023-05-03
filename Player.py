import pygame
from imageloader import imageloader
class Player:
	coor = [100, 350]
	hp = 100
	def dead(self):
		pass
	def show(self, target):
		posx, posy = self.coor[0], self.coor[1] 
		imageloader().cleanimg(target, imageloader().soldier(), (posx, posy), 250)
