import pygame
from pygame.rect import Rect

class Transform:
    def __init__(self, game_object):
        self.game_object = game_object
        self._last_position = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(0, 0)
        self.velocity = 1
        self.scale = pygame.math.Vector2(1, 1)

    # After every movement, if the game object has a collider, the new position is sent
    # to the collider handler in order to revert the position if there's a collision.
    def set_position(self, new_position):
        if new_position != self.position:
            if hasattr(self.game_object, '_get_collider'):
                main_collider_handler = self.game_object._get_collider()._collider_handler

                collision_one = self.game_object.get_collision()
                rect = collision_one.get_rect()
                rect_one = Rect(new_position.x, new_position.y, rect.w, rect.h)
                collision_two = main_collider_handler._this_collided_with(collision_one, rect_one=rect_one)

                if collision_two: # Collided with something
                    self.game_object.on_collision(collision_two.game_object)
                    collision_two.game_object.on_collision(self.game_object)
                    return

            self._last_position = self.position
            self.position = new_position

def surface_scale(surface, vector2):
    int_x = int(vector2.x)
    int_y = int(vector2.y)

    # if the float ends with .0, convert it to int, if not, do nothing
    x = int_x if int_x == vector2.x else vector2.x
    y = int_y if int_y == vector2.y else vector2.y

    return pygame.transform.scale(  surface, 
                                    [x, y])
