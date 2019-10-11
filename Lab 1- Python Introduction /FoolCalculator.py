import calculator as calculator


class FoolCalculator:
    def __init__(self):
        pass

    def sum(self, m, n):
        return calculator.sum(m, n)

    def divide(self, m, n):
        return calculator.divide(m, n)

    def subtract(self, m, n):
        return calculator.subtract(m, n)

    def multiply(self, m, n):
        return calculator.multiply(m, n)

    def gcd(self, m, n):
        return calculator.gcd(m, n)


foolCalculator = FoolCalculator()

print('Subraction of  (-10) - (-5) = {}'.format(foolCalculator.subtract(-10, -5)))
print('Subraction of  (-10) - (5) = {}'.format(foolCalculator.subtract(-10, 5)))
print('Subraction of  (10) - (5) = {}'.format(foolCalculator.subtract(10, 5)))
print('Subraction of  (10) - (-5) = {}'.format(foolCalculator.subtract(10, -5)))

print('Sum of  (-10) + (-5) = {}'.format(foolCalculator.sum(-10, -5)))
print('Sum of  (-10) + (5) = {}'.format(foolCalculator.sum(-10, 5)))
print('Sum of  (10) + (5) = {}'.format(foolCalculator.sum(10, 5)))
print('Sum of  (10) + (-5) = {}'.format(foolCalculator.sum(10, -5)))

print('Division of  (-10) / (-5) = {}'.format(foolCalculator.divide(-10, -5)))
print('Division of  (-10) / (5) = {}'.format(foolCalculator.divide(-10, 5)))
print('Division of  (10) / (5) = {}'.format(foolCalculator.divide(10, 5)))
print('Division of  (10) / (-7) = {}'.format(foolCalculator.divide(10, -7)))

print('Multiplication of  (-10) * (-5) = {}'.format(foolCalculator.multiply(-10, -5)))
print('Multiplication of  (-10) * (5) = {}'.format(foolCalculator.multiply(-10, 5)))
print('Multiplication of  (10) * (5) = {}'.format(foolCalculator.multiply(10, 5)))
print('Multiplication of  (10) * (-7) = {}'.format(foolCalculator.multiply(10, -7)))

print('GCD of -10 and -5 = {}'.format(foolCalculator.gcd(-10, -5)))
print('GCD of -10 and 5 = {}'.format(foolCalculator.gcd(-10, 5)))
print('GCD of 10 and 5 = {}'.format(foolCalculator.gcd(10, 5)))
print('GCD of 10 and -5 = {}'.format(foolCalculator.gcd(10, -5)))
