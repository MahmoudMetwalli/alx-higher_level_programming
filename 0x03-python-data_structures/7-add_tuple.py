#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = []
    b = []
    k = len(tuple_a)
    i = 0
    while i < k:
        a.append(tuple_a[i])
        i += 1
    while i < 2:
        a.append(0)
        i += 1
    k = len(tuple_b)
    i = 0
    while i < k:
        b.append(tuple_b[i])
        i += 1
    while i < 2:
        b.append(0)
        i += 1
    tuple_c = (a[0]+ b[0]), (a[1]+ b[1])
    return tuple_c
