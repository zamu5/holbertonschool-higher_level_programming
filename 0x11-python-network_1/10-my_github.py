#!/usr/bin/python3
# github autentication

import sys
import requests

if __name__ == "__main__":
    req = requests.get('https://api.github.com/user', auth=(sys.argv[1],
                                                            sys.argv[2]))
    json_res = req.json()
    print(json_res.get('id'))
