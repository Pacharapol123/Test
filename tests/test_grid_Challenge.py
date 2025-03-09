from coe_number.grid_Challenge import gridChallenge
import unittest


class TestGridChallenge(unittest.TestCase):
    def test_sample_case_yes(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_unsorted_columns(self):
        grid = ["abc", "lmp", "qrt", "xyw", "def"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_small_grid_yes(self):
        grid = ["abc", "hjk", "mpq", "rtv"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_row_reordering_yes(self):
        grid = ["cba", "daf", "ghi"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_all_rows_reverse_no(self):
        grid = ["zyx", "wvu", "tsr"]
        self.assertEqual(gridChallenge(grid), "NO")
