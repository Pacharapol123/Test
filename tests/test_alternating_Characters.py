from coe_number.alternating_Characters import alternatingCharacters
import unittest


class TestAlternatingCharacters(unittest.TestCase):
    def test_all_same_A(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_all_same_B(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)

    def test_alternating_AB(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_alternating_BA(self):
        self.assertEqual(alternatingCharacters("BABABA"), 0)

    def test_mixed_AAABBB(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)
