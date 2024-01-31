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
        """
        Initializes a new Square object with the given size.
        """
        self._Square__size = size
        try:
            if self._Square__size is int:
                raise TypeError
            if self._Square__size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
            return
        except ValueError:
            print("size must be >= 0")
            return
        return
