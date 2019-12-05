from flask import Blueprint
from flask_restplus import Api, Namespace
from .Hello import Hello
from .Category import CategoryResource
from .products import Products

api_ns = Namespace(
'api', # The namespace name
'Root Namespace of this api.', # An optionale short description
'api' # An optional prefix path. If not provided, prefix is /+name
# decorators (list) – A list of decorators to apply to each resources
# validate (bool) – Whether or not to perform validation on this namespace
# ordered (bool) – Whether or not to preserve order on models and marshalling 
)


# Route
api_ns.add_resource(Hello, '/Hello')
api_ns.add_resource(CategoryResource, '/Category')
api_ns.add_resource(Products, '/products')
