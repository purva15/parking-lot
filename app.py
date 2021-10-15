from flask import Flask, url_for
from availability import manageParking
from report import revenueReport

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/availability/<carType>/<carNo>")
def checkAvailability(carType=None, carNo=None):
    response = manageParking.isParkingAvailable(carType, carNo)
    print(response)
    return {
        "availability": response
    }


@app.route("/report")
def generateReport():
    response = revenueReport.generateReport()
    return {
        "response": response
    }


# with app.test_request_context():
 #   print(url_for('checkAvailability', carType="Regular", carNo))
