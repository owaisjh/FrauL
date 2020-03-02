from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required


from user import Service

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


api = Api(app)

api.add_resource(Service, '/service')


if __name__ == "__main__":
    app.run(port=5000, debug=True)
