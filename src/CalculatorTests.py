import unittest
from CsvReader import CsvReader
from Calculator import MyCalculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = MyCalculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, MyCalculator)

    def test_addition(self):
        test_data = CsvReader('src/csv/TestAddition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
