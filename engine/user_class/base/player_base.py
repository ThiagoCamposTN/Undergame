import pygame
from engine.core.internal.behaviour import GameObject
from engine.core.component.spritesheet import Spritesheet
from engine.user_class.animator import Animator
from engine.core.internal.transform import Vector2

class PlayerBase(GameObject):
    def _awake(self, game_display, main_camera):
        self.animator = None
        super()._awake(game_display, main_camera)

    def _start(self):
        super()._start()
        
    def _late_update(self):
        self._game_update()
        super()._late_update()

    def load_sprite(self, path, sprite_size):
        self.sprite = Spritesheet(path, sprite_size, self.main_camera.display_scale)

        if(path != ''):
            self.animator = Animator(self.sprite.cells, path)

    def _game_update(self):
        if self.animator:
            self.animator.update()

            if self.sprite and self.on_screen():
                self.game_display.blit(self.sprite.sheet, self._position_based_on_display_scale().to_tuple(), self.sprite.get_sprite(self.animator.frame))

    def _position_based_on_display_scale(self):
        camera_based_position = self.main_camera.get_position_based_on_camera(self.transform.position)

        actual_position = ( self.main_camera.display_scale.x * camera_based_position.x, 
                            self.main_camera.display_scale.y * camera_based_position.y)

        return Vector2(actual_position)

    def _update_scale(self):
        self.sprite._resize_sprites(self.main_camera.display_scale)

    def on_screen(self):
        player_top_left = self.transform.position
        player_bottom_right = self.transform.position + self.sprite.original_sprite_size

        half_screen_size = self.main_camera.get_scaled_screen_size() // 2

        screen_top_left = self.main_camera.transform.position - half_screen_size
        screen_bottom_right = self.main_camera.transform.position + half_screen_size

        if( player_bottom_right.x > screen_top_left.x and
            player_top_left.x < screen_bottom_right.x and
            player_bottom_right.y > screen_top_left.y and
            player_top_left.y < screen_bottom_right.y ):
            return True

        return False
