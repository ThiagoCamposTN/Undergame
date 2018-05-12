from engine.core.internal.behaviour import GameObject
from engine.core.internal.transform import Vector2

class Camera(GameObject):
    def __init__(self, game_manager, position, zoom):
        super().__init__()
        self.game_manager = game_manager
        self.transform.position = position
        self.display_scale = zoom
        self.delta = Vector2.zero()

    def zoom(self, factor):
        self.display_scale = Vector2.one() * factor
        self.game_manager.update_objects_scale()

    def move(self, delta):
        self.delta = delta

    def set_position(self, position):
        self.move(position - self.transform.position)

    def get_position(self):
        return self.transform.position + self.delta