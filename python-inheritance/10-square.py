#!/usr/bin/python3
"""
Author: Nour Mohamed
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class representing a square. Inherits from Rectangle."""

    def __init__(self, size):
        self.integer_validator("width", size)
        super().__init__(size, size)
        self.__size = size
