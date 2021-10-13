import json


def isParkingAvailable(carType):
	with open('./data/parkingSpotData.json') as data:
		spots = json.load(data)
	for key, value in spots.items():
		spotId = int(key)
		if value["availability"]:
			if carType == "Regular":
				parkCar(spotId,value)
				print("new spots = ",spots)
				with open("./data.parkingSpotData.json","w") as a_file:
					json.dumps(spots)
					a_file.close()
				return True
			else:
				response = checkConsecutiveSpots()
				if response is not False:
					#parkCar(response,value)
					return True	

	return False

def checkConsecutiveSpots():
	with open('./data/parkingSpotData.json') as data:
		spots = json.load(data)
	for key, value in spots.items():
		currentSpotId = int(key)
		currentBlockId = int(value["blockId"])
		if value["availability"] == "False":
			continue
		for nextKey, nextValue in spots.items():
			nextSpotId = int(nextKey)
			if nextValue["availability"] == "False":
				continue
			nextBlockId = int(nextValue["blockId"])
			if abs(currentSpotId - nextSpotId == 1) and currentBlockId == nextBlockId:
				return [currentSpotId,nextSpotId]
			else:
				continue

	return False

def parkCar(spotIds,value):
	a_file = open("./data.parkingSpotData.json","w")
	print(spotIds)
	value["availability"] = "False"
	print("Nee Value", value)
	#json_object[spotIds]: value
	return True	

if __name__ == "__main__":
#	print(isParkingAvailable("MonsterTruck"))
#	print(isParkingAvailable("Regular"))	
	a_file = opne("./data/parkingSpotData.json","w")
	

