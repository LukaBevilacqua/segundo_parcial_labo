import pygame
from pygame.locals import *
from config import *


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, belongs) -> None:
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load("./src/assets/images/items/flower.png").convert_alpha(), SIZE_PLAYER)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.hide = True
        self.found = False
        self.speed_v = 0
        self.belongs = belongs

    def update(self):
        if self.found:
            self.speed_v += GRAVITY
            self.rect.y += self.speed_v
            self.stay()
            if self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT
                self.speed_v = 0

    def stay(self):
        if self.rect.colliderect(self.belongs.rect):
            self.rect.bottom = self.belongs.rect.top

    def show_power_up(self):
        if self.found:
            self.hide = False
            self.speed_v -= 5
            if self.speed_v == -25:
                self.speed_v = 0
                self.stay()
