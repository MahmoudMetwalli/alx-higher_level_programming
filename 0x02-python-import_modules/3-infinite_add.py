#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    a -= 1
    b = 0
    for i in range(1, (a + 1)):
        b += int(sys.argv[i])
    print(f"{b}")
