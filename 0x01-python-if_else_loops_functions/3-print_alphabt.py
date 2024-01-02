#!/usr/bin/python3
i = 61
while (i != 173):
    if (i == 65) or (i == 71):
        i += 1
        continue
    else:
        print("{:c}".format(i), end="")
    i += 1
