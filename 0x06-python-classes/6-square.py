#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    def __init__(self, size=0, position=(0, 0)):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = (position[0], position[1])
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    @property
    def position(self):
        return self.__position
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
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
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
