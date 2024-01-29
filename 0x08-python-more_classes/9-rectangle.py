#!/usr/bin/python3
"""module that defines a class rectangle"""


class Rectangle:
    """class rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """function for rectangle instantiation"""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """function that returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.height * rect_1.width) >= (rect_2.height * rect_2.width):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """function that returns a new instance with width==height==size"""
        a = size
        return cls(a, a)

    def __repr__(self):
        """function that returns a string representation of a rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __str__(self):
        """function that returns printable rectangle of hashs"""
        if self.height != 0 and self.width != 0:
            for i in range(0, self.height):
                for j in range(0, self.width):
                    print("{}".format(self.print_symbol), end="")
                if i != self.height - 1:
                    print()
        return ""

    def __del__(self):
        """function that prints a string upon deletion of an instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def perimeter(self):
        """function that returns the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
