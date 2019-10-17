#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as f:
        l = sum(1 for line in f)
        f.close
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            nb_lines = l
        cont = 0
        while cont < nb_lines:
            print("{}".format(f.readline()), end="")
            cont += 1
