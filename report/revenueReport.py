import json

def generateReport():
	data = open('./data/carData.json','r')
	carData = json.load(data)
	data.close()
	for car in carData.values():
		print(car)
	return True

if __name__ == "__main__":
	generateReport()