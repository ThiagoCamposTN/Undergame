from engine.core.component.collider import Collider
from engine.core.component.room import Room

class CollisionHandler:
    collisions_list = []

    def __init__(self):
        pass

    def _append_if_has_collider(self, game_object):
        # TODO: Maybe don't do this
        if hasattr(game_object, 'collider') and type(game_object.collider) == Collider:
            self.collisions_list.append(game_object.get_collider())
        elif hasattr(game_object, 'room') and type(game_object.room) == Room:
            for collider in game_object.room.collider.collisions:
                self.collisions_list.append(collider)

    def _check_for_collision(self):
        for k, collision in enumerate(self.collisions_list):
            self._this_collided_with(collision, k)

    def _this_collided_with(self, collision_one, index=-1):
        collisions_list = self.collisions_list[index + 1:]

        for collision_two in collisions_list:
            if collision_one.get_rect().colliderect(collision_two.get_rect()):
                object_one = collision_one.game_object
                object_two = collision_two.game_object

                object_one.on_collision(object_two)
                object_two.on_collision(object_one)
