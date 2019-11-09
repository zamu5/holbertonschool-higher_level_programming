#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for row in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        st = ""
        if self.__size == 0:
            return st
        else:
            st = ("\n" * self.__position[1])
            for row in range(self.__size - 1):
                st += (" " * self.__position[0] + "#" * self.__size + "\n")
            st += (" " * self.__position[0] + "#" * self.__size)
            return st
