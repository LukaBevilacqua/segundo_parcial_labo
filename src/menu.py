import pygame
from pygame.locals import *

class Menu:
    def __init__(self, screen) -> None:
        self.screen = screen
    
    def finish(self):
        import sys
        pygame.quit()
        sys.exit()

    def show_text_button(self, text, x, y, font_size = 36, colour = (0, 0, 0)):
        font = pygame.font.SysFont("comicsans", font_size)
        render = font.render(str(text), True, colour)
        rect_text = render.get_rect(center = (x, y))
        self.screen.blit(render, rect_text)
    
    def create_button(self, rect, text: str, colour_button: tuple, colour_hover: tuple):
        mouse_position = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_position):
            pygame.draw.rect(self.screen, colour_hover, rect, border_radius=10)
        else:
            pygame.draw.rect(self.screen, colour_button, rect, border_radius=10)
        self.show_text_button(self.screen, text, rect.centerx, rect.centery)

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