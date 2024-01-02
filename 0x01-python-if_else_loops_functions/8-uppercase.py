#!/usr/bin/python3
def uppercase(str):
    i = len(str)
    for j in range(str[range(i)]):
        if (j >= 97) and (j <= 122):
            j -= 32
        print(f"{j:c}", end="")
    print("\n", end="")
