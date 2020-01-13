#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        page = response.info()
    print(page.get('X-Request-Id'))
