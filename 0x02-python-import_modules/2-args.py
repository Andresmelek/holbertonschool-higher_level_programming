#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = (sys.argv)
    number = len(argv)
    if number == 2:
        print('{} argument:'.format(number - 1))
        print('1: {}'.format(argv[1]))
    elif number == 1:
        print('{} arguments.'.format(number - 1))
    else:
        print('{} arguments:'.format(number - 1))
        for i in range(1, number):
            print('{}: {}'.format(i, argv[i]))
