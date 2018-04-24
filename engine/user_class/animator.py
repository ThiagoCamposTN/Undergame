from engine.user_class.base.animator_base import AnimatorBase
from engine.core.component.animation import Animation

class Animator(AnimatorBase):
    def start(self):
        self.initial_animation = self.get_animation('walk_forward')
        self.timer = None

    def update(self):
        direction = self.values['direction']

        animation = None

        if direction.y == -1:
            animation = self.get_animation('walk_back')

        if direction.x == -1:
            animation = self.get_animation('walk_left')

        if direction.y == 1:
            animation = self.get_animation('walk_forward')

        if direction.x == 1:
            animation = self.get_animation('walk_right')

        if animation == None:
            if self.playing_animation == None:
                self.playing_animation = self.initial_animation

            self.frame = self.playing_animation.get_frame(0)
        else:
            if self.playing_animation != animation:
                self.reset_frame_counter()

            self.playing_animation = animation

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