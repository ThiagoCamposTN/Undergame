import pygame
from game_behaviour import GameBehaviour, Transform, Vector2
from spritesheet import Spritesheet

class Player(GameBehaviour):
    def start(self):
        self.transform.position = Vector2(100, 100)
        self.transform.velocity = 1

        self.sprite = Spritesheet('resources/frisk.png', Vector2(19, 29))

        self.current_sprite = 0
        
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.transform.position.y -= self.transform.velocity

        if keys[pygame.K_a]:
            self.transform.position.x -= self.transform.velocity

        if keys[pygame.K_s]:
            self.transform.position.y += self.transform.velocity
        
        if keys[pygame.K_d]:
            self.transform.position.x += self.transform.velocity

        # TODO: Remove this system and implement an animation system
        if keys[pygame.K_x]:
            self.current_sprite += 1

        if keys[pygame.K_z]:
            self.current_sprite -= 1

        if self.current_sprite < 0:
            self.current_sprite = 0
        elif self.current_sprite > len(self.sprite.cells) - 1:
            self.current_sprite = len(self.sprite.cells) - 1
        #

        current_sprite = self.sprite.current_sprite()

        self.game_update(current_sprite)

    def game_update(self, current_sprite):
        self.game_display.blit(current_sprite, Vector2.to_tuple(self.transform.position), self.sprite.cells[self.current_sprite])
