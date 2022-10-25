#!/usr/bin/python3
"""save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON
    """

    with open(filename, mode="w", encoding="UTF-8") as saveFile:
        json.dump(my_obj, saveFile)
