#!/usr/bin/python3
"""
This is a simple script to demonstrate
how to use the PyInquirer library in Python
"""
from models.rectangle import Rectangle


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
        return f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.width}"
