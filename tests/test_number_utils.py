from coe_number.number_utils import is_prime_list
import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_true(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_1_2_4_is_false(self):
        prime_list = [1, 2, 4]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_empty_list_is_true(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_5_7_11_is_true(self):
        prime_list = [5, 7, 11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_0_1_is_true(self):
        prime_list = [0, 1]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_9_is_false(self):
        prime_list = [9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_2_3_5_7_is_true(self):
        prime_list = [2, 3, 5, 7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
