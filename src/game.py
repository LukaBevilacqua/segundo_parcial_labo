import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from initial_menu import InitialMenu
from plataforma import Platform
from playable_character import PlayableCharacter
from goombas import Goombas
from sprites import *
from coin import Coin
from sounds import *
from fire_flower import FireFlower
from projectile import Projectile



class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My Mario")
        # pygame.display.set_icon(pygame.image.load("./sra/assets/images/icono.png"))
    
        # agrego al juego un grupo de sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
    
        self.menu = InitialMenu(self.screen)
        self.start_button = pygame.Rect(CENTER_SCREEN[0] - BUTTON_WIDTH // 2, 350, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.quit_button = pygame.Rect(CENTER_SCREEN[0] - BUTTON_WIDTH // 2, 450, BUTTON_WIDTH, BUTTON_HEIGHT)   
        
        
        
        Platform([self.platforms],(0, 530, 800, 1))
        Platform([self.platforms],(225, 475, 35, 10))
        Platform([self.platforms],(125, 478, 45, 1))
        Platform([self.platforms],(150, 465, 55, 1))
        self.caja = Platform([self.platforms, self.all_sprites],(288, 415, 25, 25), False, True)
        Platform([self.platforms],(450, 452, 75, 10))
        Platform([self.platforms],(505, 477, 52, 10))
        Platform([self.platforms],(535, 415, 20, 25))
        Platform([self.platforms],(580, 415, 20, 25))

        self.fire = Projectile(self.player.rect.right, self.player.rect.centery, self.player.animations['right'])

        
    
        animations_goombas = get_animation_goombas()
        animations_player = get_animation_player()
        self.coin = Coin([self.all_sprites, self.coins], (300, 510))
        self.fire_flower = FireFlower([self.all_sprites, self.power_ups], 288, 415, self.caja)
        self.enemy = Goombas([self.all_sprites, self.enemies], animations_goombas, True, False)
        self.player = PlayableCharacter([self.all_sprites], animations_player, 0, 520)




    def run(self):
        running = True
        while running:
            # self.menu.initial_menu(self.start_button, BLUE, BLACK, "New game", self.quit_button, "Quit", BLUE, BLACK)
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            
            
            self.draw()
            
            self.update()
        self.close()
        
    def draw(self):
        prueba = pygame.transform.scale(pygame.image.load("./src/assets/images/backgrounds/prueba.jpg"), SIZE_SCREEN)
        self.screen.blit(prueba, prueba.get_rect())
    
        self.all_sprites.draw(self.screen)
        pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox_top, 2)
        pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox_bottom, 2)
        pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox_left, 2)
        pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox_right, 2)
        
    def update(self):
        
        plataformas = pygame.sprite.spritecollide(self.player, self.platforms, False)
        for plataforma in plataformas:
            if self.player.rect.bottom >= plataforma.rect.top and self.player.speed_v > 0:
                self.player.rect.bottom = plataforma.rect.top
                self.player.speed_v = 0
        
        # if self.fire_flower.rect.colliderect(self.caja.rect):
        #     self.fire_flower.rect.bottom = self.caja.rect.top
    
        plataformas = pygame.sprite.spritecollide(self.enemy, self.platforms, False)
        for plataforma in plataformas:
            if self.enemy.rect.bottom >= plataforma.rect.top and self.enemy.speed_v > 0:
                self.enemy.rect.bottom = plataforma.rect.top
                self.enemy.speed_v = 0
        # for plataforma in self.platforms:
        #     if self.player.rect.right >= plataforma.rect.left:
        #         self.player.move_right = False
        #     if self.player.rect.right < plataforma.rect.left:
        #         self.player.move_right = True
        #     if self.player.rect.left <= plataforma.rect.right:
        #         self.player.move_left = False
        #     if self.player.rect.left > plataforma.rect.right:
        #         self.player.move_left = True


        self.caja.show_item(self.player, self.fire_flower)
        
        if pygame.sprite.spritecollide(self.player, self.coins, True):
            self.player.score += 1
            coin_collect = Sounds()
            coin_collect.coin_sound.play()
            print(self.player.score)

        self.player.touch_flower(self.fire_flower)
        self.player

        self.enemy.attack(self.player)
        
        self.all_sprites.update()
        pygame.display.flip()

    def close(self):
        pygame.quit()