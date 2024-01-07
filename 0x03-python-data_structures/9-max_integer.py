#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        return None
    j = my_list[0]
    for i in range(1, a):
        if my_list[i] > j:
            j = my_list[i]
    return j
