#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("""matrix must be a matrix (list of lists) \
        of integers/floats""")
    if len(matrix) is 0 or not all(len(l) > 0 for l in matrix):
        raise TypeError("""matrix must be a matrix (list of lists) \
of integers/floats""")
    if not all(len(l) == len(matrix[0]) for l in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("""matrix must be a matrix (list of lists) \
of integers/floats""")
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("""matrix must be a matrix (list of lists) \
of integers/floats""")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    return ([[round(i / div, 2) for i in row] for row in matrix])
