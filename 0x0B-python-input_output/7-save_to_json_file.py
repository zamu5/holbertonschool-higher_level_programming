#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    """Save Object to a file"""
    import json

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
