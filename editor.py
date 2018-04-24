import pygame
import configparser
from engine.editor.manager import EditorManager
from engine.core.internal.transform import Vector2

def display_config():
    config = configparser.ConfigParser()
    config.read('editor.cfg')

    resolution = (int(config['General']['Width']), int(config['General']['Height']))
    grid_size = Vector2(int(config['Editor']['GridSizeX']), int(config['Editor']['GridSizeY']))
    spritesheet_path, data_path = str(config['Editor']['Spritesheet']), str(config['Editor']['Data'])
    room_id = str(config['Editor']['RoomId'])

    return pygame.display.set_mode(resolution), grid_size, spritesheet_path, data_path, room_id


def main():
    display, grid_size, spritesheet_path, data_path, room_id = display_config()

    manager = EditorManager(display, grid_size, spritesheet_path, data_path, room_id)
    manager.start()

if __name__ == "__main__":
    # execute only if run as a script
    main()
