#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a base geometry class BaseGeometry."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {str(self.__width)}/{str(self.__height)}"

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height
