import pygame
from pygame.locals import *

from config import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, rect: pygame.rect) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((rect[2], rect[3]))
        self.rect = self.image.get_rect(topleft = (rect[0], rect[1]))
        self.mask = pygame.mask.from_surface(self.image)
        self.image.fill(BLACK)