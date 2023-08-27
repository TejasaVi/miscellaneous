from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

@app.route("/receiver", methods=["GET"])
def postME():
    data = request.get_json()
    data = {"Tejas":"Vaykole"}
    data = jsonify(data)
    return data
if __name__ == "__main__":
    app.run(port=9000,debug=True)
