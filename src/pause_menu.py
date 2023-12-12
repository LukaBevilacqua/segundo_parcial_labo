import pygame
from pygame.locals import *
from menu import Menu
from config import *

class PauseMenu(Menu):
    def __init__(self, screen) -> None:
        super().__init__(screen)
        self.background = "sarasa"
        self.message = "Pause"
        self.paused = False

    def pause(self, rect_1, text, colour, colour_hover, rect_2, text2, colour2, colour_hover2):
        if self.paused:
            while True:
                self.show_text_button(self.message, CENTER_SCREEN[0], CENTER_SCREEN[1] // 2)
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
                    print(self.paused)
    
    def handler_pause(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused