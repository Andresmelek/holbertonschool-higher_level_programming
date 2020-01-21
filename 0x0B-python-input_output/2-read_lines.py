#!/usr/bin/python3
"""
function that reads n lines of a text file (UTF8) and prints it to stdout:
"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='UTF8') as file:
        count = 0
        for i in file:
            count += 1
            if nb_lines <= 0 or nb_lines >= count:
                print(i, end="")
