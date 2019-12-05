from flask_restplus import Resource


class Hello(Resource):
    def get(self):
        return {"hello": "World!"}