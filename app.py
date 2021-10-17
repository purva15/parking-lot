import json
from flask import Flask, url_for, request
from report.revenueReport import RevenueReport
from exceptionHandler import InvalidAPIUsage
from parkings.parkingSpots import ParkingSpots
from parkings.cars import Cars


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/reserve", methods=["POST"])
def reserve():
    data = request.get_json()
    if not data or not data.get("carNo"):
        raise InvalidAPIUsage("No car details Provided")
    carNo = data["carNo"]
    # carType is optional, default to REGULAR
    carType = data.get("carType", 'REGULAR')
    print(f"carNo={carNo}, carType={carType}")

    parkingSpots = ParkingSpots()
    parkingSpots.isAvailable(carType)

    try:
        response = {
            "carNo": carNo,
            "carType": carType
        }
        if parkingSpots.availableSpots:
            parkingSpots.book()

            car = Cars(carNo, carType)
            car.addCar(parkingSpots.availableSpots)
            response["availability"] = True
            response["location"] = {"spotId": parkingSpots.availableSpots}
        else:
            response["availability"] = False
        print(f"response={response}")
        return json.dumps(response)
    except Exception as err:
        print(err)


@app.route("/report", methods=["GET"])
def report():
    report = RevenueReport()
    response = report.generateReport()
    print(response)
    return json.dumps(response)


# with app.test_request_context():
#    print(url_for('reserve', carType="Regular", carNo="ASDASDAS"))
#    print(url_for('report'))
