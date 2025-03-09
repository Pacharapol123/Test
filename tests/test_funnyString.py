from coe_number.funnyString import funnyString
import unittest


class TestFunnyString(unittest.TestCase):
    def test_case_acxz(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_case_bcxz(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_case_a(self):
        self.assertEqual(funnyString("a"), "Funny")

    def test_case_ab(self):
        self.assertEqual(funnyString("ab"), "Funny")

    def test_case_abd(self):
        self.assertEqual(funnyString("abd"), "Not Funny")
