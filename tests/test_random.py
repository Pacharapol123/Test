from coe_number.random import guess_int, guess_float
import unittest


class TestGuessFunctions(unittest.TestCase):
    def test_guess_int_in_range(self):
        start, stop = 1, 10
        result = guess_int(start, stop)
        self.assertGreaterEqual(result, start)
        self.assertLessEqual(result, stop)

    def test_guess_int_negative_range(self):
        start, stop = -10, -1
        result = guess_int(start, stop)
        self.assertGreaterEqual(result, start)
        self.assertLessEqual(result, stop)

    def test_guess_float_in_range(self):
        start, stop = 0.0, 1.0
        result = guess_float(start, stop)
        self.assertGreaterEqual(result, start)
        self.assertLessEqual(result, stop)
        self.assertIsInstance(result, float)

    def test_guess_float_same_start_stop(self):
        start = stop = 5.5
        result = guess_float(start, stop)
        self.assertEqual(result, 5.5)

    def test_guess_int_randomness(self):
        start, stop = 100, 105
        results = set(guess_int(start, stop) for _ in range(100))
        self.assertGreaterEqual(len(results), 2)
