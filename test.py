import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(5, 5), 10)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(55, 5), 50)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(7, 8), 56)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(100, 5), 20)


if __name__ == "__main__":
    unittest.calculator()
