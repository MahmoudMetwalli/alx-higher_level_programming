#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    a = len(my_list)
    a -= 1
    if not idx < 0 and not idx > a:
        my_list[idx] = element
    return my_list
