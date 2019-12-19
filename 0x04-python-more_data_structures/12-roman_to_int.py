#!/usr/bin/python3
def roman_to_int(roman_string):
    matrix = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string:
        number = matrix[roman_string[len(roman_string) - 1]]
        for i in range((len(roman_string) - 1), 0, - 1):
            one = matrix[roman_string[i]]
            zero = matrix[roman_string[i - 1]]
            if zero >= one:
                number += zero
            else:
                number -= zero
    else:
        return 0
    return number
