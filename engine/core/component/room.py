class Room:
    def __init__(self, data):
        self.positions = {}

        for tile in data:
            for position in data[tile]:
                self.positions[str(position)] = int(tile)

    def position_from_tuple_str(self, string_position):
        splitted_position = string_position[1:-1].split(",")
        return (int(splitted_position[0]), int(splitted_position[1]))

    def save_room(self, room_name, data_path):
        print("saving")