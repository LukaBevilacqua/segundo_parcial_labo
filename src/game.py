import pygame
from pygame.locals import *
from config import *
from sprite_sheet import SpriteSheet
from menu import Menu
from plataforma import Platform
from playable_character import PlayableCharacter
from enemy import Enemy
from sprite import get_animation




class Game:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego con clases")
        # pygame.display.set_icon(pygame.image.load("./sra/assets/images/icono.png"))

        # agrego al juego un grupo de sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.menu = Menu(self.screen)
        self.start_button = pygame.Rect(CENTER_SCREEN[0] - BUTTON_WIDTH // 2, 350, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.quit_button = pygame.Rect(CENTER_SCREEN[0] - BUTTON_WIDTH // 2, 450, BUTTON_WIDTH, BUTTON_HEIGHT)   

        # sprite_sheet_player = SpriteSheet(
        #     pygame.image.load("./src/assets/images/boy_sheet.png").convert_alpha(),
        #     5, 4, WIDTH_PLAYER, HEIGHT_PLAYER, ["idle", "right", "left", "front", "back"])
        
        sprite_sheet_player = get_animation()
        
        sprite_sheet_enemy = SpriteSheet(
            pygame.image.load("./src/assets/images/enemies/esqueletos.png").convert_alpha(), 4, 9, 64, 64, ["back", "left", "front", "right"])
        
        # sprite_sheet_baby = SpriteSheet(
        #     pygame.image.load("./src/assets/images/knuckles.png").convert_alpha(), 4, 5, 64, 64, ["back", "left", "front", "right"])
        
        Platform([self.all_sprites, self.platforms],(300, 550, 200, 50))
        Platform([self.all_sprites, self.platforms],(600, 450, 150, 50))
        Platform([self.all_sprites, self.platforms],(100, 50, 150, 200))



        # creo un player y le paso el grupo donde va a pertenecer
        self.player = PlayableCharacter([self.all_sprites], 5)
        self.enemy = Enemy([self.all_sprites, self.enemies], sprite_sheet_enemy, True, False)



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
        self.screen.fill((200, 200, 200))

        self.all_sprites.draw(self.screen)

    def update(self):

        plataformas = pygame.sprite.spritecollide(self.player, self.platforms, False)
        for plataforma in plataformas:
            if self.player.rect.bottom >= plataforma.rect.top and self.player.speed_v > 0:
                self.player.rect.bottom = plataforma.rect.top
                self.player.speed_v = 0
        # for plataforma in self.platforms:
        #     if self.player.rect.right >= plataforma.rect.left:
        #         self.player.move_right = False
        #     if self.player.rect.right < plataforma.rect.left:
        #         self.player.move_right = True
        #     if self.player.rect.left <= plataforma.rect.right:
        #         self.player.move_left = False
        #     if self.player.rect.left > plataforma.rect.right:
        #         self.player.move_left = True

        # pygame.sprite.spritecollide(self.player, self.enemies, True)
        



        self.all_sprites.update()
        pygame.display.flip()

    def close(self):
        pygame.quit()