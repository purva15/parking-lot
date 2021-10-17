import json
from db.db import Sqlite
from parkings.carTypeEnum import CarTypeEnum


class Cars:
    def __init__(self, carNo, carType='REGULAR'):
        self.carNo = carNo
        self.carType = carType
        self._db = Sqlite()

    def addCar(self, spotId):
        spotValue = ','.join(map(str, spotId))
        money = 10
        if self.carType == CarTypeEnum.MT.value:
            money = 15
        car = (self.carNo, self.carType, spotValue, money)
        response = self._db.addCar(car)
