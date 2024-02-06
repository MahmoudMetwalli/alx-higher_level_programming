#!/usr/bin/python3
"""appending"""


def append_write(filename="", text=""):
    """appending"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        num_wrote = a_file.write(text)
    return num_wrote
