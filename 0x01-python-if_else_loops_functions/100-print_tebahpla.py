#!/usr/bin/python3
x = 122
while x > 96:
    print("{}".format(chr(x) if x % 2 == 0 else chr(x - 32)), end="")
    x = x - 1
