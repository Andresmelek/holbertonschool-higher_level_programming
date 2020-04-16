#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body
of the response.
"""
import urllib
from urllib import request
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
