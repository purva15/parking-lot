from flask import Flask, url_for, request
from availability import manageParking
from report import revenueReport


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/reserve", methods=["POST"])
def checkAvailability():
    data = request.get_json()
    print(data)
    response = manageParking.isParkingAvailable(data["carType"])
    print(response)
    if response is not False:
        isCarParked = manageParking.parkCar(response, data["carNo"], data["carType"])
        print(isCarParked)
    return {
        "availability": isCarParked
    }


@app.route("/report")
def generateReport():
    response = revenueReport.generateReport()
    return {
        "response": response
    }


# with app.test_request_context():
 #   print(url_for('checkAvailability', carType="Regular", carNo))
