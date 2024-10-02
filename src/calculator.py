import math

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    def factorial(self, n):
        if n < 0:
            raise ValueError("Cannot compute factorial of a negative number!")
        return math.factorial(n)

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot compute the square root of a negative number!")
        return math.sqrt(a)

    def log(self, a, base=math.e):
        if a <= 0:
            raise ValueError("Logarithm only defined for positive numbers!")
        return math.log(a, base)

    def sin(self, x):
        return math.sin(x)

    def cos(self, x):
        return math.cos(x)

    def tan(self, x):
        return math.tan(x)
    
    def exp(self, x):
        return math.exp(x)
