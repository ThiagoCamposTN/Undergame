import pygame
from game_behaviour import GameObject
from spritesheet import Spritesheet
import utils
from game_core import Vector2

class Room:
    def __init__(self, data):
        self.tiles = {}

        for tile in data:
            positions = []

            for position in data[tile]:
                positions.append(Vector2(position[0], position[1]))

            self.tiles[tile] = positions

class LevelBase(GameObject):
    def _awake(self, game_display, display_scale):
        self.sprite = None
        self.rooms = []
        super()._awake(game_display, display_scale)

    def _start(self):
        super()._start()
        self.rect = pygame.Rect(Vector2.to_tuple(self.transform.position), Vector2.to_tuple(self.sprite.sprite_size))
        
    def _late_update(self):
        self._game_update()
        super()._late_update()

    def load_sprite(self, path, sprite_size):
        self.sprite = Spritesheet(path, sprite_size, self.display_scale)
        self.add_room(utils.get_file_data(path)["room_1"])

    def add_room(self, room_data):
        self.rooms.append(Room(room_data))

    def _game_update(self):
        if self.sprite:
            room_1 = self.rooms[0]

            for tile in room_1.tiles:
                for position in room_1.tiles[tile]:
                    self.game_display.blit(self.sprite.sheet, self._tile_position_based_on_display_scale(position), self.sprite.get_sprite(int(tile)))

    def _tile_position_based_on_display_scale(self, position):
        actual_position = ( position.x * self.sprite.sprite_size.x, 
                            position.y * self.sprite.sprite_size.y )

        self.rect.topleft = actual_position

        return self.rect.topleft

    def change_scale(self, new_scale):
        self.display_scale = new_scale

        self.sprite._resize_sprites(new_scale)
