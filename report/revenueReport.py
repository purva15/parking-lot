import json
from db.db import Sqlite


class RevenueReport:
    """ All the revenue reports are generated through this class"""

    def __init__(self):
        self._db = Sqlite()

    def generateReport(self):
        totalCars, revenue = self._db.getAllCarsRevenue()

        totalParkedCars = self._db.getNoOfParkedCars()

        totalMTCars = self._db.getNoOfParkedCarsByType("MONSTER_TRUCK")

        totalRCars = self._db.getNoOfParkedCarsByType("REGULAR")

        response = {
            "totalCarsServed": totalCars,
            "totalRevenue": revenue,
            "parkedCars": {
                "count": totalParkedCars,
                "monsterTrucks": totalMTCars,
                "regularCars": totalRCars
            }
        }
        return response


if __name__ == "__main__":
    report = RevenueReport()
    report.generateReport()
