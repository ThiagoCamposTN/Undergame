import pygame
from engine.core.internal.behaviour import GameObject
from engine.core.component.spritesheet import Spritesheet
from pygame.math import Vector2

class Selector(GameObject):
    def _awake(self, game_display, display_scale):
        super()._awake(game_display, display_scale)
        self.current_sprite = 0
        self.sprite_quantity = 0
        self.transform.set_position(Vector2(0, 0))

    def get_current_sprite(self):
        return self.current_sprite

    def set_sprite_quantity(self, quantity):
        self.sprite_quantity = quantity

    def next_sprite(self):
        if self.current_sprite + 1 < self.sprite_quantity:
            self.current_sprite += 1
        else:
            self.current_sprite = 0

    def back_sprite(self):
        if self.current_sprite - 1 >= 0:
            self.current_sprite -= 1
        else:
            self.current_sprite = self.sprite_quantity - 1
