import pygame
from engine.core.internal.behaviour import GameObject
from engine.core.component.spritesheet import Spritesheet
from engine.user_class.animator import Animator
from pygame.math import Vector2
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

    def load_spritesheet(self, category='', name=''):
        if(category != name != ''):
            char_data_path = os.path.join('resources', category, name + '.json')
            char_data = utils.get_file_data(char_data_path)

            char_sheet_path = os.path.join('resources', category, char_data['file'])

            self.spritesheet = Spritesheet(char_sheet_path, char_data["sprites"], self.main_camera.display_scale)
            self.animator = Animator(self.spritesheet, char_data_path)

    def _game_update(self):
        if self.animator:
            self.animator.update()

            # current sprite frame name
            sprite_name = self.animator.frame
            # sprite position within the spritesheet
            sprite_rect = self.spritesheet.get_sprite_rect(sprite_name)
            # 'cut' the sprite out from the sprite sheet
            sprite = self.spritesheet.sheet.subsurface(sprite_rect)

            # the current camera scale
            display_scale = self.main_camera.display_scale
            # player's position and sprite scale on the screen
            player_rect = Rect( self.transform.position.x, self.transform.position.y,
                                sprite_rect.w // display_scale.x, sprite_rect.h // display_scale.y)

            if self.spritesheet and self.on_screen(player_rect):
                player_position = self._position_based_on_display_scale()
                self.game_display.blit(sprite, player_position)

    def _position_based_on_display_scale(self):
        camera_based_position = self.main_camera.get_position_based_on_camera(self.transform.position)

        actual_position = ( self.main_camera.display_scale.x * camera_based_position.x, 
                            self.main_camera.display_scale.y * camera_based_position.y)

        return Vector2(actual_position)

    def _update_scale(self):
        self.spritesheet._resize_sprites(self.main_camera.display_scale)
