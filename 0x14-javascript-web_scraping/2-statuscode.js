#!/usr/bin/node
import requests

response = requests.get(url)
print('code: ', response.status_code)
