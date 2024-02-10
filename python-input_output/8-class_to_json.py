#!/usr/bin/python3
"""object to JSON string representation."""
import json


def class_to_json(obj):
    """Converts a class object to JSON string representation."""
    return json.dumps(obj.__dict__)
