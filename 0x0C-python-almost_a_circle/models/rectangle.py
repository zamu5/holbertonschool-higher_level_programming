#!/usr/bin/python3
"""
Module taht contains the class Rectangule
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width"""

        return self.__width

    @width.setter
    def width(self, value):
        """with setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y"""

        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area"""

        return self.__width * self.__height

    def display(self):
        """display"""

        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """str"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """update"""

        if args is not None and len(args) is not 0:
            list = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to dictionary"""

        list = ["x", "y", "id", "height", "width"]
        val = [self.x, self.y, self.id, self.height, self.width]
        return dict(zip(list, val))
