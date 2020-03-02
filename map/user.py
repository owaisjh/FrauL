import requests
from flask_restful import Resource, reqparse
from flask import render_template, Flask
import sqlite3



class add(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('lat',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")
    parser.add_argument('lon',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")

    def post(self):
        data = add.parser.parse_args()
        connection = sqlite3.connect('map.db')
        cursor = connection.cursor()
        query = "INSERT INTO maps VALUES(?, ?)"
        cursor.execute(query, (data["lat"], data["lon"]))
        connection.commit()
        connection.close()
        return True, 200



class reply(Resource):
    def get(self):
        connection = sqlite3.connect('map.db')
        cursor = connection.cursor()
        query = "SELECT * FROM maps"
        result = cursor.execute(query).fetchall()
        connection.commit()
        connection.close()
        return render_template('index.html', locations= result)

