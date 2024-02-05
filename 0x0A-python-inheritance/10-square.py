#!/usr/bin/python3
"""an empty class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """init"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """area"""
        return self.__size ** 2

    def __str__(self):
        """print"""
        return f"[Rectangle] {self.__size}/{self.__size}"
