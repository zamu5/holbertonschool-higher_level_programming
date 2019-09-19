#!/usr/bin/python3
def uniq_add(my_list=[]):
    for i in range(len(my_list)):
        for j in my_list[i+1:]:
            if my_list[i] == j:
                del my_list[i]
    return sum(my_list)
