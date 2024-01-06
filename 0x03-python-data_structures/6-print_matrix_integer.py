#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    k = len(matrix)
    for i in range(k):
        q = len(matrix[i])
        for j in range(q):
            if j == (q - 1):
                print("{}".format(matrix[i][j]),end = "")
            else:
                print("{} ".format(matrix[i][j]),end = "")
        print()  
