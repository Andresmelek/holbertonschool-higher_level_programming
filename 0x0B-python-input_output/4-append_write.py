#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='UTF8') as file:
        n_text = 0
        n_text = file.write(text)
        return n_text
