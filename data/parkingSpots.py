import json


class ParkingSpots:
    def checkConsecutiveSpots(self):
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
                    return [currentSpotId, nextSpotId]
                else:
                    continue

        return False

    def isParkingAvailable(self, slotFlag=0):
        if slotFlag == 1:
            return self.checkConsecutiveSpots()
        else:
            data = open('./data/parkingSpotData.json', 'r')
            spots = json.load(data)
            data.close()
            for key, value in spots.items():
                #spotId = int(key)
                if value["availability"] == "True":
                    return key

        return False

    def bookSpots(self, spotIds):
        data = open('./data/parkingSpotData.json', 'r')
        json_object = json.load(data)
        data.close()
        print("In book spots herer spot ids are ",spotIds)
        for spotId in spotIds:
            json_object[str(spotId)]["availability"] = "False"
        data = open('./data/parkingspotData.json', 'w')
        json.dump(json_object, data)
        data.close()
        return True
