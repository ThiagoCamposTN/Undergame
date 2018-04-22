import pygame
from game_behaviour import GameObject
from game_core import Vector2

class Player(GameObject):
    def start(self):
        self.transform.position = Vector2(10, 10)
        #self.transform.velocity = 1

        self.load_sprite('resources/frisk.png', Vector2(19, 29))
        
    def update(self):
        keys = pygame.key.get_pressed()

        direction = Vector2.zero()

        direction.y += -int(keys[pygame.K_w]) + int(keys[pygame.K_s])
        direction.x += -int(keys[pygame.K_a]) + int(keys[pygame.K_d])

        self.animator.set_value("direction", direction)

        self.transform.position += direction * self.transform.velocity
