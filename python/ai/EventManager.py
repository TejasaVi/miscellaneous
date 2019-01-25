#!/bin/python


import datetime
import pprint as pprint
from collections import OrderedDict
from DataBaseManager import DataBaseManager
from flask import Flask,jsonify,abort, make_response, request
PATH = "./test.db"


app = Flask(__name__)


@app.route('/insert', methods = ['POST'])
def insert():
    db = DataBaseManager(path=PATH)
    db.get_db_connection()
    dt = OrderedDict()
    dt["name"]= request.json['name']
    dt["activity"] = request.json['activity']
    dt["time"] = datetime.datetime.now()
    db.db_insert_table("TIMEPASS", dt)
    db.con.commit()
    res = db.db_get_data("TIMEPASS")
    db.db_connection_close()
    return jsonify({'tasks': res}), 200

@app.route('/list')
def list():
    db = DataBaseManager(path=PATH)
    db.get_db_connection()
    res = db.db_get_data("TIMEPASS")
    db.db_connection_close()
    return jsonify({'tasks': res}), 200


if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0' ,port=2000)


