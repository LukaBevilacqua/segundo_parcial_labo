import pygame
from pygame.locals import *
from config import *
from sounds import Sounds

class Nivel:
    def __init__(self, screen, player, platform_list, enemies_list, background, coins_list, sound) -> None:
        self.screen = screen
        self.player = player
        self.platform_list = platform_list
        self.enemies_list = enemies_list
        self.coins_list = coins_list
        self.background = background
        self.song = sound
        

    def update(self):
        self.update_screen()
        self.control_hitboxes()



    def update_screen(self):
        self.screen.blit(self.background, (0, 0))
        
        for platform in self.platform_list:
            self.screen.blit(platform.image, platform.rect)
        
        for enemy in self.enemies_list:
            self.screen.blit(enemy.image, enemy.rect)
            enemy.update()
        
        for coin in self.coins_list:
            self.screen.blit(coin.image, coin.rect)
            coin.update()
    
    def control_hitboxes(self):
        plataformas = pygame.sprite.spritecollide(self.player, self.platforms, False)
        for plataforma in plataformas:
            if self.player.rect.bottom >= plataforma.rect.top and self.player.speed_v > 0:
                self.player.rect.bottom = plataforma.rect.top
                self.player.speed_v = 0
    
        for enemy in self.enemies_list:
            plataformas = pygame.sprite.spritecollide(enemy, self.platforms, False)
            for plataforma in plataformas:
                if enemy.rect.bottom >= plataforma.rect.top and enemy.speed_v > 0:
                    enemy.rect.bottom = plataforma.rect.top
                    enemy.speed_v = 0
            enemy.attack(self.player)
            enemy.die(self.player)
        
        if pygame.sprite.spritecollide(self.player, self.coins, True):
            self.player.score += 1
            coin_collect = Sounds()
            coin_collect.coin_sound.play()
            print(self.player.score)
    
    def music(self):
        self.song.play(-1)


