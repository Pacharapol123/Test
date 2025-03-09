from coe_number.staircase import staircase
import unittest


class TestStaircase(unittest.TestCase):
    def test_staircase_size_4_hash(self):
        n = 4
        display = "#"
        expected = "   #\n  ##\n ###\n####"
        result = staircase(n, display)
        self.assertEqual(result, expected)

    def test_staircase_size_1_star(self):
        n = 1
        display = "*"
        expected = "*"
        result = staircase(n, display)
        self.assertEqual(result, expected)

    def test_staircase_size_5_A(self):
        n = 5
        display = "A"
        expected = "    A\n   AA\n  AAA\n AAAA\nAAAAA"
        result = staircase(n, display)
        self.assertEqual(result, expected)

    def test_staircase_max_size(self):
        n = 30
        display = "@"
        expected_lines = []
        for i in range(1, 31):
            expected_lines.append(" " * (30 - i) + "@" * i)
        expected = "\n".join(expected_lines)
        result = staircase(n, display)
        self.assertEqual(result, expected)

    def test_staircase_size_4_dollar(self):
        n = 4
        display = "$"
        expected = "   $\n  $$\n $$$\n$$$$"
        result = staircase(n, display)
        self.assertEqual(result, expected)
