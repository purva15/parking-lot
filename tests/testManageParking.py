import unittest
from parkings.parkingSpots import ParkingSpots

class TestManageParking(unittest.TestCase):
    def testParking(self):
        parkingSpots = ParkingSpots()
        response = parkingSpots.isAvailable("REGULAR")
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()        



