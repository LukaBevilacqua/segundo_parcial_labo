import pygame
from config import *


def get_animation():
    animation_dict = {
        'right': [pygame.transform.scale(pygame.image.load("./src/assets/images/player/right/walk_right1.png").convert_alpha(),(WIDTH_PLAYER, HEIGHT_PLAYER)), 
        pygame.transform.scale(pygame.image.load("./src/assets/images/player/right/walk_right2.png").convert_alpha(), (WIDTH_PLAYER, HEIGHT_PLAYER)),
        pygame.transform.scale(pygame.image.load("./src/assets/images/player/right/walk_right3.png").convert_alpha(), (WIDTH_PLAYER, HEIGHT_PLAYER)),
        pygame.transform.scale(pygame.image.load("./src/assets/images/player/right/walk_right4.png").convert_alpha(), (WIDTH_PLAYER, HEIGHT_PLAYER))
        ],
        'left':[pygame.transform.scale(pygame.image.load("./src/assets/images/player/left/walk_left1.png").convert_alpha(), (WIDTH_PLAYER, HEIGHT_PLAYER)),
        pygame.transform.scale(pygame.image.load("./src/assets/images/player/left/walk_left2.png").convert_alpha(), (WIDTH_PLAYER, HEIGHT_PLAYER)),
        pygame.transform.scale(pygame.image.load("./src/assets/images/player/left/walk_left3.png").convert_alpha(), (WIDTH_PLAYER, HEIGHT_PLAYER)),
        pygame.transform.scale(pygame.image.load("./src/assets/images/player/left/walk_left4.png").convert_alpha(), (WIDTH_PLAYER, HEIGHT_PLAYER))
        ],
        'jump':[pygame.transform.scale(pygame.image.load("./src/assets/images/player/jump/jump_left.png").convert_alpha(), (WIDTH_PLAYER, HEIGHT_PLAYER)),
        pygame.transform.scale(pygame.image.load("./src/assets/images/player/jump/jump_right.png").convert_alpha(), (WIDTH_PLAYER, HEIGHT_PLAYER))
        ]
    }
    return animation_dict
