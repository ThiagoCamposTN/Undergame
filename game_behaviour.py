import pygame
from game_core import Transform
from spritesheet import Spritesheet
from animator import Animator

class GameObject:
    def awake(self, game_display):
        self.game_display = game_display
        self.transform = Transform()

    def start(self):
        pass

    def update(self):
        pass

    def load_sprite(self, path, sprite_size):
        self.sprite = Spritesheet(path, sprite_size)
        self.animator = Animator(self.sprite.cells, path)