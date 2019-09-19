#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict([(y, x*2) for y, x in a_dictionary.items()])
