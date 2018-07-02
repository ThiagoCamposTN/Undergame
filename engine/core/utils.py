import json
import os

def get_file_data(file_path):
    return json.load(open(file_path))