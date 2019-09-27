import calculator as calculator

class FoolCalculator:

        def __init__(self):
            pass

        def sum(self,m,n):
           return calculator.sum(m,n)
        def divide(self,m,n):
           return  calculator.divide(m,n)


foolCalculator = FoolCalculator()

print(foolCalculator.sum(10, 10))
print(foolCalculator.divide(-12,4))
print(foolCalculator.divide(-12,-2))
print(foolCalculator.divide(-12,5))
print(foolCalculator.divide(-12,4))