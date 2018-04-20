import pygame
from internal.color import Color
import hierarchy

class GameManager:
    def __init__(self, game_display):
        self.game_display = game_display
        self.hierarchy = hierarchy.gameObjects

    def setup(self):
        pygame.display.set_caption('Undergame')

        self.clock = pygame.time.Clock()
        self.game_finished = False
        self.fps = 60

    def start(self):
        pygame.init()
        self.setup()

        for gameObj in self.hierarchy:
            gameObj.awake(self.game_display)

        for gameObj in self.hierarchy:
            gameObj.start()
        
        self.game_loop()

        pygame.quit()
        quit()

    def game_loop(self):
        # Game loop
        while not self.game_finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_finished = True

            self.pressed_keys()
            self.update()

            pygame.display.update()
            self.clock.tick(self.fps)

    def pressed_keys(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LALT] and keys[pygame.K_F4] or keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        if keys[pygame.K_F11]:
            pygame.display.toggle_fullscreen()

    def update(self):
        self.game_display.fill(Color.lavender)

        for gameObj in self.hierarchy:
            gameObj.update()
