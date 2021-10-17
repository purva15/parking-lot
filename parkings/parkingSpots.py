import json
from db.db import Sqlite


class ParkingSpots:
    """ParkingSpots manages the parking spot data and methods."""

    def __init__(self):
        self.availableSpots = None
        self._db = Sqlite()

    def _checkConsecutiveSpots(self):
        """ Private method to determine 2 consecutive available spots"""
        response = self._db.getAllAvailableParkingSpots()
        for tup in response:
            currentSpotId = int(tup[0])
            currentBlockId = int(tup[1])
            for nextTup in response:
                nextSpotId = int(nextTup[0])
                nextBlockId = int(nextTup[1])
                if abs(currentSpotId - nextSpotId == 1) and currentBlockId == nextBlockId:
                    self.availableSpots = [currentSpotId, nextSpotId]
                    return

    def isAvailable(self, carType="REGULAR"):
        if carType == "MONSTER_TRUCK":
            self._checkConsecutiveSpots()
        elif carType == "REGULAR":
            self._db = Sqlite()
            availableSpot = self._db.getAvailableParkingSpot()
            if availableSpot:
                self.availableSpots = [availableSpot]
        print(f"availableSpots = {self.availableSpots}")
        return self.availableSpots

    def book(self):
        response = self._db.bookSpots(self.availableSpots)
