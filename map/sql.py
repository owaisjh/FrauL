import sqlite3

connection = sqlite3.connect('map.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS maps(lat float, lon float)"

cursor.execute(create_table)


connection.commit()

connection.close()