import json
from data.cars import Cars


def generateReport():
    cars = Cars()
    car_json = cars.getCarDetails()
    revenue = 0
    totalCars = len(car_json)
    totalParkedCars = 0
    parkedCarsCountType = {}
    print("car_ json got dfomr the data baseis ",car_json)
    for car in car_json.values():
        revenue += int(car["money"])
        print("car spot ids are ", car["spotId"])
        if car["spotId"] == "0":
            print("And the spot id is 0 that means this cars is not in parking lot right now hence continuing his for loop")
            continue
        print("incremeanting no of parked cars by one")
        totalParkedCars += 1
        print("after incrementing parked car coutn is ",totalParkedCars)
        carType = car["carType"]
        if carType in parkedCarsCountType:
            parkedCarsCountType[carType] += 1
        else:
            parkedCarsCountType[carType] = 1
        print(car)
    print("Total money is ", revenue)
    print("Total cars ", totalCars)
    print("Total Parked car coutn ", totalParkedCars)
    print("Parked car type abd their count ", parkedCarsCountType)
    json_object = {
        "totalCarsRevenueEarnedFrom": totalCars,
        "revenue": revenue,
        "noOfParkedCarsNow": totalParkedCars,
        "parkedCarsCountType": parkedCarsCountType
        }
    print(json_object)
    return json_object


if __name__ == "__main__":
    generateReport()
