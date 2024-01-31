#!/usr/bin/python3
"""this module is for text indentation"""


def text_indentation(text):
    """prints a 2 new lines after each of these characters: ., ? and :"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for t in ".?:":
        text = (t + "\n\n").join(
            [line.strip(" ") for line in text.split(t)])
    print(text, end="")
