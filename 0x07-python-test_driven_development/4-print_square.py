#!/usr/bin/python3
"""this module is for printing squares"""


def print_square(size):
    """function that prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
