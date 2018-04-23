import utils

class Animation():
    def __init__(self, name, info):
        self.name = name
        self.frames = info[0]
        self.durations = [i * 1000 for i in info[1]]

    def get_frame_duration(self, index):
        return self.durations[index]

    def get_frame(self, index):
        return self.frames[index]

def get_animations(path):
    data = utils.get_file_data(path)["animations"]

    animations = {}

    for animation_name in data:
        animations[animation_name] = Animation(animation_name, data[animation_name])

    return animations