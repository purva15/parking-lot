import unittest
import report.revenueReport as rReport


class TestReport(unittest.TestCase):
    def testGenerateReport(self):
        response = rReport.generateReport()
        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
