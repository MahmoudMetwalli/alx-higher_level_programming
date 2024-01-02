#!/usr/bin/python3
def islower(c):
    i = ord(c)
    if (i >= 65) and (i <= 90):
        print(f"{c} => upper")
    else:
        print(f"{c} => lower")
