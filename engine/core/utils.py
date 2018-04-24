import json
import os

def get_file_data(file_path):
    json_path = os.path.join(os.path.splitext(file_path)[0] + '.json')
    return json.load(open(json_path))