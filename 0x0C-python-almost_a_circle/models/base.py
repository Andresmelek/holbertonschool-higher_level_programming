#!/usr/bin/python3
import json
import os


class Base():
    """Global variable"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        n_list = []
        with open(filename, 'w', encoding='UTF-8') as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                for i in list_objs:
                    n_list.append(i.to_dictionary())
                file.write(cls.to_json_string(n_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = cls(1, 1)
        if cls is Square:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            list_i = []
            filename = cls.__name__ + ".json"
            with open(filename, 'r') as file:
                jsonfile = cls.from_json_string(file.read())
                for i in jsonfile:
                    list_i.append(cls.create(**i))
                return list_i
        except:
            return []
