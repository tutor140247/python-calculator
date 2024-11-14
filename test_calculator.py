import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(1, 3), 4)
        self.assertEqual(self.calc.add(1, 4), 5)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 0), 1)
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 0), 0)
        self.assertEqual(self.calc.multiply(2, 1), 2)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(3, 2), 1)
        self.assertEqual(self.calc.modulo(5, 3), 2)

if __name__ == '__main__':
    unittest.main()