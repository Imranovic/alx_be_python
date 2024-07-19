import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(4, 6), 10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8, 2), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertIsNone(self.calc.divide(6, 0))