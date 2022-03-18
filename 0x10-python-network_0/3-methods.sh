#!/bin/bash
# Script that takes a URL and displays HTTP method server
curl -sI "$1" | grep Allow | cut -d ':' -f2 | xargs
