#!/usr/bin/python3
def uppercase(str):
    for x in str:
        i = ord(x)
        if i > 96 and i < 123:
            i = i - 32
        print("{}".format(chr(i)), end="")
    print()
