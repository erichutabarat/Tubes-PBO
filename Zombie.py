import pygame
from imageloader import imageloader

class Zombies:
	hp = 10

	def __init__(self):
		self.data_zombie = []

	def show(self, target):
		img_zombie = pygame.image.load("./assets/Zombie1.png").convert_alpha()
		img_zombie = pygame.transform.scale(img_zombie, (95, 90))
		for data in self.data_zombie:
			# new_t = target.copy()
			target.blit(img_zombie, (data[0], data[1]))
			# target = new_t
	def tambahzombie(self, id, hp):
		self.data_zombie.append([720,380, id, hp])

	def pergerakan_zombie(self, map, player):
		same_zombies = set()
		res = []
		for zombie in self.data_zombie:
			if zombie[2] not in same_zombies:
				res.append(zombie)
				same_zombies.add(zombie[2])
		self.data_zombie = res
		for zombie in self.data_zombie:
			zombie[0] -= 5
			if zombie[0]==0:
				self.data_zombie.remove(zombie)
				map.score += 1
			if zombie[0]==player.coor[0] and zombie[1]>player.coor[1]:
				player.hp -= 2