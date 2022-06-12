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
                self.positions[str(position)[1:-1]] = sprites['name']

        self.collider = MapCollider(self, spritesheet["collisions"])

    def get_position(self, position_string):
        # TODO: why are positions stored as string?
        splitted_position = position_string.split(",")

        return Vector2(int(float(splitted_position[0])), int(float(splitted_position[1])))

    def sprite_name_in_position(self, position_string):
        return self.positions[position_string]

    def save_room(self, room_name, data_path):
        print("saving")

    def on_collision(self, colliding_object):
        print("{0} is colliding".format(type(self)))
