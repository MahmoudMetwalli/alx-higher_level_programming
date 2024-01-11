#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    l = 0
    for i in a_dictionary:
        if l == 0:
            k = i
            m = a_dictionary[i]
            l = 1
        if a_dictionary[i] > m:
            k = i
            m = a_dictionary[i]
    return k
