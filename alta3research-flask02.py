#!/usr/bin/env python3

import requests
import json
from pprint import pprint
import urllib.request


URL = "http://127.0.0.1:2224/"

resp = requests.get(URL)

pprint(resp)


resp = urllib.request.urlopen(URL)
response = resp.read()
encoding = resp.info().get_content_charset('utf-8')
data = json.loads(response.decode(encoding))

print(data)
