#!/usr/bin/python3
def read_file(filename=""):
    """Read a file"""
    with open(filename, 'r') as f:
        print("{}".format(f.read()))
