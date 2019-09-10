#!/usr/bin/env python3
def uppercase(str):
    for x in str:
        i = ord(x)
        if i > 96 and i < 123:
            i = i - 32
        print(chr(i), end="")
    print("")
