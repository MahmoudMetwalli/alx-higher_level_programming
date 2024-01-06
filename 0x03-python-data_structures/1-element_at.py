#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)
    a -= 1
    if (idx < 0) or (idx > a):
        print("None")
    else:
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
