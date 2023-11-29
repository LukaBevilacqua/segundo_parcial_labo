import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet


class Player(pygame.sprite.Sprite):
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
        self.jump_power = -15
        self.is_jumping = False

    def update(self):
        self.speed_v += GRAVITY
        self.rect.y += self.speed_v

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_v = 0
            self.is_jumping = False
        else:
            self.is_jumping = True

        keys = pygame.key.get_pressed()
        if keys[K_d]:
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["right"][self.current_sprite]
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time
        if keys[K_a]:
            if self.rect.x >= 0:
                self.rect.x -= self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["left"][self.current_sprite]
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time
        if keys[K_SPACE]:
            if not self.is_jumping:
                self.jump()

    def jump(self):
        self.speed_v = self.jump_power