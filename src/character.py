import pygame
from pygame.locals import *
from config import *
# from sprite_sheet import SpriteSheet
# from sprites import GetSprites


class Character(pygame.sprite.Sprite):
    def __init__(self, groups,animations_dict: dict, life = 1) -> None:
        super().__init__(groups)
        self.animations = animations_dict
        self.current_animation = "right"
        self.current_sprite = 0
        self.image = self.animations[self.current_animation][self.current_sprite]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 5
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 100
        self.life = life
        self.speed_v = 0

    def update(self):
        self.speed_v += GRAVITY
        self.rect.y += self.speed_v


