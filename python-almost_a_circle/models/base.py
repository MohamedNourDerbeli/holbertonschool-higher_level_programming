#!/usr/bin/python3
"""
This is a simple script to demonstrate
how to use the pyrebase library.
"""


class Base:
    """A base class for our Firebase application."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
