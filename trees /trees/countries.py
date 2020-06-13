
#!/bin/python3

import sys
import os
import requests
import json
from requests import HTTPSession


# Complete the function below.
# https://jsonmock.hackerrank.com/api/countries/search?name=
def getCountries(s, p):
    http = HTTPSession
    num = {'total_pages': 11}
    name = {'data': 'name'}
    r = requests.append(get('https://jsonmock.hackerrank.com/api/countries/search?name=&page=', page=NUM)
    s=requests.get(
        'https://jsonmock.hackerrank.com/api/countries/search?name=', name=name)
    s.status_code



f=open(os.environ['OUTPUT_PATH'], 'w')


try:
    _s=str(input())
except:
    _s=None


_p=int(input())

res=getCountries(_s, _p)
f.write(str(res) + "\n")

f.close()
