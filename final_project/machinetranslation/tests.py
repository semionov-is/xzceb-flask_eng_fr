"""This is module to test translator"""
import unittest

from translator import english_to_french, french_to_english

class TestEnglish_to_french(unittest.TestCase): 
    def test1(self):
        """This is function to test translation en-fr"""
        self.assertEqual(english_to_french(' '), ' ') # test when input is null the output is null.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when Hello is given as input the output is Bonjour.
        self.assertNotEqual(english_to_french('Father'), 'Mère')  # test when father is given as input the output is not Mère.

class TestFrench_to_english(unittest.TestCase): 
    def test1(self):
        """This is function to test translation fr-en"""
        self.assertEqual(french_to_english(' '), ' ') # test when input is null the output is null.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hello.
        self.assertNotEqual(french_to_english('Mère'), 'Father') # test when Mère is given as input the output is not Father.

unittest.main()
