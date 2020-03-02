from flask_restful import Resource, reqparse
from checkfraud import checker



class Service(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('body',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")

    def post(self):
        data = Service.parser.parse_args()
        status = checker(data['body'])
        return status, 200
