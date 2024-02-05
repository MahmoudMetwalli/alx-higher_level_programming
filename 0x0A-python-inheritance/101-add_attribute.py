#!/usr/bin/python3
"""no more attributes"""


def add_attribute(obj, attr, value):
    """adds attribute"""
    for i in dir(type(obj)):
        if i == "__dict__":
            setattr(obj, attr, value)
            return
    raise TypeError("can't add new attribute")
