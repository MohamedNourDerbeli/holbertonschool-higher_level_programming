#!/usr/bin/python3
"""
This is a simple script to demonstrate
how to use the PyInquirer library in Python
"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """A class that represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """

        Returns:
            _type_: _description_
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for width and height properties of the rectangle."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for width and height properties of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Updates the position or dimensions of the square."""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Convert the Square object into a dictionary."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "size": self.size,
        }
