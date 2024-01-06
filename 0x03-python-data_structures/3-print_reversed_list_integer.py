#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    a -= 1
    for i in range(a + 1):
        print("{:d}".format(my_list[a - i]))
