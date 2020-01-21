#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='UTF8') as file:
        n_text = 0
        n_text = file.write(text)
        return n_text
