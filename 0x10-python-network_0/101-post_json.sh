#!/bin/bash
# send a json file
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
