#!/usr/bin/python3
"""module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    result = []
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(message)
    if len(matrix) == 0:
        raise TypeError(message)
    for i in matrix:
        if type(i) != list:
            raise TypeError(message)
        if len(i) == 0:
            raise TypeError(message)
        for j in i:
            if type(j) is not int:
                if type(j) is not float:
                    raise TypeError(message)
    a = len(matrix[0])
    for i in range(0, len(matrix)):
        if a != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        a = len(matrix[i])
    if type(div) is not int:
        if type(div) is not float:
            raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(0, len(matrix)):
        result.append([])
        for j in range(0, len(matrix[i])):
            result[i].append(round((matrix[i][j] / div), 2))
    return result
