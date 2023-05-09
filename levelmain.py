import pygame
import sys
from pygame.locals import *
from level_1 import Deadshooter
from level_2 import SecondLevel
from level_3 import ThirdLevel

class LevelSelection:
    def __init__(self):
        self.mainClock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 20)
        self.click = False
        self.screen = pygame.display.set_mode((850, 500))
        self.bg = pygame.image.load("./assets/level.png").convert()

        self.level_1_button_img = pygame.image.load(
            "./assets/level_1_button.png"
        ).convert_alpha()
        self.level_1_button_hover_img = pygame.image.load("./assets/blank.png")
        self.level_2_button_img = pygame.image.load(
            "./assets/level_2_button.png"
        ).convert_alpha()
        self.level_2_button_hover_img = pygame.image.load(
            "./assets/blank.png"
        ).convert_alpha()
        self.level_3_button_img = pygame.image.load(
            "./assets/level_3_button.png"
        ).convert_alpha()
        self.level_3_button_hover_img = pygame.image.load(
            "./assets/blank.png"
        ).convert_alpha()

    def draw_text(self, text, color, x, y):
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self.screen.blit(textobj, textrect)

    def run(self):
        running = True
        while running:
            self.screen.blit(self.bg, (0, 0))
            
            mx, my = pygame.mouse.get_pos()

            level_1_button_rect = pygame.Rect(312, 170, 225, 61)
            level_2_button_rect = pygame.Rect(312, 256, 225, 61)
            level_3_button_rect = pygame.Rect(312, 342, 225, 61)

            self.draw_text("< esc", (255, 255, 255), 20, 20)

            if level_1_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.level_1_button_hover_img, level_1_button_rect)
                if self.click:
                    self.first_level()
            else:
                self.screen.blit(self.level_1_button_img, level_1_button_rect)

            if level_2_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.level_2_button_hover_img, level_2_button_rect)
                if self.click:
                    self.second_level()
            else:
                self.screen.blit(self.level_2_button_img, level_2_button_rect)

            if level_3_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.level_3_button_hover_img, level_3_button_rect)
                if self.click:
                    self.thrid_level()
            else:
                self.screen.blit(self.level_3_button_img, level_3_button_rect)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("left klik at", mx, my)
                        self.click = True

            pygame.display.update()
            self.mainClock.tick(60)

    def first_level(self):
        level_1 = Deadshooter()
        level_1.run()
        self.click = False 

    def second_level(self):
        level_2 = SecondLevel()
        level_2.run()
        self.click = False 

    def thrid_level(self):
        level_3 = ThirdLevel()
        level_3.run()
        self.click = False 

if __name__ == "__main__":
    level = LevelSelection()
    level.run()