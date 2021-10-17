import json
from db.db import Sqlite
from parkings.carTypeEnum import CarTypeEnum


class Cars:
    REGULAR_CAR_MONEY = 10
    MT_MONEY = 15
    def __init__(self, carNo, carType='REGULAR'):
        self.carNo = carNo
        self.carType = carType
        self._db = Sqlite()

    def addCar(self, spotId):
        spotValue = ','.join(map(str, spotId))
        money = self.REGULAR_CAR_MONEY
        if self.carType == CarTypeEnum.MT.value:
            money = self.MT_MONEY
        car = (self.carNo, self.carType, spotValue, money)
        response = self._db.addCar(car)
