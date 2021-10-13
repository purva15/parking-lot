from data.parkingData import spots;
from data import carType as ct;
from  availability import parkingAvailability

def updateAvailabilityOfSpot(spotsToBeReserved):
	for spotId in spotsToBeReserved:
		spots[spotId]["value"] = "False"

		





def parkCar(carType):
	response = parkingAvailability.isParkingAvailable(carType)
	if response is not False:
		updateAvailabilityOfSpot(response)
	else:
		return "Booked by someone else."	
	return response

if __name__ == "__main__":
	print(parkCar("MonsterTruck"))


