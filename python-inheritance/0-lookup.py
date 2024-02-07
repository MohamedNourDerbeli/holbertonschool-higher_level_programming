#!/usr/bin/python3

"""
This module provides a function to look up
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of names in the given
    object's namespace, including attributes
    and methods.

    Args:
        obj (object): The object whose attributes
        and methods should be listed.

    Returns:
        list: A list of strings representing
        the names of the object's attributes
              and methods.
    """
    return dir(obj)
