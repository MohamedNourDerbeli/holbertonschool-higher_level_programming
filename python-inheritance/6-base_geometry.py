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
