"""This is module to test translator"""
import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        """This is function to test translation en-fr"""
        self.assertEqual(englishToFrench(''), '') # test when input is null the output is null.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test when Hello is given as input the output is Bonjour.

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        """This is function to test translation fr-en"""
        self.assertEqual(frenchToEnglish(''), '') # test when input is null the output is null.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hello.

unittest.main()


"""Write at least 2 tests in tests.py for each method
Test for null input for frenchToEnglish
Test for null input for englishToFrench.
Test for the translation of the world ‘Hello’ and ‘Bonjour’.
Test for the translation of the world ‘Bonjour’ and ‘Hello' """