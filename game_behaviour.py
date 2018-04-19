import pygame

class GameBehaviour:
    def awake(self, game_display):
        self.game_display = game_display
        self.transform = Transform()

    def start(self):
        pass

    def update(self):
        pass

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def zero():
        return Vector2(0, 0)

    def to_tuple(position):
        return (position.x, position.y)

class Transform:
    def __init__(self):
        self.position = Vector2.zero()