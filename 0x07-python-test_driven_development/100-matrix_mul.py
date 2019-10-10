#!/usr/bin/python3
"""
Module have function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not [[isinstance(row, list)] for row in m_a]:
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if not [[isinstance(row, list)] for row in m_b]:
        raise TypeError("m_b must be a list of lists")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise TypeError("m_b can't be empty")
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")
    if not all(len(l) == len(m_a[0]) for l in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(l) == len(m_b[0]) for l in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    r1 = []
    i1 = 0

    for a in m_a:
        r2 = []
        i2 = 0
        num = 0
        while (i2 < len(m_b[0])):
            num += a[i1] * m_b[i1][i2]
            if i1 == len(m_b) - 1:
                i1 = 0
                i2 += 1
                r2.append(num)
                num = 0
            else:
                i1 += 1
        r1.append(r2)

    return r1
