from simple_calc import SimpleCalc
import unittest

class CalcTests(unittest.TestCase):
    calc = SimpleCalc()

    def test_multiply(self):
        actual = self.calc.multiply(2, 2)
        expected = 4
        self.assertEquals(actual, expected)