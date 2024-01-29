#!/usr/bin/python3
"""module that defines a class rectangle"""


class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        """function for rectangle instantiation"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """function to retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """function to set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """function to retrive width"""
        return self.__width

    @width.setter
    def width(self, value):
        """function to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """function that returns rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """function that returns the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
        
    def __str__(self):
        """function that returns printable rectangle of hashs"""
        if self.height != 0 and self.width != 0:
            for i in range(0, self.height):
                for j in range(0, self.width):
                    print("#", end="")
                if i != self.height - 1:
                    print()
        return ""
