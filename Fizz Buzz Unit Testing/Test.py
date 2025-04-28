import unittest
from Core import FizzBuzz 

class TestFizzBuzz(unittest.TestCase):
    def test_multiple_of_3(self):
        self.assertEqual(FizzBuzz(9), "fizz")

    def test_multiple_of_5(self):
        self.assertEqual(FizzBuzz(10), "buzz")

    def test_multiple_of_3_and_5(self):
        self.assertEqual(FizzBuzz(15), "fizzbuzz")

    def test_neither(self):
        self.assertEqual(FizzBuzz(7), "7")

if __name__ == "__main__":
    unittest.main()
