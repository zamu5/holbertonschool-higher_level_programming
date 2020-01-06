#!/bin/bash
# ends a POST request to the passed URL, and displays the body of the response
curl -sL --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
