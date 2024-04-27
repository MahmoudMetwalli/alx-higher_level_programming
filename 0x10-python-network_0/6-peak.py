#!/usr/bin/python3
"""To Find Peaks"""

def find_peak(list_of_integers):
    """BRUTE force implementation
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
