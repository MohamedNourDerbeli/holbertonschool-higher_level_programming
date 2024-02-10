#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Function to create an object from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)
