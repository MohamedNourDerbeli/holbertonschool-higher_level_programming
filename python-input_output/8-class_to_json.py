#!/usr/bin/python3
"""object to JSON string representation."""
to_json_string = __import__("3-to_json_string").to_json_string


def class_to_json(obj):
    """Converts a class object to JSON string representation."""

    return obj.__dict__
