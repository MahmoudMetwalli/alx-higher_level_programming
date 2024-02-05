#!/usr/bin/python3
"""task 12"""


class MyInt(int):
    """MyInt"""

    def __eq__(self, value):
        """reverse == opeartor"""
        return self.real != value

    def __ne__(self, value):
        """reverse != operator"""
        return self.real == value
