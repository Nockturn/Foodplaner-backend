''' from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import requests
import json
import os

app = Flask(__name__)
CORS(app)
app.config.from_pyfile(os.path.join("../../", "config/app.conf"), silent=False)
 '''
from controller import productsController as productsControllerModule
import app
import json
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

''' if __name__ == "__main__":
    app.run() '''