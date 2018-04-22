import pygame
from game_core import Vector2

class Spritesheet:
    def __init__(self, image, size, display_scale):
        self.original_sheet = pygame.image.load(image)
        self.display_scale = display_scale

        self.sprite_size = self._get_sprite_size(size)
        self.sheet_size = self._get_sheet_size()

        self.sheet = pygame.transform.scale(self.original_sheet, self.sheet_size.to_tuple())

        self._get_sprites()

    def _get_sprite_size(self, size):
        return Vector2(size.x * self.display_scale.x, size.y * self.display_scale.y)

    def _get_sheet_size(self):
        width, height = self.original_sheet.get_rect().size
        return Vector2(width * self.display_scale.x, height * self.display_scale.y)

    def _get_sprites(self):
        '''
        Calculates all the sprites positions based on the given size,
        considering all sprites having an offset by 1 horizontally and vertically
        '''
        self.cells = []

        sprite_x = self.sprite_size.x
        sprite_y = self.sprite_size.y

        rows = self._get_rows()
        colls = self._get_colls()

        # offset is the pixels of the borders of the sheet and between sprites
        offset = self.display_scale

        for i in range(rows * colls):
            self.cells.append(((i % colls)*(sprite_x + offset.x) + offset.x, int(i / colls)*(sprite_y + offset.y) + offset.y, sprite_x, sprite_y))

    def get_sprite(self, number):
        return self.cells[number]

    def _get_rows(self):
        return int(self.sheet_size.y / self.sprite_size.y)

    def _get_colls(self):
        return int(self.sheet_size.x / self.sprite_size.x)

    