import pygame
from pygame.locals import *

class Menu:
    def __init__(self, screen) -> None:
        self.screen = screen
    
    def show_text_button(self, text, x, y, font_size = 36, colour = (0, 0, 0)):
        self.font = pygame.font.SysFont("comicsans", font_size)
        self.render = self.font.render(str(text), True, colour)
        self.rect_text = self.render.get_rect()
        self.rect_text.center = (x, y)
        self.screen.blit(self.render, self.rect_text)
    
    def create_button(self, rect, text: str, colour_button: tuple, colour_hover: tuple):
        mouse_position = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_position):
            pygame.draw.rect(self.screen, colour_hover, rect, border_radius=10)
        else:
            pygame.draw.rect(self.screen, colour_button, rect, border_radius=10)
        self.show_text_button(self.screen, text, rect.centerx, rect.centery)

    def finish(self):
        import sys
        pygame.quit()
        sys.exit()
