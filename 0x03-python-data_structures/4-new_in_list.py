#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list)
    a -= 1
    new_list = []
    for i in range(a + 1):
        new_list.append(my_list[i])
    if not idx < 0 and not idx > a:
        new_list[idx] = element
    return new_list
