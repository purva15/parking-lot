import unittest
from parkings.cars import Cars


class TestCar(unittest.TestCase):
    def testAddCar(self):
        car = Cars("testNo", "REGULAR")
        response = car.addCar("1as", "10as")
        self.assertIsNone(response=None)


if __name__ == "__main__":
    unittest.main()
