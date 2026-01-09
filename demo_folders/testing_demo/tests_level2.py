import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator(8,2)

    def test_sum(self):
        answer = self.calc.get_sum()
        self.assertEqual(answer, 10, "The answer wasn't 10.")

    def test_product(self):
        answer = self.calc.get_product()
        self.assertEqual(answer, 16, "The answer wasn't 16.")

    def test_quotient(self):
        answer = self.calc.get_quotient()
        self.assertEqual(answer, 4, "The answer wasn't 10.")

    def test_sub(self):
        answer = self.calc.get_difference()
        self.assertEqual(answer, 6, "The answer wasn't 10.")


if __name__ == "__main__":
    unittest.main()