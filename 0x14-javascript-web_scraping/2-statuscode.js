#!/usr/bin/node
import request

response = request.get(url)
print('code: ', response.status_code)
