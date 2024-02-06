#!/usr/bin/python3
"""writes to file"""


def write_file(filename="", text=""):
    """writes to file"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        num_wrote = a_file.write(text)
    return num_wrote
