#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = ([[i*i for i in row] for row in matrix])
    return copy
