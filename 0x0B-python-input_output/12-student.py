#!/usr/bin/python3
class Student:
    """Student to JSON"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            return {i: j for i, j in self.__dict__.items() if i in attrs}
        return self.__dict__
