#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    number = len(argv)
    add = 0
    for i in range(1, number):
        add += int(argv[i])
    print('{}'.format(add))
