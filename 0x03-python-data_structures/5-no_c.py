#!/usr/bin/python3
def no_c(my_string):
    word = ""
    for ele in my_string:
        if ele == 'c' or ele == 'C':
            continue
        word += ele
    return word
