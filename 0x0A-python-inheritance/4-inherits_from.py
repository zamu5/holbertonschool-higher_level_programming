#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Only sub class of """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
