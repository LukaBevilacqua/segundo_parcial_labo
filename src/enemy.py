import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from character import Character

class Enemy(Character):
    def __init__(self, groups, sprite_sheet: SpriteSheet, movement: bool, shoot: bool, life = 1) -> None:
        super().__init__(groups, sprite_sheet, life)
        self.movement = movement
        self.life = life
        self.speed = 2
        self.movement_right = True
        self.can_shoot = shoot
        self.damage = 1

    def update(self):
        super().update()
        if self.movement:
            if self.movement_right and self.rect.left <= (WIDTH - self.speed):
                self.rect.x += self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["right"][self.current_sprite]
                    if self.current_sprite == 8:
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
                    if self.current_sprite == 8:
                        self.current_sprite = 0
                    self.last_update = current_time
            else:
                self.movement_right = True

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    
    # def shoot(self, list):
    #     projectile = 