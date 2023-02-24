from flask import Flask
import json, pymysql

import pymysql, os, json

#db instance identifier: database-1
#username: admin
#password: PythonAws2023
#port: 3306
#host: database-1.cm0g4ldq4qxz.eu-west-2.rds.amazonaws.com

def load_table():
    connection = pymysql.connect(host="database-1.cm0g4ldq4qxz.eu-west-2.rds.amazonaws.com", user="admin", password="PythonAws2023")
    cursor = connection.cursor()
    connection.select_db("sys")

    # Execute a SELECT query on the table you want to export as a JSON file
    cursor.execute('SELECT * FROM tblCompanies')

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Convert the rows into a list of dictionaries
    data = []
    for row in rows:
        data.append(dict(zip([column[0] for column in cursor.description], row)))

    connection.close()

    return data
    

app = Flask(__name__)

# Members API Route
@app.route("/")
def listings():
    listings = load_table()
    return listings

if __name__ == "__main__":
    app.run()

