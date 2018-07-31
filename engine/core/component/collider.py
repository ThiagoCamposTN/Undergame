from pygame.math import Vector2
from pygame.rect import Rect
from engine.core.component.spritesheet import Spritesheet

class MapCollision:
    def __init__(self, game_object, col_type, name, rect):
        self.type = col_type
        self.name = name
        self.rect = rect
        self.game_object = game_object

    def get_rect(self):
        return self.rect

class MapCollider:
    def __init__(self, game_object, data):
        self.collisions = []

        self._get_collisions_from_data(game_object, data)

    def _get_collisions_from_data(self, game_object, data):
        for collisions in data:
            for raw_rect in collisions['rects']:
                rect = Rect(raw_rect[0], raw_rect[1], raw_rect[2], raw_rect[3])

                self.collisions.append(MapCollision(game_object, collisions['type'], 
                                                    collisions['name'], rect))

class Collision:
    def __init__(self, game_object, col_type, name, sprite_name, rect):
        self.type = col_type
        self.name = name
        self.sprite_name = sprite_name
        self.rect = rect
        self.game_object = game_object

    def get_rect(self):
        position = self.game_object.transform.position
        return Rect(position.x, position.y, self.rect.w, self.rect.h)
        
class Collider:
    def __init__(self, game_object, data):
        self.collisions = {}

        self._get_collisions_from_data(game_object, data)

    def _get_collisions_from_data(self, game_object, data):
        for collisions in data:
            for sprite_name in collisions['sprites']:
                rect = Rect(0, 0, collisions['rect'][0], collisions['rect'][1])

                self.collisions[sprite_name] = Collision(   game_object, collisions['type'], 
                                                            collisions['name'], sprite_name, rect)
