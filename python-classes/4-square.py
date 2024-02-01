#!/usr/bin/python3
"""
This class represents an empty square.

Attributes:
    _size (int): The size of each side of the square.
"""


class Square:
    """
    This class represents a emty square.
    """

    def __init__(self, size=0):
        self._Square__size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Initializes a new Square object with the given size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        return self._Square__size**2
