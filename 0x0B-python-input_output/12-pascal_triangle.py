#!/usr/bin/python3
"""pascal"""

def fac(n):
    """calculate factorial"""
    if n == 0:
        return 1
    result = 1
    for i in range(1, (n + 1)):
        result *= i
    return result

def pascal_triangle(n):
    """pascal"""
    pascal = []
    for i in range(0, n):
        pascal.append([])
        for j in range(0, (i + 1)):
            pascal[i].append(int(fac(i) / (fac(i - j) * fac(j))))
    return pascal
