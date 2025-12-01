import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        # Runs before every test method
        self.calc = SimpleCalculator()

    # ---- Addition Test ----
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)

    # ---- Subtraction Test ----
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    # ---- Multiplication Test ----
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    # ---- Division Test ----
    def test_division(self):
        # Normal cases
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)

        # Edge case: division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
