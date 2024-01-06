#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)
    a -= 1
    if (idx < 0) or (idx > a):
        return "None"
    else:
        return my_list[idx]
