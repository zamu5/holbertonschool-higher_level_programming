#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy =  dict([(y, x*2) for y, x in a_dictionary.items()])
    return copy
