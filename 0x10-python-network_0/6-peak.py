#!/usr/bin/python3
"""To Find Peaks"""


def find_peak(list_of_integers):
    """Finding peaks"""
    if len(list_of_integers) == 0:
        return None
    return max(list_of_integers)
"""
    if len(list_of_integers) == 1 or list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    for i in range(1,len(list_of_integers), 2):
        try:
            if list_of_integers[i] >
        except IndexError:
            pass
"""

