#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    l = 0
    with open(filename, 'r') as f:
        while f.readline() != "":
            l += 1
    f.close()
    with open(filename, 'r+') as f:
        lines = f.readlines()
        st = ""
        i = 0
        while i < l:
            if search_string in lines[i]:
                st += lines[i] + new_string
            else:
                st += lines[i]
            i += 1
    with open(filename, 'w+') as f:
        f.write(st)
