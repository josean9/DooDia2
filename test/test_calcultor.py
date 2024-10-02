import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator import Calculator


import unittest
import math

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

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(16), 4)
        self.assertEqual(self.calc.sqrt(0), 0)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)

    def test_log(self):
        self.assertAlmostEqual(self.calc.log(math.e), 1)
        self.assertAlmostEqual(self.calc.log(100, 10), 2)
        with self.assertRaises(ValueError):
            self.calc.log(0)  # Logaritmo de 0 debe lanzar error
        with self.assertRaises(ValueError):
            self.calc.log(-10)  # Logaritmo de un número negativo debe lanzar error

    def test_trigonometric(self):
        self.assertAlmostEqual(self.calc.sin(math.pi / 2), 1)
        self.assertAlmostEqual(self.calc.cos(math.pi), -1)
        self.assertAlmostEqual(self.calc.tan(math.pi / 4), 1)

    def test_exp(self):
        self.assertAlmostEqual(self.calc.exp(1), math.e)
        self.assertAlmostEqual(self.calc.exp(0), 1)

