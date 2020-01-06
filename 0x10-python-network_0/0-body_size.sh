#!/bin/bash
# print the size of the body response
curl -sI http://2f3050f3cd04.38.hbtn-cod.io:5000 | awk '/Content-Length/ {print $2}'
