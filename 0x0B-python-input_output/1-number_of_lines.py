#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        cont = 0
        while f.readline() != "":
            cont += 1
    return cont
