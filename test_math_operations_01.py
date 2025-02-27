# test_math_operations.py

import unittest
from math_operations_01 import add, multiply, subtract

class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 3), -3)
        self.assertEqual(subtract(10, 10), 0)

    def test_multiply(self):
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(2, 2), 4)

if __name__ == "__main__":
    unittest.main()
