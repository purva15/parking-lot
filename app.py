from flask import Flask, url_for
from availability import parkingAvailability
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/availability/<carType>")
def checkAvailability(carType="Regular"):
    response = parkingAvailability.isParkingAvailable(carType)
    print(response)
    return {
        "availability" : response
    }

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

with app.test_request_context():
    print(url_for('checkAvailability', carType="Regular"))  




