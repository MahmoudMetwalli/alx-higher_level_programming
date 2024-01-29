#!/usr/bin/python3
"""module that adds two integers"""
def add_integer(a, b=98):
    """function that adds two integers"""
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
