import pygame
from engine.core.internal.behaviour import GameObject
from engine.core.component.spritesheet import Spritesheet
from engine.user_class.animator import Animator
from engine.core.internal.transform import Vector2

class PlayerBase(GameObject):
    def _awake(self, game_display, display_scale):
        self.animator = None
        self.sprite = None
        super()._awake(game_display, display_scale)

    def _start(self):
        super()._start()
        self.rect = pygame.Rect(Vector2.to_tuple(self.transform.position), Vector2.to_tuple(self.sprite.sprite_size))
        
    def _late_update(self):
        self._game_update()
        super()._late_update()

    def load_sprite(self, path, sprite_size):
        self.sprite = Spritesheet(path, sprite_size, self.display_scale)
        self.animator = Animator(self.sprite.cells, path)

    def _game_update(self):
        if self.animator:
            self.animator.update()

            if self.sprite:
                self.game_display.blit(self.sprite.sheet, self._position_based_on_display_scale(), self.sprite.get_sprite(self.animator.frame))

    def _position_based_on_display_scale(self):
        actual_position = ( self.display_scale.x * self.transform.position.x, 
                            self.display_scale.y * self.transform.position.y )

        self.rect.topleft = actual_position

        return self.rect.topleft

    def change_scale(self, new_scale):
        self.display_scale = new_scale

        self.sprite._resize_sprites(new_scale)
