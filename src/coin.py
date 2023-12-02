from typing import Any
import pygame
from pygame.locals import *
from config import *
from sprites import get_animation_coins

class Coin(pygame.sprite.Sprite):
    def __init__(self, groups, where: tuple) -> None:
        super().__init__(groups)
        self.animations = get_animation_coins()
        self.current_animation = "right"
        self.current_sprite = 0
        self.image = self.animations[self.current_animation][self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = where
        self.mask = pygame.mask.from_surface(self.image)
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 100

    def update(self) -> None:
        self.animate()

    def animate(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.time_animation:
            self.current_sprite += 1
            self.image = self.animations[self.current_animation][self.current_sprite]
            if self.current_sprite == ((len(self.animations[self.current_animation])) - 1):
                self.current_sprite = 0
            self.last_update = current_time


