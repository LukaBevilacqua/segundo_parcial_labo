import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from character import Character
from sounds import Sounds


class PlayableCharacter(Character):
    def __init__(self, groups, animations_dict: dict, x, y, projectile, life=1) -> None:
        super().__init__(groups, animations_dict, life)
        self.is_jumping = False
        self.jump_power = -15
        self.damage = 1
        self.speed = 3
        self.move_right = True
        self.move_left = True
        self.score = 0
        self.power_up = False
        self.power_up_time = 10000
        self.last_power_up_time = 0
        self.rect.topleft = (x, y)
        self.projectile = projectile
        self.jump_sound = Sounds()

        # Definir rectángulos para cada lado de Mario
        self.hitbox_top = pygame.Rect(x, y, 25, 5)
        self.hitbox_bottom = pygame.Rect(x, y + 20, 25, 5)
        self.hitbox_left = pygame.Rect(x, y, 5, 25)
        self.hitbox_right = pygame.Rect(x + 20, y, 5, 25)

    def update_hitboxes(self):
        self.hitbox_top.topleft = self.rect.topleft
        self.hitbox_bottom.topleft = (self.rect.left, self.rect.bottom - 5)
        self.hitbox_left.topleft = self.rect.topleft
        self.hitbox_right.topleft = (self.rect.right - 5, self.rect.top)
    
    def update(self):
        self.speed_v += GRAVITY
        self.rect.y += self.speed_v
        self.update_hitboxes()

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_v = 0
            self.is_jumping = False
        elif self.speed_v == 1:
            self.is_jumping = False
        else:
            self.is_jumping = True

        keys = pygame.key.get_pressed()
        if keys[K_d]:
            if self.rect.right <= WIDTH and self.move_right:
                self.rect.x += self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['right'][self.current_sprite]
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time
                if self.is_jumping:
                    self.image = self.animations['jump'][1]
        if keys[K_a]:
            if self.rect.x >= 0 and self.move_left:
                self.rect.x -= self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations['left'][self.current_sprite]
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time
                if self.is_jumping:
                    self.image = self.animations['jump'][0]
        if keys[K_w]:
            Press_button = True
            if not self.is_jumping and Press_button:
                self.jump()
                Press_button = False
        if keys[K_SPACE]:
                self.shoot()
    
    def jump(self):
        self.speed_v = self.jump_power
        self.jump_sound.jump_sound.play()

    
    def touch_flower(self, flower):
        if self.rect.colliderect(flower.rect):
            self.power_up = True
    
    def shoot(self):
        if self.power_up:
            pass

