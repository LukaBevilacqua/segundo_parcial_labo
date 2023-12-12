import pygame
from pygame.locals import *
from config import *
from nivel import Nivel
from floor import Floor
from block import Blook
from goombas import Goombas
from sprites import *
from coin import Coin

class NivelUno(Nivel):
    def __init__(self, screen, player) -> None:
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        animations_goombas = get_animation_goombas()
        sound = pygame.mixer.Sound("./src/assets/sounds/level_one.mp3")
        sound.set_volume(0.3)

        background = pygame.image.load("./src/assets/images/backgrounds/level_1.jpg").convert_alpha()

        platform_list = [Floor([self.all_sprites, self.platforms], (0, 550, 200, 70)),
                        Floor([self.all_sprites, self.platforms], (200, 550, 200, 70)),
                        Floor([self.all_sprites, self.platforms], (400, 550, 200, 70)),
                        Floor([self.all_sprites, self.platforms], (600, 550, 200, 70)),
                        Blook([self.all_sprites, self.platforms], (150, 480, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (175, 480, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (200, 480, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (270, 460, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (350, 390, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (375, 390, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (400, 390, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (470, 330, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (495, 330, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (520, 330, 25, 25), True),
                        Blook([self.all_sprites, self.platforms], (545, 330, 25, 25), True)
                        ]
        
        enemies_list = [Goombas([self.all_sprites, self.enemies], animations_goombas, (520, 510)),
                        Goombas([self.all_sprites, self.enemies], animations_goombas, (400, 510)),
                        Goombas([self.all_sprites, self.enemies], animations_goombas, (760, 510))
                        ]
        
        coins_list = [Coin([self.all_sprites, self.coins], (300, 400)),
                        Coin([self.all_sprites, self.coins], (285, 450)),
                        Coin([self.all_sprites, self.coins], (325, 350)),
                        Coin([self.all_sprites, self.coins], (550, 535)),
                        Coin([self.all_sprites, self.coins], (482, 300))
                        ]

        super().__init__(screen, player, platform_list, enemies_list, background, coins_list, sound)