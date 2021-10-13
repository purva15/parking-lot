from flask import Flask, url_for
from availability import parkingAvailability

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

with app.test_request_context():
    print(url_for('checkAvailability', carType="Regular"))    


