from flask_restplus import Api
from resources import api
from flask import Flask
from app_v1 import blueprint as bp_v1

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(bp_v1)

    from Model import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)