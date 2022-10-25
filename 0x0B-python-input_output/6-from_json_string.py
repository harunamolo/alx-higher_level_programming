#!/usr/bin/python3
"""from_json_string
"""
import json


def from_json_string(my_str):
    """Returns a python object represented by a JSON string
    """

    return json.loads(my_str)
