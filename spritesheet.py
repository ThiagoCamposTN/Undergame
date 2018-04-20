import pygame
from game_behaviour import Vector2

class Spritesheet:
    def __init__(self, image, size):
        self.sheet = pygame.image.load(image)
        self.sprite_size = size
        self.sheet_size = Vector2(self.sheet.get_rect().size[0], self.sheet.get_rect().size[1])

        self.get_sprites()

    def get_sprites(self):
        '''
        Calculates all the sprites positions based on the given size,
        considering all sprites having an offset by 1 horizontally and vertically
        '''
        self.cells = []

        sprite_x = self.sprite_size.x
        sprite_y = self.sprite_size.y

        rows = self.get_rows()
        colls = self.get_colls()

        for i in range(rows * colls):
            self.cells.append(((i % colls)*(sprite_x + 1) + 1, int(i / colls)*(sprite_y + 1) + 1, sprite_x, sprite_y))

    def get_sprite(self, number):
        return self.cells[number]

    def get_rows(self):
        return int(self.sheet_size.y / self.sprite_size.y)

    def get_colls(self):
        return int(self.sheet_size.x / self.sprite_size.x)
