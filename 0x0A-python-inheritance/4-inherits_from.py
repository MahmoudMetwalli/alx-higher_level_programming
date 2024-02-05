#!/usr/bin/python3
"""checks object"""


def inherits_from(obj, a_class):
    """checks object"""
    if isinstance((obj), a_class) and not type(obj) == a_class:
        return True
    else:
        return False
