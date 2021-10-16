import json
from data.cars import Cars
from db.db import Sqlite


def generateReport():
    db = Sqlite()
    response = db.getAllCarsRevenue()
    totalCars = response[0][0] 
    revenue = response[0][1]

    response = db.getNoOfParkedCars()
    totalParkedCars = response[0][0]
    print(response)

    response = db.getNoOfParkedCarsByType("MONSTER_TRUCK")
    totalMTCars = response[0][0]

    response = db.getNoOfParkedCarsByType("REGULAR")
    totalRCars = response[0][0]

    json_object = {
        "totalCarsRevenueEarnedFrom" : totalCars,
        "revenue" : revenue,
        "parkedCars": {
            "count" : totalParkedCars,
            "monster_truck" : totalMTCars,
            "regular": totalRCars
        }
    }
    print(json_object)
    return json_object



if __name__ == "__main__":
    generateReport()
