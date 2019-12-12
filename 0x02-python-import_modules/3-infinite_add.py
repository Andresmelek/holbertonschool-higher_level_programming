#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    add = 0
    for i in range(1, len(argv)):
        add += int(argv[i])
    print('{}'.format(add))
