import json
from db.db import Sqlite


class ParkingSpots:

    def checkConsecutiveSpots(self):
        db = Sqlite()
        response = db.getAllAvailableParkingSpots()
        for tup in response:
            currentSpotId = int(tup[0])
            currentBlockId = int(tup[1])
            for nextTup in response:
                nextSpotId = int(nextTup[0])
                nextBlockId = int(nextTup[1])
                if abs(currentSpotId - nextSpotId == 1) and currentBlockId == nextBlockId:
                    return [currentSpotId, nextSpotId]
                else:
                    continue

        return False

    def isParkingAvailable(self, slotFlag=0):
        if slotFlag == 1:
            return self.checkConsecutiveSpots()
        else:
            db = Sqlite()
            response = db.getAvailableParkingSpot()
            print(response[0])
            return key

        return response[0]

    def bookSpots(self, spotIds):
        db = Sqlite()
        response = db.bookSpots(spotIds)
        return True
