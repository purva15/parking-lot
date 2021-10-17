import unittest
from report.revenueReport import RevenueReport


class TestReport(unittest.TestCase):
    def testGenerateReport(self):
        report = RevenueReport()
        response = report.generateReport()
        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
