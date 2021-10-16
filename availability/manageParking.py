import json
import random
from data.carTypeEnum import CarTypeEnum
from data.cars import Cars
from data.parkingSpots import ParkingSpots


def isParkingAvailable(carType):
    parkingSpots = ParkingSpots()
    parkingFlag = 0
    if carType == CarTypeEnum.MT.value:
        parkingFlag = 1
    response = parkingSpots.isParkingAvailable(parkingFlag)
    print(response)
    return response


def parkCar(spotIds, carNo, carType):
	car = Cars()
	parkingSpots = ParkingSpots()
	parkingSpots.bookSpots(spotIds)

	spotValue = ','.join(map(str, spotIds))
	money = 10
	if carType == CarTypeEnum.MT.value:
		money = 15
	car.addCar(carNo, carType, spotValue, money)
	return True


if __name__ == "__main__":
    McarType = "MONSTER_TRUCK"
    McarNo = "MTTESTING"
    RcarType = "REGULAR"
    RCarNo = "RTESTING"
    response = isParkingAvailable(McarType)
    print("resposnse for monster truck is ", response)
    if response is not False:
        print("Parking is available for monster truck so calling park car function.")
        parkCar(response, McarNo, McarType)

    # r = isParkingAvailable(RcarType)
    # print(r[0])
    # if r is not False:
    #     print("parking is available for regular car hence calling park car function.")
    #     parkCar(r, RCarNo, RcarType)
