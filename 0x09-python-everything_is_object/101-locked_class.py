#!/usr/bin/python3
"""to be locked"""


class LockedClass:

    __slots__ = ['first_name']

    def __init__(self, value=""):
        """to be locked"""
        self.first_name = value
