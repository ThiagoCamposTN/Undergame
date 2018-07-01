class Room:
    def __init__(self, data):
        self.positions = {}

        for tile in data:
            for position in data[tile]:
                self.positions[str(position)] = tile

    def get_position(self, position_string):
        splitted_position = position_string[1:-1].split(",")
        return (int(splitted_position[0]), int(splitted_position[1]))

    def sprite_name_in_position(self, position_string):
        return self.positions[position_string]

    def save_room(self, room_name, data_path):
        print("saving")
