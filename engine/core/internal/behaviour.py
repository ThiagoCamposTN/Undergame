import pygame
from engine.core.internal.transform import Transform

class GameObject:
    def _awake(self, game_display, display_scale):
        self.game_display = game_display
        self.transform = Transform()
        self.display_scale = display_scale

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
