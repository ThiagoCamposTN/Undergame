from animator_base import AnimatorBase
from animation import Animation

class Animator(AnimatorBase):
    def start(self):
        self.new_animation = self.get_animation('walk_forward')
        self.timer = None

    def update(self):
        direction = self.values['direction']

        if direction.y == -1:
            self.new_animation = self.get_animation('walk_back')

        if direction.x == -1:
            self.new_animation = self.get_animation('walk_left')

        if direction.y == 1:
            self.new_animation = self.get_animation('walk_forward')

        if direction.x == 1:
            self.new_animation = self.get_animation('walk_right')

        if self.playing_animation != self.new_animation:
            self.reset_frame_counter()

        self.playing_animation = self.new_animation
        
        if self.timer == None:
            self.timer = self.get_current_time()

        if self.get_current_time() > self.timer + self.playing_animation.get_frame_duration(self.frame_counter):
            self.timer = None

            if self.frame_counter < len(self.playing_animation.durations) - 1:
                self.frame_counter += 1
            else:
                self.reset_frame_counter()

        self.frame = self.playing_animation.get_frame(self.frame_counter)

    def reset_frame_counter(self):
        self.frame_counter = 0