import pygame
from engine.user_class.base.level_base import LevelBase
from pygame.math import Vector2

class Level(LevelBase):
    def start(self):
        self.transform.position = Vector2(0, 0)
        self.load_debug_sheet('spritesheets')
        self.load_room('room1')
        
    def update(self):
        pass
