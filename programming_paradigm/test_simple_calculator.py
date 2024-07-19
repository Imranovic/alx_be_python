import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(4, 6), 10)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8, 2), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertIsNone(self.calc.divide(6, 0))