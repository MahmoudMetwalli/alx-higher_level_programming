#!/usr/bin/python3
"""BASE"""


class Base:
    """BASE CLASS"""
    __nb_objects = 0

    def __init__(self, base_id=None):
        """CLASS CONSTRUCTOR"""
        if base_id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = base_id
