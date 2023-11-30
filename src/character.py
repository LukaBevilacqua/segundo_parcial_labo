import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet


class Character(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet : SpriteSheet, life) -> None:
        super().__init__(groups)
        self.animations = sprite_sheet.get_animations_dict()
        self.current_sprite = 0
        self.image = self.animations["right"][self.current_sprite]
        self.rect = self.image.get_rect(topleft = (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 100
        self.life = life
        self.speed_v = 0

    def update(self):
        self.speed_v += GRAVITY
        self.rect.y += self.speed_v

