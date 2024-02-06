#!/usr/bin/python3
"""reads and prints file"""


def read_file(filename=""):
    """reads nad prints file"""
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read())
