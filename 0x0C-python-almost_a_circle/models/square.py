#!/usr/bin/python3
"""This module hace the class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}".format(self.id, self.x,
                                                    self.y, self.width)

    def update(self, *args, **kwargs):
        if args is not None and len(args) is not 0:
            list = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if list[i] != "size":
                    setattr(self, list[i], args[i])
                else:
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        lis = ["id", "size", "x", "y"]
        val = [self.id, self.size, self.x, self.y]
        return dict(zip(lis, val))
