#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    t = [[1]]
    for x in range(n - 1):
        t.append([f + n for f, n in zip(t[-1] + [0], [0] + t[-1])])
    return t
