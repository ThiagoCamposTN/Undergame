import pygame
from engine.core.component import animation

class AnimatorBase:
    def __init__(self, sprite, path):
        self.sprite = sprite
        self.animations = animation.get_animations(path)
        
        self.playing_animation = None
        self.frame_counter = 0

        self.values = {}
        self.frame = 0

        self.start()

    def set_value(self, name, value):
        self.values[name] = value

    def start(self):
        pass

    def update(self):
        pass

    def get_current_time(self):
        return pygame.time.get_ticks()

    def get_animation(self, animation_name):
        return self.animations[animation_name]
