import pygame
from engine.core.internal.transform import Vector2
from pygame.surface import Surface
from pygame.rect import Rect

class Spritesheet:
    def __init__(self, image_path, sprites_data, display_scale):
        self.display_scale = Vector2.one()
        self.sheet = self._load_spritesheet(image_path)
        self.sprites = self._get_and_sprites_from_raw_data(sprites_data)
        
        self._resize_sprites(new_scale=display_scale)

    def _load_spritesheet(self, image_path):
        if image_path != '':
            return pygame.image.load(image_path)
        
        return Surface((1, 1))

    def _get_and_sprites_from_raw_data(self, data):
        sprites = {}

        for sprite in data:
            sprites[sprite['name']] = Rect( sprite['rect'][0], sprite['rect'][1], 
                                            sprite['rect'][2], sprite['rect'][3])

        return sprites

    def _rescale_existing_sprites(self, old_scale):
        for sprite_name in self.sprites:
            self.sprites[sprite_name] = Rect(   self.sprites[sprite_name].x * self.display_scale.x // old_scale.x,
                                                self.sprites[sprite_name].y * self.display_scale.y // old_scale.y,
                                                self.sprites[sprite_name].w * self.display_scale.x // old_scale.x,
                                                self.sprites[sprite_name].h * self.display_scale.y // old_scale.y)

    def _resize_sprites(self, new_scale):
        old_scale = self.display_scale
        self.display_scale = new_scale
        
        self.sheet = pygame.transform.scale(self.sheet, 
                                            self._get_sheet_size(old_scale).to_tuple())

        self._rescale_existing_sprites(old_scale=old_scale)

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
