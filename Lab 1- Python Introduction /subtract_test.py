import calculator as c
import unittest


class TestSubtract(unittest.TestCase):
    def test_subtract_integers_positive(self):
        result = c.subtract(10, 2)
        self.assertEqual(result, 8)


    def test_subtract_integers_negative(self):
        result = c.subtract(-10, -2)
        self.assertEqual(result, -8)


    def test_subtract_integers_negative_positive(self):
        result = c.subtract(-10, 2)
        self.assertEqual(result,-12)


    def test_subtract_integer_positive_negative(self):
        result = c.subtract(10,-2)
        self.assertEqual(result, 12)