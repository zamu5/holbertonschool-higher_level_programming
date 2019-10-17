#!/usr/bin/python3
import sys
import os

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

if __name__ == "__main__":

    files = 'add_item.json'

    if os.path.exists(files):
        try:
            l = load_from_json_file(files)
        except:
            l = []
    else:
        l = []
    for i in range(1, len(sys.argv)):
        l.append(sys.argv[i])
    save_to_json_file(l, files)
