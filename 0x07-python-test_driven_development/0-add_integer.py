#!/usr/bin/python3
"""

this module have the add integers function

"""


def add_integer(a, b=98):
    """
    The function add_integers returns the adding of two numbers
    """
    if a is None or (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if b is None or (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
