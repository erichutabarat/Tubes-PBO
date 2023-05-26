import pygame
import sys
from levelmain import LevelSelection
from setting import Settings

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Deadshooter")
        self.screen = pygame.display.set_mode((850, 500))
        self.mainClock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 20)
        self.click = False
        # Memulai background sound (Music)
        self.bg_music =  pygame.mixer.music.load("./assets/audio/bg_music.mp3")
        
        self.main_menu_bg = pygame.image.load("./assets/menu.png").convert()

        self.start_button_img = pygame.image.load(
            "./assets/start_button1.png"
        ).convert_alpha()
        self.start_button_hover_img = pygame.image.load("./assets/blank.png")
        self.level_button_img = pygame.image.load(
            "./assets/level_button1.png"
        ).convert_alpha()
        self.level_button_hover_img = pygame.image.load(
            "./assets/blank.png"
        ).convert_alpha()
        self.settings_button_img = pygame.image.load(
            "./assets/setting_button1.png"
        ).convert_alpha()
        self.settings_button_hover_img = pygame.image.load(
            "./assets/blank.png"
        ).convert_alpha()
        self.exit_button_img = pygame.image.load(
            "./assets/exit_button1.png"
        ).convert_alpha()
        self.exit_button_hover_img = pygame.image.load(
            "./assets/blank.png"
        ).convert_alpha()

    def main_menu(self):
        while True:
            self.screen.blit(self.main_menu_bg, (0, 0))
            pygame.mixer.music.play(-1)
            mx, my = pygame.mouse.get_pos()

            start_button_rect = pygame.Rect(139, 157, 225, 61)
            level_button_rect = pygame.Rect(138, 232, 225, 61)
            settings_button_rect = pygame.Rect(138, 303, 225, 61)
            exit_button_rect = pygame.Rect(139, 375, 225, 61)

            if start_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.start_button_hover_img,
                                 start_button_rect)
                if self.click:
                    self.level_selection()
            else:
                self.screen.blit(self.start_button_img, start_button_rect)

            if level_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.level_button_hover_img,
                                 level_button_rect)
                if self.click:
                    self.level_selection()
            else:
                self.screen.blit(self.level_button_img, level_button_rect)

            if settings_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.settings_button_hover_img,
                                 settings_button_rect)
                if self.click:
                    self.settings()
            else:
                self.screen.blit(self.settings_button_img,
                                 settings_button_rect)

            if exit_button_rect.collidepoint((mx, my)):
                self.screen.blit(self.exit_button_hover_img, exit_button_rect)
                if self.click:
                    pygame.quit()
                    sys.exit()
            else:
                self.screen.blit(self.exit_button_img, exit_button_rect)

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("left klik at", mx, my)
                        self.click = True

            pygame.display.update()
            self.mainClock.tick(60)

    def level_selection(self):
        level = LevelSelection()
        level.run()

    def settings(self):
        setting = Settings()
        setting.run()

if __name__ == "__main__":
    game = Game()
    game.main_menu()