#!/usr/bin/python3
"""function that returns an object """
import json


def from_json_string(my_str):
    """serialize the object from a JSON formatted string"""

    return json.loads(my_str)
