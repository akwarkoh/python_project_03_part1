#!/usr/bin/env python3

import requests
import json
from pprint import pprint
import urllib.request
import crayons

# sends a get request
URL = "http://127.0.0.1:2224/"
resp = requests.get(URL)

# Prints the data requested from the api
pprint(resp)

# sends an http get request 
resp = urllib.request.urlopen(URL)
response = resp.read()
# prep bytes decode
encoding = resp.info().get_content_charset('utf-8')
# decode data
data = json.loads(response.decode(encoding))
# prints pythonic data
print(crayons.green(data))
# prints data type
print(crayons.red(type(data)))
print(crayons.yellow(data[1]['country']))