#!/usr/bin/python3
"""
    Project 0x05 - Test driven development
    Task 1
    Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of matrix by div
    """

    new_matrix = []
    strError = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for val in row:
            if type(val) not in [int, float]:
                raise TypeError(strError)
        new_matrix.append(list(map(lambda n: round(n/div, 2), row)))

    return (new_matrix)
