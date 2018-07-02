import pygame
from engine.core.internal.behaviour import GameObject
from engine.core.component.spritesheet import Spritesheet
from engine.user_class.animator import Animator
from engine.core.internal.transform import Vector2
from pygame.rect import Rect
from engine.core import utils
import os

class PlayerBase(GameObject):
    def _awake(self, game_display, main_camera):
        self.animator = None
        super()._awake(game_display, main_camera)

    def _start(self):
        super()._start()
        
    def _late_update(self):
        self._game_update()
        super()._late_update()

    def load_spritesheet(self, name):
        if(name != ''):
            char_sheet_path = os.path.join('resources/characters/', name + '.png')
            char_data_path = os.path.join('resources/characters/', name + '.json')
            char_data = utils.get_file_data(char_data_path)

            self.spritesheet = Spritesheet(char_sheet_path, char_data["sprites"], self.main_camera.display_scale)
            self.animator = Animator(self.spritesheet, char_data_path)

    def _game_update(self):
        if self.animator:
            self.animator.update()

            sprite_name = self.animator.frame
            sprite = self.spritesheet.get_sprite_rect(sprite_name)
            display_scale = self.main_camera.display_scale

            player_rect = Rect( self.transform.position.x, self.transform.position.y,
                                sprite.w // display_scale.x, sprite.h // display_scale.y)

            if self.spritesheet and self.on_screen(player_rect):
                player_position = self._position_based_on_display_scale()
                self.game_display.blit(self.spritesheet.sheet, player_position.to_tuple(), sprite)

    def _position_based_on_display_scale(self):
        camera_based_position = self.main_camera.get_position_based_on_camera(self.transform.position)

        actual_position = ( self.main_camera.display_scale.x * camera_based_position.x, 
                            self.main_camera.display_scale.y * camera_based_position.y)

        return Vector2(actual_position)

    def _update_scale(self):
        self.spritesheet._resize_sprites(self.main_camera.display_scale)
