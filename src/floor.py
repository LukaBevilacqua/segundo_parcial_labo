import pygame
from pygame.locals import *
from config import *
from plataforma import Platform

class Floor(Platform):
    def __init__(self, groups, rect: pygame.rect, can_broke: bool = False, item: bool = False) -> None:
        super().__init__(groups, rect, can_broke, item)

        self.image = pygame.transform.scale(pygame.image.load("./src/assets/images/blocks/floor.png").convert_alpha(),
                                                (self.rect[2], self.rect[3]))