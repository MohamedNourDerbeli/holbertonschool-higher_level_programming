#!/usr/bin/python3
"""
This is a simple script to demonstrate
how to use the pyrebase library.
"""
import json


class Base:
    """A base class for our Firebase application."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string from a list of dictionaries."""
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as fp:
                json.dump([], fp)
        else:
            data = list(i.to_dictionary() for i in list_objs)
            with open(f"{cls.__name__}.json", "w") as fp:
                fp.write(cls.to_json_string(data))
