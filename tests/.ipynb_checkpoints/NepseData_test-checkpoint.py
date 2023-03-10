import unittest
import NepseData

class TestNepseData(unittest.TestCase): #For single data
    def test_get_data(self):
        data = NepseData.get_data("adbl")
        self.assertIsInstance(data,tuple),"Data not tuple"
        self.assertIsNotNone(data) ,"Data is None"

    def test_get_multiple_data(self):  #for multiple data
        tickers = ["adbl","nabil","jblb"]
        for data in tickers:
            datas = NepseData.get_data(data)
            self.assertIsInstance(datas,tuple),"Data not tuple"
            self.assertIsNotNone(datas) ,"Data is not None"

            
if __name__ == '__main__':
    unittest.main()
