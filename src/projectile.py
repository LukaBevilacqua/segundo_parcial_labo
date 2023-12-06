import pygame



class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction) -> None:
        super().__init__()
        self.suface = pygame.transform.scale(pygame.image.load("./src/assets/images/player/fireball/fire_ball_player.png").convert_alpha(), (30, 50))
        self.rect = self.suface.get_rect()
        self.rect.x = x
        self.rect.centery = y
        self.direction = direction

    def update(self):
        if self.direction == "right":
            self.rect.x += 10
        else:
            self.rect.x -= 10
            
