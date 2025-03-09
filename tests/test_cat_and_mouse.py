from coe_number.cat_and_mouse import cat_and_mouse
import unittest


class CatAndMouseTest(unittest.TestCase):

    def test_give_1_2_3_should_CatB(self):
        self.assertEqual(cat_and_mouse(1, 2, 3), "Cat B")

    def test_give_1_3_2_should_MouseC(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")

    def test_give_1_5_4_should_CatB(self):
        self.assertEqual(cat_and_mouse(1, 5, 4), "Cat B")

    def test_cat_a_wins(self):
        self.assertEqual(cat_and_mouse(1, 4, 2), "Cat A")

    def test_cat_b_wins(self):
        self.assertEqual(cat_and_mouse(4, 1, 2), "Cat B")

    def test_mouse_escapes(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")
