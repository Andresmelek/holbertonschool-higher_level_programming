#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as error_m:
        print("Exception: {:s}".format(str(error_m)), file=sys.stderr)
        return False
