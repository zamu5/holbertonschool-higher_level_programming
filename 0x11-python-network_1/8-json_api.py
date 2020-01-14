#!/usr/bin/python3
# sends a POST request to http://0.0.0.0:5000/search_user with the letter

import sys
import requests

if __name__ == "__main__":
    data = {'q': ""}
    try:
        data['q'] = sys.argv[1]
    except:
        None
    req = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_res = req.json()
        if not json_res:
            print("No result")
        else:
            print("[{}] {}".format(json_res.get('id'), json_res.get('name')))
    except:
        print("Not a valid JSON")
