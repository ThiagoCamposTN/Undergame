import pygame
from engine.core.internal.behaviour import GameObject
from engine.core.component.spritesheet import Spritesheet
from engine.core import utils
from engine.core.internal.transform import Vector2
from engine.core.component.room import Room
from pygame.rect import Rect
import os

class LevelBase(GameObject):
    def _awake(self, game_display, main_camera):
        self.spritesheet = None
        #self.rooms = []
        self.debug_sheet = None
        super()._awake(game_display, main_camera)

    def _start(self):
        super()._start()
        
    def _late_update(self):
        self._game_update()
        super()._late_update()

    def load_spritesheet(self, category):
        sheet_data_path = os.path.join('resources', category, self.room.spritesheet_name + '.json')
        sheet_data = utils.get_file_data(sheet_data_path)

        sheet_image_path = os.path.join('resources', category, sheet_data['file'])
        
        self.spritesheet = Spritesheet(sheet_image_path, sheet_data["sprites"], self.main_camera.display_scale)
    
    def load_debug_sheet(self, category):
        sheet_data_path = os.path.join('resources', category, 'debug.json')
        sheet_data = utils.get_file_data(sheet_data_path)

        sheet_image_path = os.path.join('resources', category, sheet_data['file'])
        
        self.debug_sheet = Spritesheet(sheet_image_path, sheet_data["sprites"], self.main_camera.display_scale)

    def load_room(self, room_name):
        room_path = os.path.join('resources/rooms/', room_name + '.json')
        room_data = utils.get_file_data(room_path)

        self.room = Room(room_data, room_name)

        self.load_spritesheet('spritesheets')

    def _game_update(self):
        if self.spritesheet:
            for position_string in self.room.positions:
                position = self.room.get_position(position_string)
                sprite_name = self.room.sprite_name_in_position(position_string)
                
                sprite = self.spritesheet.get_sprite_rect(sprite_name)
                display_scale = self.main_camera.display_scale
                tile_rect = Rect(   position.x, position.y, 
                                    sprite.w // display_scale.x, sprite.h // display_scale.y)

                if self.on_screen(tile_rect):
                    tile_position = self._tile_position_based_on_display_scale(tile_rect)
                    self.game_display.blit(self.spritesheet.sheet, tile_position.to_tuple(), sprite)

        self.update_collision_sprites()

    def update_collision_sprites(self):
        for collision in self.room.collider.collisions:
            if collision.type == 'rectangle':
                for rect in collision.rects:
                    display_scale = self.main_camera.display_scale
                    sprite = self.debug_sheet.get_sprite_rect('collisionBox')
                    
                    tile_rect = Rect(   rect.x, rect.y, 
                                        sprite.w // display_scale.x, sprite.h // display_scale.y)

                    if self.on_screen(tile_rect):
                        tile_position = self._tile_position_based_on_display_scale(tile_rect)
                        self.game_display.blit(self.debug_sheet.sheet, tile_position.to_tuple(), sprite)

                    #TODO: NEXT OBJECTIVE: strech the collision sprites if desired

    #TODO: This function is very similar to player_base's _position_based_on_display_scale
    def _tile_position_based_on_display_scale(self, rect):
        position = Vector2(rect.x, rect.y)
        camera_based_position = self.main_camera.get_position_based_on_camera(position)

        actual_position = ( self.main_camera.display_scale.x * camera_based_position.x, 
                            self.main_camera.display_scale.y * camera_based_position.y)

        return Vector2(actual_position)

    def _update_scale(self):
        self.spritesheet._resize_sprites(self.main_camera.display_scale)
