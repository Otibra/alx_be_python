import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # Create a calculator instance before each test
        self.calc = SimpleCalculator()

    # ---- Addition Tests ----
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)

    # ---- Subtraction Tests ----
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    # ---- Multiplication Tests ----
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    # ---- Division Tests ----
    def test_divide(self):
        # Normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)

        # Edge case: division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)


# Run tests if script is executed directly
if __name__ == "__main__":
    unittest.main()
