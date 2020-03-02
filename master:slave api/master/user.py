from flask_restful import Resource, reqparse

utility = [
    {
        "ip": "https://slave1.com/service",
        "status": 0
    },
    {
        "ip": "https://slave2.com/service",
        "status": 0
    },
    {
        "ip": "https://slave3.com/service",
        "status": 0
    }
]


class GetUtility(Resource):
    def get(self):
        for i in range(len(utility)):
            if utility[i]["status"] == 0:
                utility[i]["status"] = 1
                return utility[i]["ip"], 200

        return utility[0]["ip"], 200



class UpdateStatus(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('identity',
                        type=int,
                        required=True,
                        help="This field cannot be left blank.")

    def post(self):
        data = UpdateStatus.parser.parse_args()
        utility[data['identity']]["status"] = 0
        return True, 200
