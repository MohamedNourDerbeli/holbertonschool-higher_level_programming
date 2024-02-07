#!/usr/bin/python3
"""
This function checks if the given object
is an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    If they match, the function returns True;
    otherwise, it returns False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
