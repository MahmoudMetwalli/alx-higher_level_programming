#!/usr/bin/python3
"""an empty class BaseGeometry"""


class BaseGeometry:
    """an empty class BaseGeometry"""

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """an empty class Rectangle"""
    def __init__(self, width, height):
        """Initiation"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
