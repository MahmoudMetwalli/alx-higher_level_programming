#!/usr/bin/python3
"""To Find Peaks"""

def find_peak(list_of_integers):
    if len(list_of_integers) is not 0:
        return max(list_of_integers)
    else:
        return None
