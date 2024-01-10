#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = [x for x in sorted(a_dictionary)]
    for i in keys:
        print("{}: {}".format(i, a_dictionary[i]))
