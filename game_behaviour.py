import pygame
from game_core import Transform
from spritesheet import Spritesheet
from animator import Animator
from game_core import Vector2

class GameObject:
    def awake(self, game_display):
        self.game_display = game_display
        self.transform = Transform()

        self.animator = None
        self.sprite = None

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
        self.sprite = Spritesheet(path, sprite_size)
        self.animator = Animator(self.sprite.cells, path)

    def _game_update(self):
        if self.animator:
            self.animator.update()

            if self.sprite:
                self.game_display.blit(self.sprite.sheet, Vector2.to_tuple(self.transform.position), self.sprite.get_sprite(self.animator.frame))