#!/usr/bin/python3
# look for commits
import sys
import requests


if __name__ == "__main__":
    try:
        url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1],
                                                                  sys.argv[2])
        req = requests.get(url)
        json_res = req.json()
        for commit in range(0, 10):
            print("{}: {}".format(json_res[commit].get('sha'),
                                  json_res[commit].get('commit')
                                  .get('author').get('name')))
    except:
        None
