#!/usr/bin/python3
"""solves the N queens problem"""


import sys

def main():
    """solves the N queens problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = eval(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    print("OK")

if __name__ == "__main__":
    main()
