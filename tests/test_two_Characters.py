from coe_number.two_Characters import alternate
import unittest


class TestAlternateCharacters(unittest.TestCase):
    def test_simple_two_characters(self):
        self.assertEqual(alternate("ab"), 2)

    def test_alternating_with_c_acac(self):
        self.assertEqual(alternate("cacac"), 5)

    def test_long_alternating_pattern(self):
        self.assertEqual(alternate("cdcdcdc"), 7)

    def test_empty_string(self):
        self.assertEqual(alternate(""), 0)

    def test_alternate_with_three_characters(self):
        self.assertEqual(alternate("aba"), 3)
