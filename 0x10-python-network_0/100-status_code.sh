#!/bin/bash
# displays only the status code of the response.
curl -s -w "%{http_code}" -o /dev/null "$1"
