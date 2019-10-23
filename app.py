from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import controller.productsController as productsControllerModule
import requests
import json
import re
import os
import sqlite3

app = Flask(__name__)
CORS(app)
app.config.from_pyfile(os.path.join(".", "config/app.conf"), silent=False)

@app.route('/')
def index():
  return app.config.get('PRODUCTS_SECRET')
  
@app.route('/products', methods=['GET'])
def getProducts():
  resdata = productsControllerModule.getAllProducts(app.config.get('PRODUCTS_SECRET'))
  res = app.response_class(
    response=json.dumps(resdata),
    status=200,
    mimetype='application/json'
  )
  return res