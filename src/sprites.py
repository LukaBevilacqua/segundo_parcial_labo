import pygame
from config import *



def get_animation_player():
    animation_dict = {
        'right': [pygame.transform.scale(pygame.image.load("./src/assets/images/player/right/walk_right1.png").convert_alpha(), SIZE_PLAYER), 
            pygame.transform.scale(pygame.image.load("./src/assets/images/player/right/walk_right2.png").convert_alpha(), SIZE_PLAYER),
            pygame.transform.scale(pygame.image.load("./src/assets/images/player/right/walk_right3.png").convert_alpha(), SIZE_PLAYER),
            pygame.transform.scale(pygame.image.load("./src/assets/images/player/right/walk_right4.png").convert_alpha(), SIZE_PLAYER)
            ],
        'left':[pygame.transform.scale(pygame.image.load("./src/assets/images/player/left/walk_left1.png").convert_alpha(), SIZE_PLAYER),
            pygame.transform.scale(pygame.image.load("./src/assets/images/player/left/walk_left2.png").convert_alpha(), SIZE_PLAYER),
            pygame.transform.scale(pygame.image.load("./src/assets/images/player/left/walk_left3.png").convert_alpha(), SIZE_PLAYER),
            pygame.transform.scale(pygame.image.load("./src/assets/images/player/left/walk_left4.png").convert_alpha(), SIZE_PLAYER)
            ],
        'jump':[pygame.transform.scale(pygame.image.load("./src/assets/images/player/jump/jump_left.png").convert_alpha(), SIZE_PLAYER),
            pygame.transform.scale(pygame.image.load("./src/assets/images/player/jump/jump_right.png").convert_alpha(), SIZE_PLAYER)
            ]
        }
    return animation_dict


def get_animation_goombas():
    animation_dict = {
        'right': [pygame.transform.scale(pygame.image.load("./src/assets/images/enemies/goombas/0.png").convert_alpha(), SIZE_GOOMBAS), 
            pygame.transform.scale(pygame.image.load("./src/assets/images/enemies/goombas/1.png").convert_alpha(), SIZE_GOOMBAS),
            pygame.transform.scale(pygame.image.load("./src/assets/images/enemies/goombas/0.png").convert_alpha(), SIZE_GOOMBAS)
            ],
        'left':[pygame.transform.scale(pygame.image.load("./src/assets/images/enemies/goombas/1.png").convert_alpha(),SIZE_GOOMBAS), 
            pygame.transform.scale(pygame.image.load("./src/assets/images/enemies/goombas/0.png").convert_alpha(), SIZE_GOOMBAS),
            pygame.transform.scale(pygame.image.load("./src/assets/images/enemies/goombas/1.png").convert_alpha(), SIZE_GOOMBAS)
            ],
        'die':[pygame.transform.scale(pygame.image.load("./src/assets/images/enemies/goombas/2.png").convert_alpha(), SIZE_GOOMBAS)
            ]
        }
    return animation_dict

def get_animation_coins():
    animation_dict = {
        'right': [pygame.transform.scale(pygame.image.load("./src/assets/images/coins/0.png").convert_alpha(),SIZE_COIN), 
            pygame.transform.scale(pygame.image.load("./src/assets/images/coins/1.png").convert_alpha(),SIZE_COIN),
            pygame.transform.scale(pygame.image.load("./src/assets/images/coins/2.png").convert_alpha(),SIZE_COIN), 
            pygame.transform.scale(pygame.image.load("./src/assets/images/coins/3.png").convert_alpha(),SIZE_COIN),
            pygame.transform.scale(pygame.image.load("./src/assets/images/coins/4.png").convert_alpha(),SIZE_COIN), 
            pygame.transform.scale(pygame.image.load("./src/assets/images/coins/5.png").convert_alpha(),SIZE_COIN),
            pygame.transform.scale(pygame.image.load("./src/assets/images/coins/6.png").convert_alpha(),SIZE_COIN), 
            pygame.transform.scale(pygame.image.load("./src/assets/images/coins/7.png").convert_alpha(),SIZE_COIN)
            ]
        }
    return animation_dict




