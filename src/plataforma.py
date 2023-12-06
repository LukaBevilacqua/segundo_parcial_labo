import pygame
from pygame.locals import *

from config import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, groups, rect: pygame.rect, can_broke: bool = False, item: bool = False) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((rect[2], rect[3]))
        self.rect = self.image.get_rect(topleft = (rect[0], rect[1]))
        self.mask = pygame.mask.from_surface(self.image)
        self.image.fill(BLACK)
        self.can_broke = can_broke
        self.have_item = item

    def destroy(self, player):
        if self.can_broke:
            if self.rect.colliderect(player.hitbox_top):
                self.kill()

    def show_item(self, player, item):
        if self.have_item:
            if self.rect.colliderect(player.hitbox_top):
                item.found = True
                self.have_item = False