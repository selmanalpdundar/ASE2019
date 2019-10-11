import calculator as c
import unittest

class TestMulyiply(unittest.TestCase):
    def test_multiply_integers_positivie(self):
        result = c.multiply(5,2)
        self.assertEqual(result,10)

    def test_multiply_integers_negative(self):
        result = c.multiply(-5,-2)
        self.assertEqual(result,10)

    def test_multiply_integers_negative_positive(self):
        result = c.multiply(-5,2)
        self.assertEqual(result,-10)

    def test_multiply_integers_positive_negative(self):
        result = c.multiply(5,-2)
        self.assertEqual(result,-10)