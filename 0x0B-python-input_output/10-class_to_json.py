#!/usr/bin/python3
"""
function that returns the dictionary
description with simple data
"""


def class_to_json(obj):
    return obj.__dict__
