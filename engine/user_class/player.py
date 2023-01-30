import pygame
from engine.user_class.base.player_base import PlayerBase
from pygame.math import Vector2

class Player(PlayerBase):
    def start(self):
        self.load_spritesheet('characters', 'Kanji')
        
    def update(self):
        keys = pygame.key.get_pressed()

        direction = Vector2(0, 0)

        direction.y += -int(keys[pygame.K_w]) + int(keys[pygame.K_s])
        direction.x += -int(keys[pygame.K_a]) + int(keys[pygame.K_d])

        self.animator.set_value("direction", direction)

        self.transform.set_position(self.transform.position + direction * self.transform.velocity)

        # Camera follows player
        self.main_camera.transform.set_position(self.transform.position)
