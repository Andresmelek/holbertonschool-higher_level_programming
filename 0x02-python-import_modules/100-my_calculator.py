#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(argv[1])
    c = argv[2]
    b = int(argv[3])

    if c == '+':
        print('{} {} {} = {}'.format(a, c, b, add(a, b)))
    elif c == '-':
        print('{} {} {} = {}'.format(a, c, b, sub(a, b)))
    elif c == '*':
        print('{} {} {} = {}'.format(a, c, b, mul(a, b)))
    elif c == '/':
        print('{} {} {} = {}'.format(a, c, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
