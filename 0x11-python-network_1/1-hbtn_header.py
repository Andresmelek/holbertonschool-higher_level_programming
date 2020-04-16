#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id
"""
from sys import argv
from urllib import request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        info = response.info()
        print(info['X-Request-Id'])
