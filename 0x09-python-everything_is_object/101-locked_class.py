#!/usr/bin/python3
"""to be locked"""


class LockedClass:

    def __init__(self):
        """to be locked"""
        self.__dict__

    def __setattr__(self, attr, value):
        if attr != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{attr}'")
        else:
            self.__dict__[attr] = value
