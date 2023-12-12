import pygame
from pygame.locals import *
from menu import Menu
from config import *

class InitialMenu(Menu):
    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.background = pygame.transform.scale(pygame.image.load("./src/assets/images/backgrounds/prueba4.jpg"), SIZE_SCREEN)
        self.logo = pygame.image.load("./src/assets/images/logo/logo.png")
        self.song = pygame.mixer.Sound("./src/assets/sounds/main_menu.mp3")
        self.song.set_volume(0.3)

    def initial_menu(self, rect_1, text, colour, colour_hover, rect_2, text2, colour2, colour_hover2, rect_3, text3, color3, color_hover3):
        self.song.play(-1)
        while True:
            self.screen.blit(self.background, self.background.get_rect())
            self.screen.blit(self.logo, self.logo.get_rect(midtop = (CENTER_SCREEN[0], CENTER_SCREEN[1] // 2)))
            self.create_button(rect_1, text, colour, colour_hover)
            self.create_button(rect_2, text2, colour2, colour_hover2)
            self.create_button(rect_3, text3, color3, color_hover3)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if rect_1.collidepoint(event.pos):
                            self.song.stop()
                            return None
                        elif rect_3.collidepoint(event.pos):
                            self.finish()