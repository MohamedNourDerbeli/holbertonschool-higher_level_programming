#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method: def
        integer_validator(self, name, value): that validates value

        Args:
            name (str): The name .
            value (int): The parameter.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""
This script defines a Rectangle class with properties for width and height,
which are enforced to be positive integers.
"""


class Rectangle(BaseGeometry):

    """
    Constructor for the Rectangle class, initializing a rectangle with the
    given width and height values. Defaults to zero if no values are provided.
    """

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
