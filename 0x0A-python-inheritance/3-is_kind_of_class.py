#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Same class or inherit from """
    if isinstance(obj, a_class):
        return True
    return False
