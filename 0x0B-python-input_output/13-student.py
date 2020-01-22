#!/usr/bin/python3
"""
Class student with a list
"""


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        self_directory = self.__dict__
        flag = 0

        if type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    flag += 1
            if len(attrs) == flag:
                directory = {}
                for x in self_directory.keys():
                    if x in attrs:
                        directory[x] = self_directory[x]
                return directory
        else:
            return self_directory

    def reload_from_json(self, json):
        for key, val in json.items():
            self.__dict__[key] = val
