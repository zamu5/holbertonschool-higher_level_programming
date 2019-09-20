#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    valor = 0
    for key in range(len(roman_string)):
        if key > 0 and num[roman_string[key]] > num[roman_string[key - 1]]:
            valor += num[roman_string[key]] - 2 * num[roman_string[key - 1]]
        else:
            valor += num[roman_string[key]]
    return valor
