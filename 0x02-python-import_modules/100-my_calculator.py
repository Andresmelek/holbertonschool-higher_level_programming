#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    a = int(argv[1])
    c = argv[2]
    b = int(argv[3])

    if c == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif c == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif c == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif c == '/':
        print('{} / {} = {}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
