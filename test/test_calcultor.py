import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)  # Factorial de 0 es 1
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)  # Factorial negativo debe lanzar error

if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()