#!/usr/bin/python3
"""checks object"""


def is_kind_of_class(obj, a_class):
    """checks object"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
