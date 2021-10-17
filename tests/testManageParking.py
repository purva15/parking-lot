import unittest
import availability.manageParking as parking


class TestManageParking(unittest.TestCase):
    def testParking(self,carType):
        response = parking.isParkingAvailable("REGULAR")
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()        



