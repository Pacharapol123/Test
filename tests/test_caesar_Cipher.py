import unittest
from coe_number.caesar_Cipher import caesarCipher


class TestCaesarCipher(unittest.TestCase):
    def test_case_middleOutz(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_case_ABC(self):
        self.assertEqual(caesarCipher("ABC", 3), "DEF")

    def test_case_Z(self):
        self.assertEqual(caesarCipher("Z", 1), "A")

    def test_case_4(self):
        self.assertEqual(caesarCipher("123-!@#", 4), "123-!@#")

    def test_case_HelloWorld(self):
        self.assertEqual(caesarCipher("Hello, World!", 5), "Mjqqt, Btwqi!")
