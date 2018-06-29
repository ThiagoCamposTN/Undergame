class Vector2:
    def __init__(self, first=None, second=None):
        self.x, self.y = self.convert_if_first_parameter_is_tuple(first, second)

    def convert_if_first_parameter_is_tuple(self, first, second):
        # if the first parameter is tuple, ignore the second parameter

        if isinstance(first, tuple):
            return first[0], first[1]
        else:
            return first, second

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

    def __mul__(self, number):
        return Vector2(self.x * number, self.y * number) 

    def __truediv__(self, number):
        return Vector2(self.x / number, self.y / number)

    def __floordiv__(self, number):
        return Vector2(self.x // number, self.y // number)

    def __eq__(self, vetor_b):
        return self.x == vetor_b.x and self.y == vetor_b.y

    def __str__(self):
        return "Vector2({0}, {1})".format(self.x, self.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

class Transform:
    def __init__(self):
        self.position = Vector2.zero()
        self.velocity = 1
        self.scale = Vector2.one()
