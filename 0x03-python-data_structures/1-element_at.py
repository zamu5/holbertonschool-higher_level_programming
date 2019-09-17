#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for x in my_list:
        if x == idx + 1:
            return (x)
        elif x > idx + 1:
            return None
