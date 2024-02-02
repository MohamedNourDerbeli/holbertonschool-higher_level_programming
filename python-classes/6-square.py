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
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(v, int) and v > 0 for v in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
