#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    li = list_of_integers
    if li == []:
        return None
    for i in range(len(li) - 1):
        if i > 0 and i < len(li) - 1:
            if li[i] > li[i - 1] and li[i] > li[i + 1]:
                return li[i]
            if li[i] == li[i - 1] and li[i] == li[i + 1] and li[i] == max(li):
                return li[i]
