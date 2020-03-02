from flask import Flask,request,jsonify, render_template
import sqlite3



app = Flask(__name__)



@app.route('/add',methods = ["POST"])
def add():
    data = request.get_json()
    connection = sqlite3.connect('map.db')
    cursor = connection.cursor()
    query = "INSERT INTO maps VALUES(?, ?)"
    cursor.execute(query, (data["lat"], data["lon"]))
    connection.commit()
    connection.close()
    return jsonify(data)


@app.route('/get')
def get_map():
    connection = sqlite3.connect('map.db')
    cursor = connection.cursor()
    query = "SELECT * FROM maps"
    result = cursor.execute(query).fetchall()
    connection.commit()
    connection.close()
    return render_template('index.html', locations=result)


if __name__ == "__main__":
    app.run(port=5858, debug=True)
