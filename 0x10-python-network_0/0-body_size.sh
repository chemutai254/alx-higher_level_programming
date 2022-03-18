#!/bin/bash
# Bash script that takes in a URL, sends a request
# And displays the size of the body of the response
curl -s "$1" | wc -c
