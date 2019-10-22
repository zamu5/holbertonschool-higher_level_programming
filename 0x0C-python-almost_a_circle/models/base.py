#!/usr/bin/python3
"""this module have the base class"""

import json
import os


class Base:
    """Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        if list_dictionaries is None and list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        li = []
        fi = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for i in range(len(list_objs)):
                li.append(list_objs[i].to_dictionary())
        li = cls.to_json_string(li)
        with open(fi, 'w') as f:
            f.write(li)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            create = cls(5, 5)
        elif cls.__name__ == "Square":
            create = cls(5)
        create.update(**dictionary)
        return create

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        fi = "{}.json".format(cls.__name__)
        if os.path.exists(fi) is False:
            return []
        with open(fi, 'r') as f:
            lis = f.read()
        lic = cls.from_json_string(lis)
        lii = []
        for i in range(len(lic)):
            lii.append(cls.create(**lic[i]))
        return lii
