from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import requests
import json
import re

app = Flask(__name__)
CORS(app)
url = 'https://www.foodrepo.org/api/v3/products'
@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/products', methods=['GET'])
def getProducts():
  querystring = request.args

  payload = ""
  headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Token token=aeab5454535b1ee71a073111698dd871'
  }

  response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
  data = json.loads(response.text)

  pages = []
  pager = {}
  for x in range(int(re.search('=(.*)&page', data['links']['last']).group(1))):
        pages.append(x)
  
  pager['currentpage'] = int(re.search('=(.*)&page', data['links']['self']).group(1))
  pager['totalItems'] = int(re.search('=(.*)&page', data['links']['last']).group(1)) * 10
  pager['pageSize'] = 10
  pager['totalPages'] = int(re.search('=(.*)&page', data['links']['last']).group(1)) / 2
  pager['startPage'] = 1
  pager['endPage']= int(re.search('=(.*)&page', data['links']['last']).group(1))
  pager['pages'] = pages
  data['pager'] = pager
  resdata = data
  pages.pop(0)

  res = app.response_class(
    response=json.dumps(resdata),
    status=200,
    mimetype='application/json'
  )
  return res