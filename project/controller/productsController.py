import requests
import json
import re
import os

url = 'https://www.foodrepo.org/api/v3/products'

def getAllProducts(secret):
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token token=' + secret
    }
    print(secret)
    response = requests.request("GET", url, data=payload, headers=headers)
    data = json.loads(response.text)

    pages = []
    pager = {}
    for x in range(int(re.search('=(.*)&page', data['links']['last']).group(1))):
            pages.append(x)
    pages.pop(0)
    pager['currentpage'] = int(re.search('=(.*)&page', data['links']['self']).group(1))
    pager['totalItems'] = int(re.search('=(.*)&page', data['links']['last']).group(1)) * 10
    pager['pageSize'] = 10
    pager['totalPages'] = int(re.search('=(.*)&page', data['links']['last']).group(1)) / 2
    pager['startPage'] = 1
    pager['endPage']= int(re.search('=(.*)&page', data['links']['last']).group(1))
    pager['pages'] = pages
    data['pager'] = pager
    return data