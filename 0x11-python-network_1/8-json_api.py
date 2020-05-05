#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":

    try:
        datas = {'q': argv[1]}
    except Exception:
        datas = {'q': ""}
        pass

    try:
        request = requests.post('http://0.0.0.0:5000/search_user', data=datas)
        jsonreq = request.json()
        if 'id' not in jsonreq or 'name' not in jsonreq:
            print("No result")
        else:
            print("[{}] {}".format(jsonreq.get('id'), jsonreq.get('name')))

    except Exception:
            print("Not a valid JSON")
