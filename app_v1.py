from flask_restplus import Api
from flask import Blueprint
from resources.app import api_ns as ns1

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint,
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1, path='/resources')
