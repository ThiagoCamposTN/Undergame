import pygame
from engine.core.static.color import Color
from engine.core import hierarchy
from engine.core.internal.transform import Vector2
from engine.core.internal.camera import Camera

class GameManager:
    def __init__(self, game_display):
        self.game_display = game_display
        self.hierarchy = hierarchy.gameObjects

    def setup(self):
        pygame.display.set_caption('Undergame')

        self.clock = pygame.time.Clock()
        self.game_finished = False
        self.fps = 60

        self.main_camera = Camera(self, Vector2(self.game_display.get_size()) // 2, Vector2(2, 2))

    def start(self):
        pygame.init()
        self.setup()

        for gameObj in self.hierarchy:
            gameObj._awake(self.game_display, self.main_camera)

        for gameObj in self.hierarchy:
            gameObj._start()
        
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
            gameObj._update()

    def update_objects_scale(self):
        for gameObj in self.hierarchy:
            gameObj._update_scale()
