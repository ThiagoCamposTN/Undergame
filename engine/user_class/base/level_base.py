import pygame
from engine.core.internal.behaviour import GameObject
from engine.core.component.spritesheet import Spritesheet
from engine.core import utils
from engine.core.internal.transform import Vector2
from engine.core.component.room import Room

class LevelBase(GameObject):
    def _awake(self, game_display, main_camera):
        self.sprite = None
        self.rooms = []
        super()._awake(game_display, main_camera)

    def _start(self):
        super()._start()
        
    def _late_update(self):
        self._game_update()
        super()._late_update()

    def load_sprite(self, path, sprite_size):
        self.sprite = Spritesheet(path, sprite_size, self.main_camera.display_scale)
        self.add_room(utils.get_file_data(path)["room_1"])

    def add_room(self, room_data):
        self.rooms.append(Room(room_data))

    def _game_update(self):
        if self.sprite:
            room_1 = self.rooms[0]

            for str_position in room_1.positions:
                position = room_1.position_from_tuple_str(str_position)

                tile_position = self._tile_position_based_on_display_scale(Vector2(position[0], position[1])).to_tuple()
                sprite_in_position = room_1.positions[str_position]
                self.game_display.blit(self.sprite.sheet, tile_position, self.sprite.get_sprite(sprite_in_position))

    #TODO: This function is almost exactly to player_base's _position_based_on_display_scale
    def _tile_position_based_on_display_scale(self, position):
        camera_based_position = self.main_camera.get_position_based_on_camera(position)

        actual_position = ( self.main_camera.display_scale.x * camera_based_position.x, 
                            self.main_camera.display_scale.y * camera_based_position.y)

        return Vector2(actual_position)

    def _update_scale(self):
        self.sprite._resize_sprites(self.main_camera.display_scale)
