#!/usr/bin/python3
# search SW

import sys
import requests

if __name__ == "__main__":
    search = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    req = requests.get(search)
    json_sw = req.json()
    print("Number of results: {}".format(json_sw.get('count')))
    for result in json_sw.get('results'):
        print("{}".format(result.get('name')))
