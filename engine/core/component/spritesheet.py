import pygame
from engine.core.internal.transform import Vector2
from pygame.surface import Surface
from pygame.rect import Rect

class Spritesheet:
    def __init__(self, image_path, sprites_data, display_scale):
        self.display_scale = Vector2.one()
        self.sheet = self._load_spritesheet(image_path)
        self.sprites = {}
        
        self._resize_sprites(new_scale=display_scale, sprites_data=sprites_data)

    def _load_spritesheet(self, image_path):
        if image_path != '':
            return pygame.image.load(image_path)
        
        return Surface((1, 1))

    def _get_all_sprites(self, old_scale=Vector2.one(), input_data=None):
        sprites = {}

        data = input_data or self.sprites

        for i in data:
            if input_data:
                sprite_data = Rect(data[i][0], data[i][1], data[i][2], data[i][3])
            else:
                sprite_data = data[i]
           
            sprites[i] = Rect(  sprite_data.x * self.display_scale.x // old_scale.x,
                                sprite_data.y * self.display_scale.y // old_scale.y, 
                                sprite_data.w * self.display_scale.x // old_scale.x,
                                sprite_data.h * self.display_scale.y // old_scale.y)

        return sprites

    def _resize_sprites(self, new_scale, sprites_data=None):
        old_scale = self.display_scale
        self.display_scale = new_scale
        
        self.sheet = pygame.transform.scale(self.sheet, 
                                            self._get_sheet_size(old_scale).to_tuple())

        self.sprites = self._get_all_sprites(old_scale=old_scale, input_data=sprites_data)

    def _get_sheet_size(self, old_scale=Vector2.one()):
        width, height = self.sheet.get_rect().size

        return Vector2( width * self.display_scale.x // old_scale.x,
                        height * self.display_scale.y // old_scale.y)

    def get_sprite_rect(self, name):
        return self.sprites[name]

    def get_sprite_name_by_index(self, index):
        return list(self.sprites.keys())[index]

    def get_sprite_rect_by_index(self, index):
        return self.get_sprite_rect(self.get_sprite_name_by_index(index))
