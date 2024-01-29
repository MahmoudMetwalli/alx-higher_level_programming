#!/usr/bin/python3
"""module that defines a class rectangle"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        """function for rectangle instantiation"""
        self.width = width
        self.height = height
    @property
    def width(self):
        """function to retrive width"""
        return self.width
    @width.setter
    def width(self, value):
        """function to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        """function to retrive height"""
        return self.height
    @height.setter
    def height(self, value):
        """function to set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
