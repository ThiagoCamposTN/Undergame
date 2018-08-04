import pygame
from engine.core.internal.transform import Transform

class GameObject:
    def __init__(self):
        self.transform = Transform(self)

    def _awake(self, game_display, main_camera):
        self.game_display = game_display
        self.main_camera = main_camera

        self.awake()

    def _start(self):
        self.start()

    def _update(self):
        self.update()
        self._late_update()

    def _late_update(self):
        self.late_update()
        
    def awake(self):
        pass

    def start(self):
        pass

    def update(self):
        pass

    def late_update(self):
        pass

    def on_screen(self, object_rect):
        screen_rect = self.main_camera.get_rect()
        return screen_rect.colliderect(object_rect)
