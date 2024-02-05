#!/usr/bin/python3
"""checks if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    else:
        return False
