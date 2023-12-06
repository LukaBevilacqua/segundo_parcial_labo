import pygame
from pygame.locals import *
from config import *
from power_up import PowerUp

class FireFlower(PowerUp):
    def __init__(self, groups, x, y, belongs) -> None:
        super().__init__(groups, x, y, belongs)
