import pygame
import sys
from pygame.locals import *
from level_1 import Deadshooter
from level_2 import SecondLevel
from level_3 import ThirdLevel

class Settings:
    def __init__(self):
        self.mainClock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 20)
        self.click = False
        self.screen = pygame.display.set_mode((850, 500))
        self.bg = pygame.image.load("./assets/setting.png").convert()

        self.on_button_img = pygame.image.load(
            "./assets/on_button1.png"
        ).convert_alpha()
        self.on_button_hover_img = pygame.image.load("./assets/on_button2.png")
        self.off_button_img = pygame.image.load(
            "./assets/off_button1.png"
        ).convert_alpha()
        self.off_button_hover_img = pygame.image.load(
            "./assets/off_button2.png"
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

            on_music_button_rect = pygame.Rect(483, 223, 90, 60)
            off_music_button_rect = pygame.Rect(604, 223, 90, 60)
            on_effect_button_rect = pygame.Rect(483, 319, 90, 60)
            off_effect_button_rect = pygame.Rect(604, 319, 90, 60)

            self.draw_text("< esc", (255, 255, 255), 20, 20)

            if on_music_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.on_button_hover_img, on_music_button_rect)
                self.screen.blit(self.off_button_img, off_music_button_rect)
                # if self.click:
                    
            else:
                self.screen.blit(self.on_button_img, on_music_button_rect)
                self.screen.blit(self.off_button_hover_img, off_music_button_rect)

            if off_music_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.off_button_hover_img, off_music_button_rect)
                # if self.click:
                    
            else:
                self.screen.blit(self.off_button_img, off_music_button_rect)

            if on_effect_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.on_button_hover_img, on_effect_button_rect)
                # if self.click:
                    
            else:
                self.screen.blit(self.on_button_img, on_effect_button_rect)

            if off_effect_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.off_button_hover_img, off_effect_button_rect)
                # if self.click:
                    
            else:
                self.screen.blit(self.off_button_img, off_effect_button_rect)


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


if __name__ == "__main__":
    level = Settings()
    level.run()