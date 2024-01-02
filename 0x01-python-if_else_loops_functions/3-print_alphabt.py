#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if (i!=65) and (i!=71):
        print("{:c}".format(i), end="")
