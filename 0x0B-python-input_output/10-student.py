#!/usr/bin/python3
"""defines a student"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        """initsss"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        diction = {}
        if isinstance(attrs, list):
            for i in attrs:
                for key, value in vars(self).items():
                    if i == key:
                        diction[i] = value
            return diction
        return vars(self)
