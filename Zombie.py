import pygame
from imageloader import imageloader

class Zombies:
	hp = 10

	def __init__(self):
		self.data_zombie = []
	def dead(self):
		pass
	def show(self, target):
		img_zombie = pygame.image.load("./assets/Zombie1.png").convert_alpha()
		img_zombie = pygame.transform.scale(img_zombie, (95, 90))
		for data in self.data_zombie:
			new_t = target.copy()
			target.blit(img_zombie, (data[0], data[1]))
			target = new_t
	def tambahzombie(self):
		self.data_zombie.append([720,380])

	def pergerakan_zombie(self):
		for zombie in self.data_zombie:
			zombie[0] -= 5
			if zombie[0]==0:
				self.data_zombie.remove(zombie)