from imageloader import imageloader

class Zombie:
	coor = [500, 350]
	hp = 10
	def dead(self):
		pass
	def show(self, target):
		posx, posy = self.coor[0], self.coor[1]
		imageloader().cleanimg(target, imageloader().zombie(), (posx, posy), 250)