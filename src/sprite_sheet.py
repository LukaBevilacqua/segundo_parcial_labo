import pygame
from pygame.locals import *
from config import *

class SpriteSheet:
    def __init__(self, sheet: pygame.surface, rows, cols, width, height, keys = None) -> None:
        self.sheet = sheet
        self.width = self.sheet.get_width()
        self.height = self.sheet.get_height()
        self.rows = rows
        self.cols = cols
        self.width_sprite = width
        self.height_sprite = height
        self.keys = keys

    def get_animations(self, scale = 1):

        self.width = scale * self.width
        self.height = scale * self.height
        self.width_sprite = scale * self.width_sprite
        self.height_sprite = scale * self.height_sprite

        self.sheet = pygame.transform.scale(self.sheet, (self.width, self.height))
        cont_cols = 0
        animation_list = []
        for row in range(self.rows):
            animation_row = []
            for _ in range(self.cols):
                animation_row.append(self.sheet.subsurface((cont_cols * self.width_sprite,
                                                             row * self.height_sprite, self.width_sprite, self.height_sprite)))
                cont_cols += 1
            cont_cols = 0
            animation_list.append(animation_row)
        return animation_list
    
    def get_animations_dict(self, scale = 1):
        
        self.width = scale * self.width
        self.height = scale * self.height
        self.width_sprite = scale * self.width_sprite
        self.height_sprite = scale * self.height_sprite

        self.sheet = pygame.transform.scale(self.sheet, (self.width, self.height))
        cont_cols = 0
        animation_dict = {}
        for row in range(self.rows):
            animation_row = []
            for _ in range(self.cols):
                animation_row.append(self.sheet.subsurface((cont_cols * self.width_sprite,
                                                             row * self.height_sprite, self.width_sprite, self.height_sprite)))
                cont_cols += 1
            animation_dict[self.keys[row]] = animation_row
            cont_cols = 0
        return animation_dict







# el metodo conert_alpha() le aplica una conversion de transparencia para que funcione mejor (mejora el rendimiento)
# sheet = pygame.image.load("./src/assets/images/boy_sheet.png").convert_alpha()

# rows = 5
# cols = 4
# cont_cols = 0

# animation_list = []
# for row in range(rows):
#     animation_row = []
#     for _ in range(cols):
#         animation_row.append(sheet.subsurface((row * HEIGHT_PLAYER, cont_cols * WIDTH_PLAYER, WIDTH_PLAYER, HEIGHT_PLAYER)))
#         cont_cols += 1
#     cont_cols = 0
#     animation_list.append(animation_row)




# animation_dict = {"idle": [],
#                   "right": [],
#                   "left": [],
#                   "front": [],
#                   "back": []}