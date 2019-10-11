import calculator as c
import unittest


class TestGCD(unittest.TestCase):
    def test_gcd_integers_positive(self):
        result = c.gcd(32, 12)
        self.assertEqual(result, 4)

    def test_gcd_integers_negative(self):
        result = c.gcd(-32, -12)
        self.assertEqual(result, 4)

    def test_gcd_integers_positive_negative(self):
        result = c.gcd(32, -12)
        self.assertEqual(result, 4)

    def test_gcd_integers_negative_positive(self):
        result = c.gcd(-32, 12)
        self.assertEqual(result, 4)
