from flask import Flask, render_template, request
app = Flask(__name__)

from tp import latest_change

@app.route('/')
def change_in_io():
    data = latest_change()
    return data.to_json()
    
if __name__ == '__main__':
   app.run(debug = True)
