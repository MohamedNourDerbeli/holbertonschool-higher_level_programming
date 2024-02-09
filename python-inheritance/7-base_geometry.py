#!/usr/bin/python3
"""
This is a base class for geometry-related objects.
"""


class BaseGeometry:
    """
    This is the base class for all
    geometry-related classes in this package.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
