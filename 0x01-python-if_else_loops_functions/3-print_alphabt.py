#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if (i == 65) or (i == 71):
        continue
    else:
        print("{:c}".format(i), end="")
