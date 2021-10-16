import json
from db.db import Sqlite


class Cars:


    def addCar(self, no, carType, spotId, money):
        db = Sqlite()
        print("type ", type(spotId))
        print("in add car ",spotId)
        car = (no,carType,spotId,money)
        response = db.addCar(car)
        print("response in add car")


