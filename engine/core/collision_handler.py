from engine.core.component.collider import Collider
from engine.core.component.room import Room

class CollisionHandler:
    colliders_list = []

    def __init__(self):
        pass

    def _append_if_has_collider(self, game_object):
        # TODO: Maybe don't do this
        if hasattr(game_object, 'collider') and type(game_object.collider) == Collider:
            self.colliders_list.append(game_object.get_collider())
        elif hasattr(game_object, 'room') and type(game_object.room) == Room:
            for collider in game_object.room.collider.collisions:
                self.colliders_list.append(collider)

    def _check_for_collisions(self):
        for k, collider_one in enumerate(self.colliders_list):
            colliders_except_first = self.colliders_list[k+1:]
            if colliders_except_first:
                for collider_two in colliders_except_first:
                    if collider_one.get_rect().colliderect(collider_two.get_rect()):
                        #print("collision between {0} and {1}".format(collider_one.rect, collider_two.rect))
                        object_one = collider_one.game_object
                        object_two = collider_two.game_object

                        object_one.on_collision(object_two)
                        object_two.on_collision(object_one)