"""
    __add__(): By using thos method we can control the sum of two objects bu modifying this method.
"""
class Calculator:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
    
    def __add__(self, other):
        f = self.feet + other.feet
        i = (self.inches + other.inches)
        return Calculator(f + i // 12, i % 12)
    
c1 = Calculator(3, 9)
c2 = Calculator(2, 7)
c3 = c1 + c2
print(f"{c3.feet}.{c3.inches}")

