#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    a -= 1
    if a == 1:
        b = "argument"
    else:
        b = "arguments"
    if a == 0:
        c = "."
    else:
        c = ":"
    print("{} {} {}".format(a, b, c))
    for i in range(1, (a + 1)):
        print("{}: {}".format(i, sys.argv[i]))
