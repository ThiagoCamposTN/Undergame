from engine.core import utils

class Animation():
    def __init__(self, name, frames, duration):
        self.name = name
        self.frames = frames
        self.durations = [time * 1000 for time in duration]

    def get_frame_duration(self, index):
        return self.durations[index]

    def get_frame(self, index):
        return self.frames[index]

def get_animations(path):
    animation_data = utils.get_file_data(path)["animations"]

    animations = {}

    for animation in animation_data:
        animations[animation['name']] = Animation(  animation['name'], 
                                                    animation['frames'], 
                                                    animation['duration'])

    return animations