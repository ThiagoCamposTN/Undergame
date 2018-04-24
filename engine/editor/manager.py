import pygame
from engine.core.static.color import Color
from engine.core.internal.transform import Vector2
from engine.editor.canvas import Canvas

class EditorManager:
    def __init__(self, game_display, grid_size, spritesheet_path, data_path, room_id):
        self.game_display = game_display
        self.grid_size = grid_size
        self.spritesheet_path = spritesheet_path
        self.data_path = data_path
        self.room_id = room_id
        self.canvas = Canvas()

    def setup(self):
        pygame.display.set_caption('Map Editor')

        self.clock = pygame.time.Clock()
        self.finished = False
        self.fps = 60

        self.display_scale = Vector2(2, 2)

    def start(self):
        pygame.init()
        self.setup()

        self.canvas._awake(self.game_display, self.display_scale)

        self.canvas._start(self.grid_size, self.spritesheet_path, self.data_path, self.room_id)
        
        self.main_loop()

        pygame.quit()
        quit()

    def main_loop(self):
        # Main loop
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True

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
        self.game_display.fill(Color.light_pink)

        self.canvas._update()
