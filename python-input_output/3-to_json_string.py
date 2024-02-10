#!/usr/bin/python3
import json

"""Function to convert a Python object to a JSON string"""


def to_json_string(my_obj):
    """serialize the object to a JSON formatted string"""
    return json.dumps(my_obj)
