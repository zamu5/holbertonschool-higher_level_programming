#!/usr/bin/python3
class MyInt(int):
    """My integer """
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
