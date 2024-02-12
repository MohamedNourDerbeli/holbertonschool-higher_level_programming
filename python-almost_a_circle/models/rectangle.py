#!/usr/bin/python3
"""
This is a simple script to demonstrate
how to use the PyOpenGL library to draw a
"""
from models.base import Base


class Rectangle(Base):
    """docstring for Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def x(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__y = value
