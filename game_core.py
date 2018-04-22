class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def zero():
        return Vector2(0, 0)

    def one():
        return Vector2(1, 1)

    def to_tuple(position):
        return (position.x, position.y)

    def __add__(self, b):
        return Vector2(self.x + b.x, self.y + b.y)

    def __sub__(self, b):
        return Vector2(self.x - b.x, self.y - b.y)

    def __mul__(self, b):
        return Vector2(self.x * b, self.y * b)

    def __truediv__(self, b):
        return Vector2(self.x / b, self.y / b)

    def __floordiv__(self, b):
        return Vector2(self.x // b, self.y // b)

    def __eq__(self, vetor_b):
        return self.x == vetor_b.x and self.y == vetor_b.y

    def __str__(self):
        return "Vector2({0}, {1})".format(self.x, self.y)

class Transform:
    def __init__(self):
        self.position = Vector2.zero()
        self.velocity = 1
        self.scale = Vector2.one()
