#!/usr/bin/python3
# sends a request to the URL and displays the body of the response

from urllib.error import URLError
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except URLError as e:
        print("Error code: {}".format(e.code))
