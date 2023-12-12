import pygame
from pygame.locals import *
from menu import Menu
from config import *

class OptionsMenu(Menu):
    def __init__(self, screen) -> None:
        super().__init__(screen)