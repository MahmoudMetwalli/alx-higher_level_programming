#!/usr/bin/env python3
def no_c(my_string):
    str4 = ""
    for ele in my_string:
        if ele == 'c' or ele == 'C':
            continue
        str4 += ele
    return str4
