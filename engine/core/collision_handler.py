from engine.core.component.collider import Collider
from engine.core.component.room import Room

class CollisionHandler:
    collisions_list = []

    def __init__(self):
        pass

    def _append_if_has_collider(self, game_object):
        # TODO: Maybe don't do this
        if hasattr(game_object, 'collider') and type(game_object.collider) == Collider:
            self.collisions_list.append(game_object.get_collision())
            game_object.collider._set_handler(self) 
        elif hasattr(game_object, 'room') and type(game_object.room) == Room:
            game_object.room.collider._set_handler(self) 
            for collision in game_object.room.collider.collisions:
                self.collisions_list.append(collision)

    def _check_for_collision(self):
        for k, collision_one in enumerate(self.collisions_list):
            collision_two = self._this_collided_with(collision_one, k)

            if collision_two:
                object_one = collision_one.game_object
                object_two = collision_two.game_object

                object_one.on_collision(object_two)
                object_two.on_collision(object_one)

    def _this_collided_with(self, collision_one, index=-1, rect_one=None):
        collisions_list = self.collisions_list[index + 1:]

        if not rect_one:
            rect_one = collision_one.get_rect()

        for collision_two in collisions_list:
            if (collision_one.game_object != collision_two.game_object and 
                rect_one.colliderect(collision_two.get_rect())):
                return collision_two

        return None
