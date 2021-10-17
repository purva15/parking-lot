import json
from flask import Flask, url_for, request, jsonify
from report.revenueReport import RevenueReport
from exceptionHandler import InvalidAPIUsage
from parkings.parkingSpots import ParkingSpots
from parkings.cars import Cars


app = Flask(__name__)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict())


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/reserve", methods=["POST"])
def reserve():
    try:
        data = request.get_json()
        if not data or not data.get("carNo"):
            raise InvalidAPIUsage("Insuficient car details", "BAD_INPUT")
        carNo = data["carNo"]
        # carType is optional, default to REGULAR
        carType = data.get("carType", 'REGULAR')
        print(f"carNo={carNo}, carType={carType}")

        parkingSpots = ParkingSpots()
        parkingSpots.isAvailable(carType)

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
    except InvalidAPIUsage as e:
        raise e
    except Exception as err:
        print(err)
        raise InvalidAPIUsage(err, "FAILED")


@app.route("/report", methods=["GET"])
def report():
    try:
        report = RevenueReport()
        response = report.generateReport()
        print(response)
        return json.dumps(response)
    except Exception as err:
        print(err)
        raise InvalidAPIUsage(err, "FAILED")


# with app.test_request_context():
#    print(url_for('reserve', carType="Regular", carNo="ASDASDAS"))
#    print(url_for('report'))
