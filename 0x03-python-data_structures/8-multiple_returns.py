#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        b = "None"
    else:
        b = sentence[0]
    t = len(sentence), b
    return t
