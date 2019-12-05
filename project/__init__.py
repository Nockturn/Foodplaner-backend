from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)
app.config.from_pyfile(os.path.join("../", "config/app.conf"), silent=False)

from project.api import app