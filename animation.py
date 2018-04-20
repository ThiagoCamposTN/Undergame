from animator import Animator

class Animation(Animator):
    def start(self):
        pass

    def update(self):
        direction = self.values['direction']

        # TODO: Hard-coded numbers into enums

        if direction.y == -1:
            self.frame = 3

        if direction.x == -1:
            self.frame = 9

        if direction.y == 1:
            self.frame = 0

        if direction.x == 1:
            self.frame = 6
