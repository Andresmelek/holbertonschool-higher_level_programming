#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error_m:
        print("Exception: {:s}".format(str(error_m)), file=sys.stderr)
        return None
