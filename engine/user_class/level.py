import pygame
from engine.user_class.base.level_base import LevelBase
from engine.core.internal.transform import Vector2

class Level(LevelBase):
    def start(self):
        self.transform.position = Vector2.zero()
        self.load_sprite('resources/scenarios/ruins.png', Vector2(20, 20))
        
    def update(self):
        pass
