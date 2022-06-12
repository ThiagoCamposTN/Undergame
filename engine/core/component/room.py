from pygame.math import Vector2
from pygame.rect import Rect
from engine.core.component.collider import MapCollider

class Room:
    def __init__(self, data, name):
        spritesheet = data["spritesheet"]

        self.name = name
        self.spritesheet_name = spritesheet["name"]
        self.positions = {}

        for sprites in spritesheet["sprites"]:
            for position in sprites['positions']:
                tuple_position = tuple(position)
                self.positions[tuple_position] = sprites['name']

        self.collider = MapCollider(self, spritesheet["collisions"])

    def sprite_name_in_position(self, position_string):
        return self.positions[position_string]

    def save_room(self, room_name, data_path):
        print("saving")

    def on_collision(self, colliding_object):
        print("{0} is colliding".format(type(self)))
