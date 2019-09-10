#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if (x < y):
            print(x, end="")
            if (x != 8):
                print(y, end=", ")
            else:
                print(y)
