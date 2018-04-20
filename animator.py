import pygame

class Animator:
    def __init__(self, sprite):
        self.sprite = sprite
        self.values = {}
        self.frame = 0

        self.start()

    def set_value(self, name, value):
        self.values[name] = value

    def start(self):
        pass

    def update(self):
        pass
