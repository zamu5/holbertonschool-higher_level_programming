#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if not flag:
            if i is '.' or i is '?':
                print("{}\n".format(i))
                flag = 1
            else:
                print("{}".format(i), end="")
        else:
            if i is not " ":
                flag = 0