from flask import Flask, request
from flask_restful import Resource, Api



from user import GetUtility, UpdateStatus

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)





api = Api(app)



api.add_resource(GetUtility, '/getutil')
api.add_resource(UpdateStatus, '/update')




if __name__ == "__main__":
    app.run(port=5000, debug=True)
