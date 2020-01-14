#!/usr/bin/python3
# search SW

import sys
import requests

if __name__ == "__main__":
    search = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    req = requests.get(search)
    json_sw = req.json()
    print("Number of results: {}".format(json_sw.get('count')))
    while json_sw.get('next') is not None:
        for result in json_sw.get('results'):
            print("{}".format(result.get('name')))
            for i in result.get('films'):
                jso = requests.get(i).json()
                print("\t{}".format(jso.get('title')))
        json_sw = requests.get(json_sw.get('next')).json()
    for result in json_sw.get('results'):
        print("{}".format(result.get('name')))
        for i in result.get('films'):
            jso = requests.get(i).json()
            print("\t{}".format(jso.get('title')))
