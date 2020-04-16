#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":

    reque = reque.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(reque.json().get('id'))
