from flask import Flask, request, jsonify
from flask_cors import CORS


from fnoData import ParticipantData as fno

app = Flask(__name__)
cors = CORS(app)


@app.route("/receiver", methods=["GET"])
def get_eod_data():
    today = fno(date="15122022")
    data = today.end_of_day_data()
    data = jsonify(data)
    return data

# main driver function
if __name__ == '__main__':
    app.run(port=9000, debug=True)
