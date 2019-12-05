from flask import request
from flask_restplus import Resource
from Model import db
from project.controller import productsController
# from run import app
import json

""" categories_schema = CategorySchema(many=True)
category_schema = CategorySchema() """

class Products(Resource):
    def get(self):
        resdata = productsController.getAllProducts('aeab5454535b1ee71a073111698dd871')
        return {'status': 'success', 'response': resdata}, 200
