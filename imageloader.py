import pygame
class imageloader:
	def cleanimg(self, target, src, loc, op):
		x = loc[0]
		y = loc[1]
		temp = pygame.Surface((src.get_width(), src.get_height()))
		temp.blit(target, (-x,-y))
		temp.blit(src, (0,0))
		temp.set_alpha(op)
		target.blit(temp,loc)
	def soldier(self):
		self.soldier_img = pygame.image.load("./assets/Soldier1.png")
		self.soldier_img = pygame.transform.scale(self.soldier_img, (120,100))
		return self.soldier_img

	def zombie(self):
		self.zombie_img = pygame.image.load("./assets/Zombie.png")
		self.zombie_img = pygame.transform.scale(self.zombie_img, (100, 80))
		return self.zombie_img

	def tanah(self):
		self.tanah_img = pygame.image.load("./assets/Tanah2.png")
		self.tanah_img = pygame.transform.scale(self.tanah_img, (128, 128))
		return self.tanah_img

	def show_tanah(self, target, posx):
		self.cleanimg(target, self.tanah(), (posx, 440), 250)