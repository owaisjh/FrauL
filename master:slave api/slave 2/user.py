import requests
from flask_restful import Resource, reqparse
from checkfraud import checker

identity=1
API_ENDPOINT = "http://master"

class Service(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('body',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")

    def post(self):
        data = Service.parser.parse_args()
        status = checker(data['body'])




        data ={
                'identity': identity
                }
        r = requests.post(url=API_ENDPOINT, data=data)
        return status, 200
