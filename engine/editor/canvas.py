import pygame
from engine.core.internal.behaviour import GameObject
from engine.core.component.spritesheet import Spritesheet
from pygame.math import Vector2
from engine.core import utils
from engine.editor.selector import Selector
from engine.core.component.room import Room
import os

class Canvas(GameObject):
    def _awake(self, game_display, display_scale, main_camera):
        self.spritesheet = None
        self.room = None
        self.selector = Selector()
        super()._awake(game_display, main_camera)

        self.selector._awake(game_display, display_scale)
        self.last_change = None
        self.selector_grid_position = Vector2(0, 0)
        self.display_scale = display_scale

    def _start(self, grid_size, spritesheet_path, data_path, room_name):
        self.grid_size = grid_size
        self.spritesheet_path = spritesheet_path
        self.data_path = data_path
        self.room_name = room_name
        super()._start()
        
    def _late_update(self):
        self._screen_update()
        super()._late_update()

    def _screen_update(self):
        if self.spritesheet:
            for str_position in self.room.positions:
                position = self.room.get_position(str_position)
                tile_position = self._tile_position_based_on_display_scale(position)
                sprite_in_position = self.room.positions[str_position]

                # 'cut' the sprite out from the sprite sheet
                sprite = self.spritesheet.sheet.subsurface(self.spritesheet.get_sprite_rect(sprite_in_position))

                self.game_display.blit(sprite, tile_position)
        
        selector_position = self._selector_position_based_on_display_scale(self.selector.transform.position)
        self.selector_grid_position = Vector2(selector_position[0], selector_position[1])
        selector_index = self.selector.get_current_sprite()
        self.game_display.blit(self.spritesheet.sheet, selector_position, self.spritesheet.get_sprite_rect_by_index(selector_index))

    def _tile_position_based_on_display_scale(self, position):
        actual_position = ( self.display_scale.x * position.x, 
                            self.display_scale.y * position.y )

        return actual_position

    def _selector_position_based_on_display_scale(self, position):
        expanded_grid_size = (self.grid_size.x * self.display_scale.x, self.grid_size.y * self.display_scale.y)
        
        selector_position = (int(position.x / expanded_grid_size[0]), int(position.y / expanded_grid_size[1]))
        selector_position = (selector_position[0] * expanded_grid_size[0], selector_position[1] * expanded_grid_size[1])

        return selector_position

    def _update_scale(self):
        self.spritesheet._resize_sprites(self.main_camera.display_scale)

    def load_room(self, room_name):
        room_path = os.path.join("resources", "rooms", f"{room_name}.json")
        room_data = utils.get_file_data(room_path)

        self.room = Room(room_data, room_name)

    def start(self):
        sheet_data = utils.get_file_data(self.data_path)

        self.spritesheet = Spritesheet(self.spritesheet_path, sheet_data["sprites"], self.main_camera.display_scale)
        self.load_room(self.room_name)
        self.selector.set_sprite_quantity(len(self.spritesheet.sprites))

    def update(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        mouse_position = pygame.mouse.get_pos()
        self.selector.transform.set_position(Vector2(mouse_position[0], mouse_position[1]))

        self.check_mouse_click(mouse)
        self.check_sprite_change(keys)

    def check_mouse_click(self, mouse):
        if mouse[0]:
            new_tile_position = (self.selector_grid_position.x // self.display_scale.x, self.selector_grid_position.y // self.display_scale.y)
            sprite_index = self.selector.get_current_sprite()
            self.room.positions[str(new_tile_position)[1:-1]] = self.spritesheet.get_sprite_name_by_index(sprite_index)

    def check_sprite_change(self, keys):
        changed_delta = None

        if keys[pygame.K_x]:
            changed_delta = 0
        elif keys[pygame.K_z]:
            changed_delta = 1
        elif keys[pygame.K_s]:
            changed_delta = 2

        if self.last_change != changed_delta:
            if changed_delta == 0:
                self.selector.next_sprite()
            elif changed_delta == 1:
                self.selector.back_sprite()
            elif changed_delta == 2:
                self.room.save_room(self.room_name, self.data_path)

        self.last_change = changed_delta
