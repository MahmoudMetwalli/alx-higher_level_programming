#!/usr/bin/python3
"""an empty class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """an empty class Rectangle"""
    def __init__(self, width, height):
        """Initiation"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
