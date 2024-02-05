#!/usr/bin/python3

"""
This script defines a Rectangle class with properties for width and height,
which are enforced to be positive integers.
"""


class Rectangle:

    """
    Constructor for the Rectangle class, initializing a rectangle with the
    given width and height values. Defaults to zero if no values are provided.
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """
    Property getter for the height attribute,
    returns the private variable __height.
    """

    @property
    def height(self):
        return self.__height

    """
    Property setter for the height attribute, validating that the input is an
    integer and greater than or equal to 0. Raises a TypeError otherwise.
    """

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
    Property getter for the width attribute,
    returns the private variable __width.
    """

    @property
    def width(self):
        return self.__width

    """
    Property setter for the width attribute, validating that the input is an
    integer and greater than or equal to 0. Raises a TypeError otherwise.
    """

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
