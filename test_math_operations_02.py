import unittest
from math_operations_02 import MathOperations

class TestMathOperations(unittest.TestCase):
    """
    Unit tests for the MathOperations class.
    """

    def setUp(self):
        """
        Set up an instance of MathOperations before each test.
        """
        self.math_ops = MathOperations()

    def test_add(self):
        """
        Test the add method.
        """
        self.assertEqual(self.math_ops.add(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(self.math_ops.add(-2, 3), 1)  # -2 + 3 = 1
        self.assertEqual(self.math_ops.add(0, 0), 0)  # 0 + 0 = 0

    def test_subtract(self):
        """
        Test the subtract method.
        """
        self.assertEqual(self.math_ops.subtract(10, 5), 5)  # 10 - 5 = 5
        self.assertEqual(self.math_ops.subtract(0, 5), -5)  # 0 - 5 = -5
        self.assertEqual(self.math_ops.subtract(5, 5), 0)  # 5 - 5 = 0

if __name__ == "__main__":
    unittest.main()
