#!/bin/python

from flask import Flask,jsonify,abort,make_response



app = Flask(__name__)



###############################################################################
""" 
HTTP Error handling: Examples showing error returning in josn/(string)message format.
"""
###############################################################################
@app.errorhandler(400)
def bad_request(error):
    #return make_response(jsonify({'error':'Bad Request'}),400)
    return "<h1>Oops! BAD REQUEST</h1>"

@app.errorhandler(401)
def unauthorized(error):
    #return make_response(jsonify({'error':'unauthorized access'}),401)
    return "<h1>Sorry! Page Access not Authorized</h1>"

@app.errorhandler(402)
def payment_required(error):
   #return make_response(jsonify({'error':'payment required'}),402)
   return "<h1>Payment Required</h1>"

@app.errorhandler(403)
def forbidden(error):
    #return make_response(jsonify({'error':'>access forbidden'}),403)
    return "<h1>Access forbidden</h1>"

@app.errorhandler(404)
def not_found(error):
    #return make_response(jsonify({'error':'Not Found'}),404)
    return "<h1>Oops! PAGE NOT FOUND</h1>"
###############################################################################

"""
Example with static path creation
"""
@app.route('/')
def index():
    return "Hello World"

"""
Example with dynamic path creation
"""
@app.route('/example/<name>')
def example(name):
        ret_value = "<h1>Hello <font color=\"red\">" + str(name) + "</font> !</h1>"
        return ret_value

"""
Example with dynamic (path+static) creation
"""
"""
@app.route('/example/<name>/python_dev')
def python_dev(name=None):
    ret_value = "<h1><font color=\"red\">" + str(name) + "</font> is a Python Developer</h1>"
    return ret_value
if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0' ,port=2000)
