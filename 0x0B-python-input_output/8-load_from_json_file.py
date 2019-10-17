#!/usr/bin/python3
def load_from_json_file(filename):
    """Create object from a JSON file"""

    import json

    with open(filename) as f:
        return json.loads(f.read())
