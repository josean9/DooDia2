import unittest
import sys
import os

# Añadir el directorio 'test' al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'test')))

from test_calcultor import TestCalculator

if __name__ == '__main__':
    unittest.main()
