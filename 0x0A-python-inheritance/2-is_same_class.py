#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ Exact same object """
    if type(obj) == a_class:
        return True
    return False
