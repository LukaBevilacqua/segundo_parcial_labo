import pygame

class Sounds:
    def __init__(self) -> None:
        self.coin_sound = pygame.mixer.Sound("./src/assets/sounds/coin.mp3")
        self.coin_sound.set_volume(0.3)
        self.jump_sound = pygame.mixer.Sound("./src/assets/sounds/jump.mp3")
        self.jump_sound.set_volume(0.3)
        # self.dead_sound = pygame.mixer.Sound("./src/assets/sad.mp3")
        # self.dead_sound.set_volume(0.3)
        # self.background_sound = pygame.mixer.Sound("./src/assets/background_sound.mp3")
        # self.background_sound.set_volume(0.3)

