#!/usr/bin/python3
def from_json_string(my_str):
    """From JSON string to Object"""
    import json

    return json.loads(my_str)
