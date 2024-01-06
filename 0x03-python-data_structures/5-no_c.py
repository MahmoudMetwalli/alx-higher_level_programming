#!/usr/bin/env python3
def no_c(my_string):
    word = ""
    for ele in my_string[:]:
        if ele != 'c' and ele != 'C':
            word += ele
    return word
