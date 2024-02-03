#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list\
 of lists) of integers/floats")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
