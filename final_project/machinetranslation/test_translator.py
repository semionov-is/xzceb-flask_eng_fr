"""This is module to test translator"""
import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        """This is function to test translation en-fr"""
        self.assertEqual(englishToFrench(' '), ' ') # test when input is null the output is null.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test when Hello is given as input the output is Bonjour.
        self.assertNotEqual(englishToFrench('Father'), 'Mère')  # test when father is given as input the output is not Mère.

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        """This is function to test translation fr-en"""
        self.assertEqual(frenchToEnglish(' '), ' ') # test when input is null the output is null.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hello.
        self.assertNotEqual(frenchToEnglish('Mère'), 'Father') # test when Mère is given as input the output is not Father.

unittest.main()
