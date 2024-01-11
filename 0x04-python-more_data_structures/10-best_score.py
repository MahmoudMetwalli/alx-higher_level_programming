#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    flag = 0
    for i in a_dictionary:
        if flag == 0:
            k = i
            m = a_dictionary[i]
            flag = 1
        if a_dictionary[i] > m:
            k = i
            m = a_dictionary[i]
    return k
