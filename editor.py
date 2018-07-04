import pygame
import configparser
from engine.editor.editor_manager import EditorManager
from pygame.math import Vector2

def display_config():
    config = configparser.ConfigParser()
    config.read('editor.cfg')

    resolution = (int(config['General']['Width']), int(config['General']['Height']))
    grid_size = Vector2(int(config['Editor']['GridSizeX']), int(config['Editor']['GridSizeY']))
    spritesheet_path, data_path = str(config['Editor']['Spritesheet']), str(config['Editor']['Data'])
    room_name = str(config['Editor']['RoomName'])

    return pygame.display.set_mode(resolution), grid_size, spritesheet_path, data_path, room_name


def main():
    display, grid_size, spritesheet_path, data_path, room_name = display_config()

    manager = EditorManager(display, grid_size, spritesheet_path, data_path, room_name)
    manager.start()

if __name__ == "__main__":
    # execute only if run as a script
    main()
