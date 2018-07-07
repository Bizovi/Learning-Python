import unittest
import unit_testing as calc

# create class that inherits from unittest.testcase
# gives access to testing capabilities within that class

class TestCalc(unittest.TestCase):

    def test_add(self):
        '''We have access to lots of assert methods'''
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-5, 5), 0)
        self.assertEqual(calc.add(-5, -5), -10)

    def test_subtract(self):
        '''We have access to lots of assert methods'''
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-5, 5), -10)
        self.assertEqual(calc.subtract(-5, -5), 0)

    def test_multiply(self):
        '''We have access to lots of assert methods'''
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-5, 5), -25)
        self.assertEqual(calc.multiply(-5, -5), 25)

    def test_divide(self):
        '''We have access to lots of assert methods'''
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-5, 5), -1)
        self.assertEqual(calc.divide(-5, -5), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        # exception expected, function ran, passed arguments
        # not a preferred method
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # can test it via context manager


if __name__ == '__main__':
    unittest.main()

    # python -m unittest test_calc.py
    # ....
    # ----------------------------------------------------------------------
    # Ran 4 test in 0.001s
    # OK
