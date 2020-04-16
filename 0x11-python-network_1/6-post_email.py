#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    reqquest = requests.post(argv[1], data=email)
    print(request.text)
