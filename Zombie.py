import pygame
from imageloader import imageloader

class Spritezombie(pygame.sprite.Sprite):
	def __init__(self, img, x, y):
		super().__init__()
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Zombies:
	hp = 10

	def __init__(self):
		self.data_zombie = []
	def dead(self):
		pass
	def show(self, target):
		img_zombie = pygame.image.load("./assets/Zombie.png").convert_alpha()
		img_zombie = pygame.transform.scale(img_zombie, (95, 90))
		group = pygame.sprite.Group()
		for data in self.data_zombie:
			# imageloader().cleanimg(target, imageloader().zombie(), (data[0], data[1]), 250)
			# new_t = target.copy()
			# target.blit(img_zombie, (data[0], data[1]))
			# target = new_t
			zombie_x = Spritezombie(img_zombie, data[0], data[1])
			group.add(zombie_x)
		group.draw(target)
	def tambahzombie(self):
		self.data_zombie.append([700,380])

	def pergerakan_zombie(self):
		for zombie in self.data_zombie:
			zombie[0] -= 2