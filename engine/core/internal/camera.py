from engine.core.internal.behaviour import GameObject
from pygame.math import Vector2
from pygame.rect import Rect

class Camera(GameObject):
    def __init__(self, game_manager, position, zoom):
        super().__init__()
        self.game_manager = game_manager
        self.transform.set_position(position)
        self.display_scale = zoom

    def zoom(self, factor):
        self.display_scale = Vector2(1, 1) * factor
        self.game_manager.update_objects_scale()

    def get_screen_size(self):
        return Vector2(self.game_manager.game_display.get_size())

     # screen divided by the current scale
    def get_scaled_screen_size(self):
        screen_size = self.get_screen_size()

        return Vector2( screen_size.x // self.display_scale.x,
                        screen_size.y // self.display_scale.y )

    def get_position_based_on_camera(self, position):
        half_screen_scaled = self.get_scaled_screen_size() // 2

        return position + half_screen_scaled - self.transform.position

    def get_rect(self):
        screen_scaled = self.get_scaled_screen_size()
        half_screen_scaled = screen_scaled // 2

        return Rect(    self.transform.position.x - half_screen_scaled.x,
                        self.transform.position.y - half_screen_scaled.y, 
                        screen_scaled.x,
                        screen_scaled.y)
