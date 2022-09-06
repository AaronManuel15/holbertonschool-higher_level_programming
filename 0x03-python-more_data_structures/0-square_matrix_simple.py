#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        rows = len(matrix)
        columns = len(matrix[0])

        matrix_T = []
        for j in range(columns):
            row = []
            for i in range(rows):
                row.append(matrix[i][j] ** 2)
            matrix_T.append(row)

        return matrix_T
