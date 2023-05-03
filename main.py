import pygame
from imageloader import imageloader as imgres
from Player import Player
from Zombie import Zombie
import os

class Deadshooter:
	width = 850
	height = 500
	velo = 5
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(" Dead Shooter ")
		self.bg = pygame.image.load("./assets/BG.png").convert()
		self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

	def running(self):
		self.running = True
		while self.running:
			pygame.time.delay(100)
			self.screen.blit(self.bg, (0,0))
			Player().show(self.screen)
			Zombie().show(self.screen)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					self.running = False

			# Event Keyboard
			keys = pygame.key.get_pressed()
			if keys[pygame.K_UP] and Player().coor[1]>0:
				Player().coor[1] -= self.velo
			if keys[pygame.K_DOWN] and Player().coor[1]<400:
				Player().coor[1] += self.velo
			if keys[pygame.K_LEFT] and Player().coor[0]>0:
				Player().coor[0] -= self.velo
			if keys[pygame.K_RIGHT] and Player().coor[0]<500:
				Player().coor[0] += self.velo
			Zombie().coor[0] -= self.velo
			pygame.display.update()
	def exit(self):
		pygame.quit()


Games = Deadshooter()
Games.running()
Games.exit()