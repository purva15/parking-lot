import json
import random

def isParkingAvailable(carType, carNo):
	data = open('./data/parkingSpotData.json','r')
	spots = json.load(data)
	data.close()
	for key, value in spots.items():
		spotId = int(key)
		if value["availability"] == "True":
			if carType == "Regular":
				parkCar(key,carNo,carType)
				return True
			else:
				response = checkConsecutiveSpots()
				if response is not False:
					parkCar(response,carNo,carType)
					return True	

	return False

def checkConsecutiveSpots():
	with open('./data/parkingSpotData.json') as data:
		spots = json.load(data)
		data.close()
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

def parkCar(spotIds,carNo,carType):
	## Updating parking spot data and updating availability to False
	data = open('./data/parkingSpotData.json','r')
	json_object = json.load(data)
	data.close()
	
	for spotId in spotIds:
		json_object[str(spotId)]["availability"] = "False"
	data = open('./data/parkingspotData.json','w')
	json.dump(json_object,data)
	data.close()
	## Updating parking spot data ends here

	## Update carData.json starts here
	carFile = open('./data/carData.json','r+')
	spotValue = ','.join(spotIds)
	
	car_object = {
		"carType": carType,
		"carNo": carNo,
		"spotId":','.join(spotIds) 
	}
	carDict = json.load(carFile)
	carDict.update(car_object)
	carFile.seek(0)
	json.dump(carDict,carFile)
	carFile.close()

	## update carData.json ends here
	return True	

if __name__ == "__main__":
	#print(isParkingAvailable("MonsterTruck"))
	print(isParkingAvailable("Regular","XAZ789789"))	
	
	

