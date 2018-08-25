import json

def get_file_data(file_path):
    json_data = None

    with open(file_path) as opened_file:
        json_data = json.load(opened_file)

    return json_data
