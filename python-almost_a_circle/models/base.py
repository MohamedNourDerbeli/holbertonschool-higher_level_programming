#!/usr/bin/python3
"""
This is a simple script to demonstrate
how to use the pyrebase library.
"""
import json
from os.path import isfile
from turtle import *


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
        """Saves objects in a file (one object per line)."""
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as fp:
                json.dump([], fp)
        else:
            data = list(i.to_dictionary() for i in list_objs)
            with open(f"{cls.__name__}.json", "w") as fp:
                fp.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of objects from a JSON string."""
        if json_string is None:
            return []
        else:
            data = list(json.loads(json_string))
            return data

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of the class using a dictionary."""
        cls.update(dictionary)
        return cls(**dictionary)

    @classmethod
    def load_from_file(cls):
        """Loads objects from a file and returns them as a list."""
        if isfile(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", "r") as fp:
                data = cls.from_json_string(fp.read())
        lis = []
        for i in data:
            lis.append(cls.create(**i))
        return lis

    # @staticmethod
    # def draw(list_rectangles, list_squares):
    #     """Draws rectangles and squares on screen."""
    #     while True:
    #         forward(200)
    #         left(170)
    #         if abs(pos()) < 1:
    #             break
