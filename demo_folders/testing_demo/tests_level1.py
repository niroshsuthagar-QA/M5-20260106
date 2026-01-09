import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calc = Calculator(8,2)
        answer = calc.get_sum()
        print(f'The answer was {answer}. \n Test Results:')
        self.assertEqual(answer, 10, "The answer wasn't 10.")

    def test_product(self):
        calc = Calculator(8,2)
        answer = calc.get_product()
        print(f'The answer was {answer}. \n Test Results:')
        self.assertEqual(answer, 16, "The answer wasn't 16.")

    def test_quotient(self):
        calc = Calculator(8,2)
        answer = calc.get_quotient()
        print(f'The answer was {answer}. \n Test Results:')
        self.assertEqual(answer, 4, "The answer wasn't 10.")

    def test_sub(self):
        calc = Calculator(8,2)
        answer = calc.get_difference()
        print(f'The answer was {answer}. \n Test Results:')
        self.assertEqual(answer, 6, "The answer wasn't 10.")

if __name__ == "__main__":
    unittest.main()