import pygame

class MockDisplay:
    def __init__(self, resolution, window_mode):
        self.resolution = resolution
        self.window_mode = window_mode

    def get_size(self):
        return self.resolution