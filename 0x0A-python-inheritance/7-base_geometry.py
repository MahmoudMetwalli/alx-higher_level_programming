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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
