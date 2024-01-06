#!/usr/bin/env python3
def no_c(my_string):
    a = len(my_string)
    new_str = []
    for i in range(a):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            new_str.append(my_string[i])
    str = ""
    for ele in new_str:
        str += ele
    return str
