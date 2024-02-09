#!/usr/bin/python3

"""
This is a base class for geometry-related objects.
"""


class BaseGeometry:
    """
    This is the base class for all geometry-related classes in this package.
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
