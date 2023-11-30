import pygame
from pygame.locals import *
from menu import Menu

class InitialMenu(Menu):
    def __init__(self, screen) -> None:
        super().__init__(screen)

    def initial_menu(self, rect_1, colour, colour_hover, text, rect_2, text2, colour2, colour_hover2):
        while True:
            self.create_button(rect_1, text, colour, colour_hover)
            self.create_button(rect_2, text2, colour2, colour_hover2)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finish()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if rect_1.collidepoint(event.pos):
                            return None
                        elif rect_2.collidepoint(event.pos):
                            self.finish()