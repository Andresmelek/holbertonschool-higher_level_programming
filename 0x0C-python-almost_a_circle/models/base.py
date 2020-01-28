#!/usr/bin/python3
""" Base class """
import json
import os
import csv


class Base():
    """ Global variable """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of a list to a file """
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
        """ returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
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
        """ returns a list of instances """
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes to Csv """
        flag = 0
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', encoding='utf-8') as file:
            if cls.__name__ == "Rectangle":
                value_dict = {"width": "width", "height": "height",
                              "x": "x", "y": "y", "id": "id"}
                listt = ["width", "height", "x", "y", "id"]
            else:
                value_dict = {"size": "size", "x": "x", "y": "y", "id": "id"}
                listt = ["size", "x", "y", "id"]

            files = csv.DictWriter(file, fieldnames=listt)
            for instance in list_objs:
                if flag == 0:
                    files.writerow(value_dict)
                    flag += 1
                files.writerow(instance.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes csv """
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', encoding='utf-8') as file:
            i_dict = {}
            i_array = []

            csv_file = csv.DictReader(file)
            for instance in csv_file:
                for key, value in instance.items():
                    i_dict[key] = int(value)
                inst = cls.create(**i_dict)
                i_array.append(inst)
            return i_array
