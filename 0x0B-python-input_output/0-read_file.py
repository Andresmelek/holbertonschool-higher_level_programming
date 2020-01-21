#!/usr/bin/python3
"""
Function that reads a text file UTF8
"""


def read_file(filename=""):
    with open(filename, encoding='UTF8') as file:
        print(file.read(), end="")
