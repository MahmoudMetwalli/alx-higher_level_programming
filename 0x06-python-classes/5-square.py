#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    def __init__(self, size=0):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    def area(self):
        return self.__size**2
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    @property
    def size(self):
        return self.__size
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#")
