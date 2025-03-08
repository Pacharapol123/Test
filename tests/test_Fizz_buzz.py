from coe_number.Fizz_buzz import fizzbuzz
import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_divisible_by_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_divisible_by_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_divisible_by_3_and_5(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_not_divisible_by_3_or_5(self):
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(7), "7")

    def test_zero(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")

    def test_negative_numbers(self):
        self.assertEqual(fizzbuzz(-3), "Fizz")
        self.assertEqual(fizzbuzz(-5), "Buzz")
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")
        self.assertEqual(fizzbuzz(-7), "-7")
