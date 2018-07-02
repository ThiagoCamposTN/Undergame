from engine.core.internal.transform import Vector2
from pygame.rect import Rect

class Collision:
    def __init__(self, col_type, rects):
        self.type = col_type
        self.rects = rects

class Collider:
    def __init__(self, data):
        self.collisions = []

        self._get_collisionsfrom_data(data)

    def _get_collisionsfrom_data(self, data):
        for collisions in data:
            rects = []

            for rect in collisions['rects']:
                rects.append(Rect(rect[0], rect[1], rect[2], rect[3]))

            self.collisions.append(Collision(collisions['type'], rects))

        print(self.collisions[0].__dict__)