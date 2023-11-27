import json

import requests



url = "http://httpbin.org/post"
payload = {"key1": "value1", "key2": "value2"}
headers = {"accept": "application/json", "Content-Type": "application/json"}
r = requests.post(url, data=payload, headers=headers)
print(r.request.headers)
print(r.headers)