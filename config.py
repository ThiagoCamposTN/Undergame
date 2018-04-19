import pygame
import configparser

def game_display():
    config = configparser.ConfigParser()
    config.read('game.cfg')

    resolution = (int(config['General']['Width']), int(config['General']['Height']))
    window_mode = int(config['General']['WindowMode'])

    if window_mode == 1:
        window_mode = pygame.FULLSCREEN
    else:
        window_mode = 0

    return pygame.display.set_mode(resolution, window_mode)
