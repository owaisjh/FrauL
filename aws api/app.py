from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS


from user import Service





app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Service, '/service')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
