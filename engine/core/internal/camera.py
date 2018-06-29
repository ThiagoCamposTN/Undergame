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

    def get_screen_size(self):
        return Vector2(self.game_manager.game_display.get_size())

    def get_position_based_on_camera(self, position):
        screen_size = self.get_screen_size()

        # half the screen, divided by the current scale
        half_screen_scaled = Vector2( screen_size.x // (self.display_scale.x * 2),
                                screen_size.y // (self.display_scale.y * 2))

        return position + half_screen_scaled - self.transform.position
