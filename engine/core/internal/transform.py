import pygame

class Transform:
    def __init__(self):
        self.position = pygame.math.Vector2(0, 0)
        self.velocity = 1
        self.scale = pygame.math.Vector2(1, 1)

def surface_scale(surface, vector2):
    int_x = int(vector2.x)
    int_y = int(vector2.y)

    # if the float ends with .0, convert it to int, if not, do nothing
    x = int_x if int_x == vector2.x else vector2.x
    y = int_y if int_y == vector2.y else vector2.y

    return pygame.transform.scale(  surface, 
                                    [x, y])