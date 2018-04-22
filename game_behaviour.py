import pygame
from game_core import Transform
from spritesheet import Spritesheet
from animator import Animator
from game_core import Vector2

class GameObject:
    def _awake(self, game_display, display_scale):
        self.game_display = game_display
        self.transform = Transform()

        self.animator = None
        self.sprite = None
        self.display_scale = display_scale

        self.awake()

    def awake(self):
        pass

    def _start(self):
        self.start()
        
        self.rect = pygame.Rect(Vector2.to_tuple(self.transform.position), Vector2.to_tuple(self.sprite.sprite_size))

    def start(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass

    def _update(self):
        self.update()
        self._game_update()
        self.late_update()

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