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
from pause_menu import PauseMenu
from nivel_uno import NivelUno



class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My Mario")
        pygame.display.set_icon(pygame.image.load("./src/assets/images/icon_game/icon.png"))
    
        self.all_sprites = pygame.sprite.Group()

    
        self.initial_menu = InitialMenu(self.screen)
        self.start_button = pygame.Rect(int(CENTER_SCREEN[0] - BUTTON_WIDTH // 2), 350, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.options_button = pygame.Rect(int(CENTER_SCREEN[0] - BUTTON_WIDTH // 2), 430, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.quit_button = pygame.Rect(int(CENTER_SCREEN[0] - BUTTON_WIDTH // 2), 510, BUTTON_WIDTH, BUTTON_HEIGHT) 
        
        self.pause_menu = PauseMenu(self.screen)



        
        


        self.fire = []
        


        
    
        animations_player = get_animation_player()
        self.player = PlayableCharacter([self.all_sprites], animations_player, 0, 520, self.fire)



        self.nivel_actual = NivelUno(self.screen, self.player)

    def run(self):
        running = True
        run = True
        while run:
            self.initial_menu.initial_menu(self.start_button, "New game", BLUE, WHITE, self.options_button, "Options",
                                    BLUE, WHITE, self.quit_button, "Quit", BLUE, WHITE)
            while running:
                self.clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                        run = False
                
                self.nivel_actual.update()

                if not self.pause_menu.paused:
                    self.draw()
                    self.handle_pause()
                    self.update()
            self.close()
        
    def draw(self):
        
    
        self.all_sprites.draw(self.screen)
        # pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox_top, 2)
        # pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox_bottom, 2)
        # pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox_left, 2)
        # pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox_right, 2)
        
    def update(self):
        
    


        # self.caja.show_item(self.player, self.fire_flower)
        
        

        # self.player.touch_flower(self.fire_flower)
        # self.player

        
        self.all_sprites.update()
        pygame.display.flip()

    def close(self):
        pygame.quit()

    def handle_pause(self):
        self.pause_menu.pause(self.start_button, "Continue", BLUE, WHITE, self.quit_button, "Quit", BLUE, WHITE)