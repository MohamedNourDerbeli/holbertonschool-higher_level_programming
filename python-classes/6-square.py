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

    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        self._position = position

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

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or v < 0 for v in value):
            TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return self._Square__size**2

    def my_print(self):
        if self._Square__size == 0:
            print()
            return
        for _ in range(self._position[1]):
            print(end="")
        for _ in range(self._Square__size):
            print(" " * self._position[0] + "#" * self._Square__size)
