#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a
parameter, and displays the body of the response
"""
from urllib import parse
from urllib import request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    package = parse.urlencode(values)
    package = package.encode('ascii')
    request0 = request.Request(url, package)
    with request.urlopen(request0) as response:
        page = response.read()
        print(page.decode('utf-8'))
