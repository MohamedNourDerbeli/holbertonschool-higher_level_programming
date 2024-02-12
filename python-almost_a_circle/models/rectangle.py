#!/usr/bin/python3
"""
This is a simple script to demonstrate
how to use the PyOpenGL library to draw a rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class representing a rectangle object."""

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """Getter method for the x coordinate attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x coordinate attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for the y coordinate attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y coordinate attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle object with specified
        dimensions and coordinates."""
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle's attributes on the console."""
        print("\n" * self.__y, end="")
        for line in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args):
        """Update one or more attributes of the rectangle."""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__x = args[4]
