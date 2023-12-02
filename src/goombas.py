import pygame
from pygame.locals import *
from config import *
from character import Character


class Goombas(Character):
    def __init__(self, groups, animations_dict: dict, movement: bool, life = 1) -> None:
        super().__init__(groups, animations_dict, life)
        self.movement = movement
        self.life = life
        self.speed = 2
        self.movement_right = True
        self.damage = 1

    def update(self):
        super().update()
        if self.movement_right and self.rect.left <= (WIDTH - self.speed):
            self.rect.x += self.speed
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite += 1
                self.image = self.animations["right"][self.current_sprite]
                if self.current_sprite == ((len(self.animations["right"])) - 1):
                    self.current_sprite = 0
                self.last_update = current_time
        else:
            self.movement_right = False
            
        if self.rect.right >= 0 and not self.movement_right:
            self.rect.x -= self.speed
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.time_animation:
                self.current_sprite += 1
                self.image = self.animations["left"][self.current_sprite]
                if self.current_sprite == ((len(self.animations["left"])) - 1):
                    self.current_sprite = 0
                self.last_update = current_time
        else:
            self.movement_right = True

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
