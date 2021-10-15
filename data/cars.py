import json


class Cars:
    def getCarDetails(self):
        data = open('./data/carData.json', 'r')
        carData = json.load(data)
        data.close()
        return carData

    def addCar(self,car_object):
        carData = open('./data/carData.json', 'r+') 
        cars = json.load(carData)
        cars.update(car_object)
        carData.seek(0)
        json.dump(cars,carData)   
        carData.close()


if __name__ == "__main__":
    print("Hi I am getting called")
