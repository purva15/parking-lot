import json


def generateReport():
    data = open('./data/carData.json', 'r')
    carData = json.load(data)
    data.close()
    revenue = 0
    totalCars = len(carData)
    totalParkedCars = 0
    parkedCarsCountType = {}
    print(totalParkedCars)
    for car in carData.values():
        revenue += int(car["money"])
        if car["spotId"] == "0":
            continue
        totalParkedCars += 1
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
