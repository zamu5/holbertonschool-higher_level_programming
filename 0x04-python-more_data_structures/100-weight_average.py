#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    return(sum([i*j for i, j in my_list]) / sum([j for i, j in my_list]))
