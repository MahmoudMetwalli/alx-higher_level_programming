#!/usr/bin/python3
"""to be locked"""


class LockedClass:

    def __init__(self):
        """to be locked"""
        self.__dict__

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value
