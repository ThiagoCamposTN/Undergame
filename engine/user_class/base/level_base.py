import pygame
from engine.core.internal.behaviour import GameObject
from engine.core.component.spritesheet import Spritesheet
from engine.core import utils
from engine.core.internal.transform import Vector2
from engine.core.component.room import Room
from pygame.rect import Rect

class LevelBase(GameObject):
    def _awake(self, game_display, main_camera):
        self.spritesheet = None
        self.rooms = []
        super()._awake(game_display, main_camera)

    def _start(self):
        super()._start()
        
    def _late_update(self):
        self._game_update()
        super()._late_update()

    def load_spritesheet(self, path):
        sheet_data = utils.get_file_data(path)

        self.spritesheet = Spritesheet(path, sheet_data["sprites"], self.main_camera.display_scale)
        self.add_room(sheet_data["room_1"])

    def add_room(self, room_data):
        self.rooms.append(Room(room_data))

    def _game_update(self):
        if self.spritesheet:
            # TODO: Change to be not hardcoded
            room_1 = self.rooms[0]

            for position_string in room_1.positions:
                position = room_1.get_position(position_string)
                sprite_name = room_1.sprite_name_in_position(position_string)
                
                sprite = self.spritesheet.get_sprite_rect(sprite_name)
                display_scale = self.main_camera.display_scale
                tile_rect = Rect(   position[0], position[1], 
                                    sprite.w // display_scale.x, sprite.h // display_scale.y)

                if self.on_screen(tile_rect):
                    tile_position = self._tile_position_based_on_display_scale(tile_rect)
                    self.game_display.blit(self.spritesheet.sheet, tile_position.to_tuple(), sprite)

    #TODO: This function is very similar to player_base's _position_based_on_display_scale
    def _tile_position_based_on_display_scale(self, rect):
        position = Vector2(rect.x, rect.y)
        camera_based_position = self.main_camera.get_position_based_on_camera(position)

        actual_position = ( self.main_camera.display_scale.x * camera_based_position.x, 
                            self.main_camera.display_scale.y * camera_based_position.y)

        return Vector2(actual_position)

    def _update_scale(self):
        self.spritesheet._resize_sprites(self.main_camera.display_scale)
