class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def zero():
        return Vector2(0, 0)

    def to_tuple(position):
        return (position.x, position.y)

    def __add__(self, b):
        return Vector2(self.x + b.x, self.y + b.y)

    def __mul__(self, b):
        return Vector2(self.x * b, self.y * b)

class Transform:
    def __init__(self):
        self.position = Vector2.zero()
        self.velocity = 1
